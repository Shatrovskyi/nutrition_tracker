from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, MealPlan, NutritionTracker, Food


@login_required
def index(request):
    """View function for the home page of the site."""

    num_users = User.objects.count()
    num_meal_plans = MealPlan.objects.count()
    num_foods = Food.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_users": num_users,
        "num_meal_plans": num_meal_plans,
        "num_foods": num_foods,
        "num_visits": num_visits + 1,
    }

    return render(request, "tracker/index.html", context=context)


class MealPlanListView(LoginRequiredMixin, generic.ListView):
    model = MealPlan
    context_object_name = "meal_plan_list"
    template_name = "tracker/meal_plan_list.html"


class NutritionTrackerListView(LoginRequiredMixin, generic.ListView):
    model = NutritionTracker
    template_name = "tracker/nutrition_tracker_list.html"
    paginate_by = 5

    def get_queryset(self):
        return NutritionTracker.objects.filter(user=self.request.user).order_by("-date")


class FoodListView(LoginRequiredMixin, generic.ListView):
    model = Food
    template_name = "tracker/food_list.html"
    paginate_by = 6


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "tracker/user_list.html"
    paginate_by = 6
