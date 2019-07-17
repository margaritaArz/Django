from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from .forms import ShopUserRegisterForm
from .models import ShopUser

def main(request):
    context = {'username': 'Иван', 'array': [1, 2, 3, 4, 5]}
    return render(request, 'mainapp/main.html', context=context)



def products(request):
    return render(request, 'mainapp/products')

def contacts(request):
    return render(request, 'mainapp/contacts')

def login(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=login, password=password)
        print(login, password)

        if user:
            auth.login(request, login)
            return HttpResponseRedirect(reverse('main'))

    else:
       return render(request, 'authapp/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

def register(request):


    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        form = ShopUserRegisterForm()

    context = {'form': ShopUserRegisterForm()}
    return render(request, 'authapp/register.html', context)


class EditView(UpdateView):
    model = ShopUser
    template_name = 'authapp/register.html'
    fields = 'username', 'first_name', 'age', 'avatar'
    success_url = reverse_lazy('main')






