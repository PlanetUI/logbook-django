from django.db import models

# Create your models here.
class CashFlow(models.Model):
    tanggal = models.DateTimeField('Tanggal Transaksi')
    nama_item = models.CharField(max_length=200)
    qty = models.IntegerField(default=1)
    harga_satuan = models.FloatField(default=0.0)
    harga_total = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.nama_item