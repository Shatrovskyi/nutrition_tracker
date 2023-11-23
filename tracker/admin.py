from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MealPlan, NutritionTracker, Food


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "weight",
        "height",
        "age",
    )
    search_fields = ("username", "first_name", "last_name", "email", "weight", "height", "age")
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("weight", "height", "age", "fitness_goals")}),)
    )
    list_filter = ("age",)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "weight",
                        "height",
                        "age",
                        "fitness_goals",
                    )
                },
            ),
        )
    )


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "get_users_count", "get_foods_count")
    search_fields = ("title", "description", "creator__username")
    list_filter = ("creator", "foods")

    def get_users_count(self, obj):
        return obj.users.count()

    def get_foods_count(self, obj):
        return obj.foods.count()

    get_users_count.short_description = "Users Count"
    get_foods_count.short_description = "Foods Count"


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "calories", "protein", "carbs", "fats", "get_meal_plans_count")
    search_fields = ("name", "protein", "carbs", "fats")
    list_filter = ("meal_plans",)

    def get_meal_plans_count(self, obj):
        return obj.meal_plans.count()

    get_meal_plans_count.short_description = "Meal Plans Count"


admin.site.register(NutritionTracker)
