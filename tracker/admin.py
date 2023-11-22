from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MealPlan, NutritionTracker, Food


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("weight", "height", "age")
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
                        "fitness_goals"
                    )
                },
            ),
        )
    )


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("foods",)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
        "protein",
        "carbs",
        "fats",
    )
    list_filter = ("meal_plans",)


admin.site.register(NutritionTracker)
