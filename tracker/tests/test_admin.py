from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from tracker.models import MealPlan, Food


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            username="john11",
            first_name="John",
            last_name="Doe",
            password="111222John",
            weight=70.5,
            height=175.0,
            age=25,
            fitness_goals="Stay fit",
        )

        self.meal_plan = MealPlan.objects.create(
            creator=self.admin_user,
            title="Test Meal Plan",
            description="Test Meal Plan Description",
        )
        self.meal_plan.users.add(self.user)

        self.food = Food.objects.create(
            name="Test Food",
            calories=100.0,
            protein=10.0,
            carbs=20.0,
            fats=5.0,
        )
        self.meal_plan.foods.add(self.food)

    def test_user_listed(self):
        url = reverse("admin:tracker_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.last_name)

    def test_user_detail_listed(self):
        url = reverse("admin:tracker_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.last_name)

    def test_meal_plan_listed(self):
        url = reverse("admin:tracker_mealplan_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.meal_plan.title)

    def test_meal_plan_detail_listed(self):
        url = reverse("admin:tracker_mealplan_change", args=[self.meal_plan.id])
        res = self.client.get(url)
        self.assertContains(res, self.meal_plan.title)

    def test_food_listed(self):
        url = reverse("admin:tracker_food_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.food.name)

    def test_food_detail_listed(self):
        url = reverse("admin:tracker_food_change", args=[self.food.id])
        res = self.client.get(url)
        self.assertContains(res, self.food.name)

    def test_add_food_detail_listed(self):
        url = reverse("admin:tracker_food_add")
        res = self.client.get(url)
        self.assertTrue(res, self.food.name)
