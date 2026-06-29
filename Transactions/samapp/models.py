from django.db import models

# Create your models here.
class Transaction(models.Model):
    description = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description


