from django.urls import path
from .views import custom_login
from django.urls import path
from .views import BookList, BookDetail, UserProfileDetail, OrderList, OrderDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('login/', custom_login, name='custom-login'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('user/profile/', UserProfileDetail.as_view(), name='user-profile'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]
