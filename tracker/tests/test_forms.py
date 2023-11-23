from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from tracker.models import MealPlan, Food

MEAL_PLAN_URL = reverse("tracker:meal-plan-list")
USER_URL = reverse("tracker:user-list")
FOOD_URL = reverse("tracker:food-list")


class FormsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )

    def setUp(self):
        self.client.force_login(self.user)

    def test_user_search_by_username(self):
        self.user1 = get_user_model().objects.create(
            username="testuser2",
            password="testpassword2",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )

        self.user2 = get_user_model().objects.create(
            username="testuser1",
            password="testpassword1",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Lose fat",
        )

        response = self.client.get(USER_URL, {"username": "testuser2"})
        users = get_user_model().objects.filter(username__icontains="testuser2")
        self.assertEqual(list(response.context["user_list"]), list(users))

    def test_meal_plan_search_by_title(self):
        self.user1 = get_user_model().objects.create(
            username="testuser2",
            password="testpassword2",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )

        self.user2 = get_user_model().objects.create(
            username="testuser1",
            password="testpassword1",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Lose fat",
        )

        MealPlan.objects.create(
            creator=self.user1,
            title="Test Meal Plan",
            description="Test Meal Plan Description",
        )
        MealPlan.objects.create(
            creator=self.user2,
            title="Different Plan",
            description="Test Meal Plan Description",
        )

        response = self.client.get(MEAL_PLAN_URL, {"title": "Test Meal"})
        meal_plans = MealPlan.objects.filter(title__icontains="Test Meal Plan")
        self.assertEqual(
            list(response.context["meal_plan_list"]), list(meal_plans)
        )

    def test_food_search_by_name(self):
        self.food = Food.objects.create(
            name="Test Food",
            calories=101.0,
            protein=10.0,
            carbs=20.0,
            fats=5.0,
        )

        response = self.client.get(FOOD_URL, {"name": "Test Food"})
        foods = Food.objects.filter(name__icontains="Test")
        self.assertEqual(list(response.context["food_list"]), list(foods))
