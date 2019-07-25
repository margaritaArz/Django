from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import BasketSlot
from mainapp.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def basket(request):
    content = {}
    return render(request, 'basketapp/basketapp.html', content)

@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = BasketSlot.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = BasketSlot(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, pk):
    content = {}
    return render(request, 'basketapp/basketapp.html', content)


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        basket_slot = get_object_or_404(BasketSlot, pk=pk)

        quantity = int(request.GET.get('quantity'))
        if quantity > 0:
            basket_slot.quantity = quantity
            basket_slot.save()
        else:
            basket_slot.delete()

    return HttpResponseRedirect ('ok')