from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_TYPES = [
        (0, 'Sipariş Oluşturulmadı.'),
        (1, 'Onay Bekliyor'),
        (2, 'Onaylandı'),
        (3, 'Kargoya Verildi'),
        (4, 'Teslim Edildi.'),
        (5, 'Onaylanmadı.'),
    ]
    status = models.IntegerField(choices=STATUS_TYPES, default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.CharField(default="0", max_length=10)
    name = models.CharField(max_length=50, default="İsim")
    surname = models.CharField(max_length=50, default="Soyisim")
    province = models.CharField(max_length=100, default="İl")
    district = models.CharField(max_length=100, default="İlçe")
    phone = models.CharField(max_length=15, default="5554443322")
    address = models.TextField(default="Adres")


class Product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    image = models.FileField()
    description = models.TextField()

    def __str__(self):
        return self.description


class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
