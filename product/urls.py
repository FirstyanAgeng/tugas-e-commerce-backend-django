from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from product import views 

router = DefaultRouter()
router.register('list_product', views.ProductViewSet)
router.register('list_order', views.ListOrderViewSet)
router.register('order_item', views.OrderItemViewSet)

app_name = 'product' 

urlpatterns = [
    path('', include(router.urls))
]
