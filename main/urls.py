from django.urls import path
from . import views

urlpatterns = [
    path('buyer/', views.buyer_page, name='buyer'),
    path('seller/', views.seller_page, name='seller'),
    path('create_order/', views.CreateOrder.as_view(), name='create_order'),
    path('', views.index, name='index'),
    path('order_detail/<int:pk>', views.order_detail, name='order_detail'),
    path('order_edit/<int:pk>', views.OrderEdit.as_view(), name='order_edit'),
    # path('add_offer/<int:order_pk>', views.add_offer, name='add_offer'),
    # path('delete_order/<int:order_pk>', views.delete_order, name='delete_order'),
    # path('cancel_offer/<int:order_pk>', views.cancel_offer, name='cancel_offer'),
    path('order_action/<int:pk>', views.OrderAction.as_view(), name='order_action')
]
