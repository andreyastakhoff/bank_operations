from django.urls import path
from .views import AccountListCreateView, TransactionListCreateView, TransactionDeleteView

urlpatterns = [
    path('accounts', AccountListCreateView.as_view(), name='account-list-create'),
    path('transactions', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>', TransactionDeleteView.as_view(), name='transaction-delete'),
]
