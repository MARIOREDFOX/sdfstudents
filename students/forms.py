from django.forms import ModelForm
from .models import Students

class StudentForms(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'