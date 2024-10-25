from django.db import models

class Product(models.Model):
    nama = models.CharField(max_length=200)
    kategori = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    nama_restoran = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=300)

    def __str__(self):
        return self.nama
