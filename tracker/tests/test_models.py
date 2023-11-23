from django.contrib.auth import get_user_model
from django.test import TestCase
from tracker.models import MealPlan, NutritionTracker, Food


class FoodModelTest(TestCase):
    def setUp(self):
        self.food = Food.objects.create(
            name="Test Food",
            calories=100.0,
            protein=10.0,
            carbs=20.0,
            fats=5.0,
        )

    def test_food_str(self):
        food = Food.objects.get(id=1)
        expected_object_name = "Test Food"
        self.assertEqual(str(food), expected_object_name)


class UserModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )

    def test_user_str(self):
        user = get_user_model().objects.get(id=1)
        expected_object_name = f"{user.username} ({user.first_name} {user.last_name})"

        self.assertEqual(str(user), expected_object_name)


class MealPlanModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )

        self.food = Food.objects.create(
            name="Test Food",
            calories=100.0,
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

    def test_meal_plan_str(self):
        meal_plan = MealPlan.objects.get(id=1)
        expected_object_name = "Test Meal Plan"
        self.assertEqual(str(meal_plan), expected_object_name)


class NutritionTrackerModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            age=25,
            weight=70.5,
            height=175.0,
            fitness_goals="Stay fit",
        )

        self.food = Food.objects.create(
            name="Test Food",
            calories=100.0,
            protein=10.0,
            carbs=20.0,
            fats=5.0,
        )

        self.nutrition_tracker = NutritionTracker.objects.create(
            user=self.user,
            food=self.food,
            serving_size=150,
            meal_type="Lunch",
            user_notes="Test notes",
        )

    def test_nutrition_tracker_str(self):
        nutrition_tracker = NutritionTracker.objects.get(id=1)
        expected_object_name = (
            f"{nutrition_tracker.user.username} "
            f"({nutrition_tracker.meal_type}{nutrition_tracker.food.name})"
        )
        self.assertEqual(str(nutrition_tracker), expected_object_name)
