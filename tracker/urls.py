from django.urls import path

from .views import (
    index,
    UserListView,
    MealPlanListView,
    FoodListView,
    NutritionTrackerListView,
    MealPlanCreateView,
    MealPlanUpdateView,
    MealPlanDeleteView,
    UserCreateView,
    UserUpdateView,
    UserDetailView,
    UserWeightUpdateView,
    UserDeleteView,
    FoodCreateView,
    FoodUpdateView,
    FoodDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("meal_plans/", MealPlanListView.as_view(), name="meal-plan-list"),
    path("foods/", FoodListView.as_view(), name="food-list"),
    path(
        "nutrition_trackers/",
        NutritionTrackerListView.as_view(),
        name="nutrition-tracker-list"
    ),
    path(
        "meal_plans/create/",
        MealPlanCreateView.as_view(),
        name="meal-plan-create"
    ),
    path(
        "meal_plans/<int:pk>/update/",
        MealPlanUpdateView.as_view(),
        name="meal-plan-update"
    ),
    path(
        "meal_plans/<int:pk>/delete/",
        MealPlanDeleteView.as_view(),
        name="meal-plan-delete"
    ),
    path(
        "foods/create/",
        FoodCreateView.as_view(),
        name="food-create"
    ),
    path(
        "foods/<int:pk>/update/",
        FoodUpdateView.as_view(),
        name="food-update"
    ),
    path(
        "foods/<int:pk>/delete/",
        FoodDeleteView.as_view(),
        name="food-delete"
    ),
    path(
        "users/create/",
        UserCreateView.as_view(),
        name="user-create"
    ),
    path(
        "users/<int:pk>/update/",
        UserUpdateView.as_view(),
        name="user-update"
    ),
    path(
        "users/<int:pk>/delete/",
        UserDeleteView.as_view(),
        name="user-delete"
    ),
    path(
        "users/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail"
    ),
    path(
        "users/<int:pk>/update/weight/",
        UserWeightUpdateView.as_view(),
        name="user-weight-update"
    )

]

app_name = "tracker"
