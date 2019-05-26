from django import forms

from .models import List, HumanName, Category


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["state", "date", "human_name", "category", "money", "memo", "deadline"]