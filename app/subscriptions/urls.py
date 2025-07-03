from django.urls import path
from .views import SubscriptionList, SubscriptionDetail

urlpatterns = [
    path('subscriptions/', SubscriptionList.as_view(), name='subscription-list'),
    path('subscriptions/<int:pk>/', SubscriptionDetail.as_view(), name='subscription-detail'),
]