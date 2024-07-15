from rest_framework import serializers
from finance.models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'balance']


class TransactionSerializer(serializers.ModelSerializer):
    account_balance = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    class Meta:
        model = Transaction
        fields = ['id', 'account_id', 'amount', 'date', 'account_balance']
