from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.


def register(request):
    if request.method == 'POST':
<<<<<<< HEAD
       form =  CreateUserForm(request.POST)
=======
       form = CreateUserForm(request.POST)
>>>>>>> 03eb2df070ad671ff4df716b591dc6de1ebd9fde
       if form.is_valid():
           form.save()
           return redirect('user-login')
    else:
<<<<<<< HEAD
        form =  CreateUserForm()
=======
        form = CreateUserForm()
>>>>>>> 03eb2df070ad671ff4df716b591dc6de1ebd9fde
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)


def profile(request):
    return render(request, 'user/profile.html')
