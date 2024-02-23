from django.urls import path

from .views import user_orders, upload_image, add_product

urlpatterns = [
    path('user_orders/<int:user_id>/', user_orders, name='user_orders'),
    path('image/', upload_image, name='upload_image'),
    path('product/', add_product, name='add_product'),
]
