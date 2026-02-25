from django.forms import ModelForm
from django import forms
from .models import Organization, College


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"