from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, MealPlan, NutritionTracker, Food
from .forms import (
    UserMainCreationForm,
    UserMainUsernameSearchForm,
    UserMainUpdateWeightForm,
    FoodNameSearchForm,
    MealPlanTitleSearchForm,
    MealPlanForm,
)


@login_required
def index(request):
    """View function for the home page of the site."""

    num_users = User.objects.count()
    num_meal_plans = MealPlan.objects.count()
    num_foods = Food.objects.count()

    context = {
        "num_users": num_users,
        "num_meal_plans": num_meal_plans,
        "num_foods": num_foods,
    }

    return render(request, "tracker/index.html", context=context)


class MealPlanListView(LoginRequiredMixin, generic.ListView):
    model = MealPlan
    context_object_name = "meal_plan_list"
    template_name = "tracker/meal_plan_list.html"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MealPlanListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = MealPlanTitleSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        form = MealPlanTitleSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class MealPlanDetailView(LoginRequiredMixin, generic.DetailView):
    model = MealPlan


class MealPlanCreateView(LoginRequiredMixin, generic.CreateView):
    model = MealPlan
    form_class = MealPlanForm
    success_url = reverse_lazy("tracker:meal-plan-list")


class MealPlanUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = MealPlan
    form_class = MealPlanForm
    success_url = reverse_lazy("tracker:meal-plan-list")


class MealPlanDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = MealPlan
    success_url = reverse_lazy("tracker:meal-plan-list")


class NutritionTrackerListView(LoginRequiredMixin, generic.ListView):
    model = NutritionTracker
    template_name = "tracker/nutrition_tracker_list.html"
    paginate_by = 5

    def get_queryset(self):
        return NutritionTracker.objects.filter(user=self.request.user).order_by("-date")


class NutritionTrackerCreateView(LoginRequiredMixin, generic.CreateView):
    model = NutritionTracker
    fields = "__all__"
    success_url = reverse_lazy("tracker:nutrition-tracker-list")


class FoodListView(LoginRequiredMixin, generic.ListView):
    model = Food
    template_name = "tracker/food_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = FoodNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        form = FoodNameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class FoodCreateView(LoginRequiredMixin, generic.CreateView):
    model = Food
    fields = "__all__"
    success_url = reverse_lazy("tracker:food-list")


class FoodUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Food
    fields = "__all__"
    success_url = reverse_lazy("tracker:food-list")


class FoodDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Food
    success_url = reverse_lazy("tracker:food-list")


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "tracker/user_list.html"
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = UserMainUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        form = UserMainUsernameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserMainCreationForm


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    queryset = User.objects.all().prefetch_related("meal_plans__foods")


class UserWeightUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UserMainUpdateWeightForm
    success_url = reverse_lazy("tracker:user-list")


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("tracker:user-list")


def meal_plan_add_user(request: HttpRequest, pk: int) -> HttpResponse:
    MealPlan.objects.get(id=pk).users.add(request.user)
    return redirect(f"/meal-plan/{pk}/")


def meal_plan_delete_user(request: HttpRequest, pk: int) -> HttpResponse:
    MealPlan.objects.get(id=pk).users.remove(request.user)
    return redirect(f"/meal-plan/{pk}/")
