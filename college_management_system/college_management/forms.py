# college_management/forms.py
from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code']
