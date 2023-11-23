from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from tracker.forms import (
    MealPlanTitleSearchForm,
    UserMainUsernameSearchForm,
    FoodNameSearchForm
)
from tracker.models import Food, MealPlan

MEAL_PLAN_URL = reverse("tracker:meal-plan-list")
USER_URL = reverse("tracker:user-list")
FOOD_URL = reverse("tracker:food-list")
NUTRITION_TRACKER = reverse("tracker:nutrition-tracker-list")
HOME_PAGE = reverse("tracker:index")


class PublicPageTest(TestCase):
    def test_login_required(self):
        res1 = self.client.get(MEAL_PLAN_URL)
        res2 = self.client.get(USER_URL)
        res3 = self.client.get(FOOD_URL)
        res4 = self.client.get(NUTRITION_TRACKER)
        res5 = self.client.get(HOME_PAGE)

        self.assertNotEqual(res1.status_code, 200)
        self.assertNotEqual(res2.status_code, 200)
        self.assertNotEqual(res3.status_code, 200)
        self.assertNotEqual(res4.status_code, 200)
        self.assertNotEqual(res5.status_code, 200)


class PrivatePageTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )
        self.client.force_login(self.user)

    def test_retrieve_home_user_food_meal_plan_tracker_list(self):
        res1 = self.client.get(MEAL_PLAN_URL)
        res2 = self.client.get(USER_URL)
        res3 = self.client.get(FOOD_URL)
        res4 = self.client.get(NUTRITION_TRACKER)
        res5 = self.client.get(HOME_PAGE)

        self.assertEqual(res1.status_code, 200)
        self.assertEqual(res2.status_code, 200)
        self.assertEqual(res3.status_code, 200)
        self.assertEqual(res4.status_code, 200)
        self.assertEqual(res5.status_code, 200)


class MealPlanListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )
        self.client.force_login(self.user)

        self.food = Food.objects.create(
            name="Test Food",
            calories=101.0,
            protein=10.0,
            carbs=20.0,
            fats=5.0,
        )

        self.meal_plan = MealPlan.objects.create(
            creator=self.user,
            title="Test Meal Plan",
            description="Test Meal Plan Description",
        )

        self.meal_plan.users.add(self.user)
        self.meal_plan.foods.add(self.food)

    def test_meal_plan_list_view_with_search(self):
        response = self.client.get(MEAL_PLAN_URL, {"title": "Test Meal"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Meal Plan")
        self.assertNotContains(response, "Different Plan")

    def test_meal_plan_list_view_without_search(self):
        response = self.client.get(MEAL_PLAN_URL)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Meal")

    def test_meal_plan_list_view_context_data(self):
        response = self.client.get(MEAL_PLAN_URL)

        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertIsInstance(
            response.context["search_form"],
            MealPlanTitleSearchForm
        )


class UserListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )
        self.client.force_login(self.user)

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

    def test_user_list_view_with_search(self):
        response = self.client.get(USER_URL, {"username": "testuser1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser1")
        self.assertNotContains(response, "testuser2")

    def test_user_list_view_without_search(self):
        response = self.client.get(USER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser1")
        self.assertContains(response, "testuser2")

    def test_user_list_view_context_data(self):
        response = self.client.get(USER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertIsInstance(
            response.context["search_form"],
            UserMainUsernameSearchForm
        )


class FoodListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )
        self.client.force_login(self.user)

        self.food1 = Food.objects.create(
            name="Test Food1",
            calories=500.0,
            protein=11.0,
            carbs=2.0,
            fats=55.0,
        )
        self.food2 = Food.objects.create(
            name="Test Food2",
            calories=100.0,
            protein=10.0,
            carbs=20.0,
            fats=5.0,
        )

    def test_food_list_view_with_search(self):
        response = self.client.get(
            FOOD_URL, {"name": "Test Food1"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Food1")
        self.assertNotContains(response, "Test Food2")

    def test_food_list_view_without_search(self):
        response = self.client.get(FOOD_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Food1")
        self.assertContains(response, "Test Food2")

    def test_food_list_view_context_data(self):
        response = self.client.get(FOOD_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("search_form", response.context)
        self.assertIsInstance(
            response.context["search_form"], FoodNameSearchForm
        )
