from django.forms import ModelForm
from users.models import Student

class AddStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone_number', 'birthday', 'payment', 'group']