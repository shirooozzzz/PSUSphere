from django.forms import ModelForm
from django import forms
from .models import Organization, College, Student, Program, OrgMember


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['prog_name', 'college']

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = ['student', 'organization', 'date_joined']