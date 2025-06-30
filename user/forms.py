from django import forms 
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

<<<<<<< HEAD

=======
>>>>>>> 9654802f352f96a2d64cd40f428950642c5acea8
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

<<<<<<< HEAD
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']
=======
>>>>>>> 9654802f352f96a2d64cd40f428950642c5acea8
