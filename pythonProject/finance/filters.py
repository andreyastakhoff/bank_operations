import django_filters
from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    accounts = django_filters.BaseInFilter(field_name="account_id", lookup_expr="in", required=False)
    date_from = django_filters.DateFilter(field_name="date", lookup_expr="gte", required=False)
    date_to = django_filters.DateFilter(field_name="date", lookup_expr="lte", required=False)
    amount_from = django_filters.NumberFilter(field_name="amount", lookup_expr="gte", required=False)
    amount_to = django_filters.NumberFilter(field_name="amount", lookup_expr="lte", required=False)

    class Meta:
        model = Transaction
        fields = ['accounts', 'date_from', 'date_to', 'amount_from', 'amount_to']
