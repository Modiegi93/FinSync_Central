from django.db import models

# Create your models here.


class Table(models.Model):
    """Table model"""
    creator = models.ForeignKey('accounts.Staff', on_delete=models.CASCADE)
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    date = models.DateField()
    items = models.ManyToManyField('Item')

    def __str__(self):
        """Return string representation of Table"""
        return self.name


class Item(models.Model):
    """Item model"""
    name = models.CharField(max_length=40)
    money_change = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """Return string representation of Item"""
        return self.name
