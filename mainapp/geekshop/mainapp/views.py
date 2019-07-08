from django.shortcuts import render


def main(request):
    context = {'username': 'Иван', 'array': [1, 2, 3, 4, 5]}
    return render(request, 'mainapp/main.html', context=context)

def products(request):
    return render(request, 'mainapp/products')

def contacts(request):
    return render(request, 'mainapp/contacts')

# Create your views here.



