from django.db import models
from django.contrib.auth.models import AbstractUser


class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fats = models.FloatField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    fitness_goals = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class MealPlan(models.Model):
    users = models.ManyToManyField(User, related_name="meal_plans")
    foods = models.ManyToManyField(Food, related_name="meal_plans")
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_meal_plans",
    )
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class NutritionTracker(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="nutrition_trackers"
    )
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name="nutrition_trackers"
    )
    date = models.DateTimeField(auto_now_add=True)
    serving_size = models.IntegerField()
    meal_type = models.CharField(max_length=255)
    user_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.meal_type}{self.food.name})"
