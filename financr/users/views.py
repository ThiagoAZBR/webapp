from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
 
def dashboard(request):
    return render(request, "users/dashboard.html")
 
def register(request):
    print(request.POST) 
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
            
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            print('')
            print(form.non_field_errors)
            print(form.errors)
            return render(request, "users/error.html", {'form':form})