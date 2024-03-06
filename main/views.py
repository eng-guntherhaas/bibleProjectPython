from django.shortcuts import render, redirect

from .forms import CreateUserForm


def homepage(request):
    return render(request, 'main/index.html')


def registre(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context = {'registerform': form}

    return render(request, 'main/registre.html', context=context)


def my_login(request):
    return render(request, 'main/my-login.html')


def day_lecture(request):
    return render(request, 'main/day-lecture.html')


def recherche(request):
    return render(request, 'main/recherche.html')
