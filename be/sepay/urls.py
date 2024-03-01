from django.urls import path
from .views import download_all_transaction, webhook_handler

urlpatterns = [
    path('download_all_transaction/', download_all_transaction),
    path('webhook/', webhook_handler),
]
