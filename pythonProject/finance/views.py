from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import TransactionFilter


# Create your views here.

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all().order_by('-date')
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TransactionFilter
    # filterset_fields = ['account','date','amount']
    ordering_fields = ['date']

    def get_queryset(self):
        queryset = super().get_queryset()
        accounts = self.request.query_params.getlist('accounts')
        if accounts:
            queryset = queryset.filter(account__in=accounts)
        return queryset


class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id']


class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
