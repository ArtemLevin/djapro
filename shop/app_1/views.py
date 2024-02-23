from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from app_1.models import User, Order, Product
from app_1.forms import ImageForm, ProductForm


def user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user).order_by('-pk')
    orders_7 = Order.objects.filter(customer=user).filter(order_date__gte=datetime.now() - timedelta(days=7)).order_by(
        '-pk')
    orders_30 = Order.objects.filter(customer=user).filter(
        order_date__gte=datetime.now() - timedelta(days=30)).order_by('-pk')
    orders_365 = Order.objects.filter(customer=user).filter(
        order_date__gte=datetime.now() - timedelta(days=365)).order_by('-pk')
    return render(request, 'app_1/user_orders.html', {'user': user, 'orders': orders,
                                                      'orders_7': set(orders_7),
                                                      'orders_30': set(orders_30) - set(orders_7),
                                                      'orders_365': set(orders_365) - set(orders_30) - set(orders_7)})

def upload_image(request):
    if request.method == 'POST':
        form =ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'app_1/upload_image.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Error data'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            add_date = form.cleaned_data['add_date']
            image = form.cleaned_data['image']

            product = Product(name=name, description=description, price=price, add_date=add_date, image=image)
            product.save()
            message = 'Product saved'
    else:
        form = ProductForm()
        message = 'Fill the form'

    return render(request, 'app_1/product_form.html', {'form': form, 'message': message})