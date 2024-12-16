from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.error(request, f'{product.model_name} already exists in your basket. Please choose another product.')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.model_name} to your basket.')

    request.session['bag'] = bag
    # For Test Purposes
    # print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping basket """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.model_name} from your basket.')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)