from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CashFlowCategory(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nama
    class Meta:
        verbose_name = _("Kategori")
        verbose_name_plural = _("Kategori")

class CashFlow(models.Model):
    kategory = models.ForeignKey(CashFlowCategory, on_delete=CASCADE, null=True)
    tanggal = models.DateTimeField('Tanggal Transaksi')
    nama_item = models.CharField(max_length=200)
    qty = models.IntegerField(default=1)
    harga_satuan = models.FloatField(default=0.0)
    harga_total = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.nama_item
    
    class Meta:
        verbose_name = _("Arus Keuangan")
        verbose_name_plural = _("Arus Keuangan")

    @property
    def harga_total(self):
        return self.qty * self.harga_satuan