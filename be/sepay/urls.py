from django.urls import path
from .views import download_all_sepay_transaction

urlpatterns = [
    path('download_all_transaction/', download_all_sepay_transaction)
]
