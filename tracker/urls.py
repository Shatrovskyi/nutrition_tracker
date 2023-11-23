from django.urls import path

from .views import (
    index,
    UserListView,
    MealPlanListView,
    FoodListView,
    NutritionTrackerListView,
    MealPlanCreateView,
    MealPlanDetailView,
    MealPlanUpdateView,
    MealPlanDeleteView,
    UserCreateView,
    UserDetailView,
    UserWeightUpdateView,
    UserDeleteView,
    FoodCreateView,
    FoodUpdateView,
    FoodDeleteView,
    NutritionTrackerCreateView,
    meal_plan_add_user,
    meal_plan_delete_user,
)


urlpatterns = [
    path("", index, name="index"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("meal-plans/", MealPlanListView.as_view(), name="meal-plan-list"),
    path("foods/", FoodListView.as_view(), name="food-list"),
    path(
        "nutrition_tracker/",
        NutritionTrackerListView.as_view(),
        name="nutrition-tracker-list",
    ),
    path("meal-plan/create/", MealPlanCreateView.as_view(), name="meal-plan-create"),
    path("meal-plan/<int:pk>/", MealPlanDetailView.as_view(), name="meal-plan-detail"),
    path(
        "meal-plan/<int:pk>/update/",
        MealPlanUpdateView.as_view(),
        name="meal-plan-update",
    ),
    path(
        "meal-plan/<int:pk>/delete/",
        MealPlanDeleteView.as_view(),
        name="meal-plan-delete",
    ),
    path("food/create/", FoodCreateView.as_view(), name="food-create"),
    path("food/<int:pk>/update/", FoodUpdateView.as_view(), name="food-update"),
    path("food/<int:pk>/delete/", FoodDeleteView.as_view(), name="food-delete"),
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("user/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path(
        "user/<int:pk>/update/weight/",
        UserWeightUpdateView.as_view(),
        name="user-weight-update",
    ),
    path(
        "nutrition_tracker/create/",
        NutritionTrackerCreateView.as_view(),
        name="nutrition-tracker-create",
    ),
    path("meal-plan/<int:pk>/add-user/", meal_plan_add_user, name="meal-plan-add-user"),
    path(
        "meal-plan/<int:pk>/delete-user/",
        meal_plan_delete_user,
        name="meal-plan-delete-user",
    ),
]

app_name = "tracker"
