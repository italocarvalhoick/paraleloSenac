from . models import Product
from . forms import Product_search_form

def product_links(request):
    product = Product.objects.all()
    return {'produto': product}

def perfume_search(request):
    search_form = Product_search_form
    if request.method == 'POST':
        search_form = Product_search_form(request.POST)
        if search_form.is_valid():
            search_form.save()
    return{'search_form': search_form}