from django.db import models


# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    account = models.ForeignKey(Account, related_name='transactions',
                                on_delete=models.CASCADE)  # Связь с моделью Account, будет храниться как account_id
    date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def account_balance(self):
        transactions = Transaction.objects.filter(account=self.account, date__lte=self.date).order_by('date')
        balance = 0
        for transaction in transactions:
            balance += transaction.amount
        return balance

    def save(self, *args, **kwargs):  # Добавление/сохранение операции.
        super().save(*args, **kwargs)
        self.account.balance += self.amount
        self.account.save()

    def delete(self, *args, **kwargs):
        self.account.balance -= self.amount
        self.account.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.account.name} - {self.date} - {self.amount}"
