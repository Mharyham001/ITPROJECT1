from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

<<<<<<< HEAD

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
=======
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

>>>>>>> 03eb2df070ad671ff4df716b591dc6de1ebd9fde
