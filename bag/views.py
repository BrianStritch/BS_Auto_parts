# imports
# 3rd party imports from django
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.db.models import Q

# internal imports from BS_Auto_parts
from products.models import Product, Category, Manufacturer


def view_bag(request):    
    """ A view to return the shopping bag contents page """

    products = Product.objects.all()
    makes = Manufacturer.objects.all().order_by('name')

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        
        
        current_sorting = f'{sort}_{direction}'

        context = {
        'products': products,
        'makes':makes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        }
        return render(request, 'products/products.html', context)

    else:

        return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ add a quantity of the selected product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'You have succesfully added another "{product.name}" size "{size.upper()}" to the shopping bag.')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'You have succesfully added "{product.name}" size "{size.upper()}" to the shopping bag.')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'You have succesfully added "{quantity}" of our "{product.name}" size "{size.upper()}" to the shopping bag.')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'You have succesfully added another "{product.name}" to the shopping bag.')
        else:
            bag[item_id] = quantity
            messages.success(request, f'You have succesfully added "{product.name}" to the shopping bag.')

    request.session['bag'] = bag 
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """ edit a quantity of the selected product in the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'You have succesfully edited the quantity of "{product.name}" size "{size.upper()}" in your shopping bag.')
        else:
            del bag[item_id]['items_by_size'][size]
            messages.success(request, f'You have succesfully removed "{product.name}" size "{size.upper()}" from your shopping bag.')
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request, f'You have succesfully removed "{product.name}" size "{size.upper()}" from your shopping bag.')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'You have succesfully edited the quantity of "{product.name}" in your shopping bag.')
        else:
            bag.pop(item_id)
            messages.success(request, f'You have succesfully removed "{product.name}" from your shopping bag.')

    request.session['bag'] = bag 
    return redirect(reverse('view_bag'))


def delete_bag_item(request, item_id):
    """ remove a selected product from the shopping bag """

    try:
        product = Product.objects.get(pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            messages.success(request, f'You have succesfully removed "{product.name}" size "{size}" from your shopping bag.')
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request, f'You have succesfully removed "{product.name}" size "{size}" from your shopping bag.')
        else:        
            bag.pop(item_id)
            messages.success(request, f'You have succesfully removed "{product.name}" from your shopping bag.')

        request.session['bag'] = bag 
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)

