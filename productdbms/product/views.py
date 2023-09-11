from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductCreate

# Read
def index(request):
    for_action = []
    for chosen in Product.objects.all():
        product = Product.objects.get(id=chosen.id)
        for_action.append({
            'form': ProductCreate(request.POST or None, instance=product),
            'product': product
        })
    context_dict = {
        'products': Product.objects.all(),
        'form': ProductCreate,
        'for_action': for_action
    }
    return render(request, 'product/index.html', context_dict)

# Create
def add(request):
    # check whether form was submitted
    if request.method == 'POST':
        # get form data
        form = ProductCreate(request.POST)

        # check whether form is valid
        if form.is_valid():
            form.save() # save new product
            return redirect('product:index')
        else:
            return HttpResponse('''Error''')
    else:
        form = ProductCreate()

    return redirect('product:index')

# Update
def update(request, product_id):
    # get ID of product
    product_id = int(product_id)

    # check whether product exists
    try:
        product = Product.objects.get(id=product_id) # if exists, get product
    except Product.DoesNotExist:
        return redirect('product:index') # if not exists, redirect 
    
    # get form data
    product_form = ProductCreate(request.POST or None, instance=product)

    # check whether form is valid
    if product_form.is_valid():
        product_form.save() # save changes made to product
        return redirect('product:index')
    else:
        return HttpResponse('''Error''')

# Delete
def delete(request, product_id):
    # get ID of product
    product_id = int(product_id)
    
    # check whether product exists
    try:
        product = Product.objects.get(id=product_id) # if exists, get product
    except Product.DoesNotExist:
        return redirect('product:index') # if not exists, redirect 
    
    # delete product
    product.delete()

    return redirect('product:index')