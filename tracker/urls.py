from django.urls import path

from .views import (
    index,
    UserListView,
    MealPlanListView,
    FoodListView,
    NutritionTrackerListView
)


urlpatterns = [
    path("", index, name="index"),
    path("users/", UserListView.as_view(), name="users"),
    path("meal_plans/", MealPlanListView.as_view(), name="meal_plans"),
    path("foods/", FoodListView.as_view(), name="foods"),
    path(
        "nutrition_trackers/",
        NutritionTrackerListView.as_view(),
        name="nutrition_trackers"
    ),

]

app_name = "tracker"
