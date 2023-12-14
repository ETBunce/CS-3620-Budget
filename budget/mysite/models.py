from django.db import models

# Create your models here.


class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    balance = models.FloatField()


class Budget(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    balance = models.FloatField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)


class Transaction(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    amount = models.FloatField()
    budget = models.ForeignKey(to=Budget, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
