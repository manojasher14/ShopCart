from django.shortcuts import render
from .models import Product

# Create your views here.
def add_cart (request , product_id):
    product = Product.objects.get(id=product_id)
    # try:
    #     cart = request.session['cart']



def cart(request):
    return render(request, 'store/cart.html')