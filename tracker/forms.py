from django import forms
from django.contrib.auth.forms import UserCreationForm
from tracker.models import User, MealPlan, Food


class MealPlanForm(forms.ModelForm):
    foods = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = MealPlan
        fields = "__all__"


class UserMainCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "age",
            "weight",
            "height",
            "fitness_goals"
        )


class UserMainUpdateWeightForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["weight"]


class UserMainUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class MealPlanTitleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )


class FoodNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by food name"}),
    )
