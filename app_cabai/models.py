from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Hama(models.Model):
	kode = models.CharField(max_length=100, unique=True)
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField(blank=True, null=True)
	def __str__(self):
		return "{}. {}".format(self.id, self.nama)

class Solusi(models.Model):
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField(blank=True, null=True)
	def __str__(self):
		return "{}. {}".format(self.id, self.deskripsi)

class JenisPenyakit(models.Model):
	kode = models.CharField(max_length=100, unique=True)
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField(blank=True, null=True)
	solusi = models.ManyToManyField(Solusi, blank=True, null=True)
	def __str__(self):
		return "{}. {}".format(self.id, self.nama)


class CFPakar(models.Model):
	jenis_penyakit = models.ForeignKey(JenisPenyakit, on_delete=models.CASCADE, blank=True, null=True)
	hama = models.ForeignKey(Hama, on_delete=models.CASCADE, blank=True, null=True)
	value = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
	def __str__(self):
		return "{}. | {} | {}".format(self.id, self.jenis_penyakit, self.hama)

class Permasalahan(models.Model):
	nama_masalah 		=	models.CharField(max_length=100)
	jenis_penyakit 		=   models.ManyToManyField(JenisPenyakit, blank=True, null=True)
	keterangan			=	models.CharField(max_length=100, default='Belum dilakukan diagnosis penyakit')
	penjelasan			=	models.TextField(default='Belum dilakukan diagnosis penyakit')

	def __str__(self):
		return "{}. {}".format(self.id, self.nama_masalah)



class CFPengguna(models.Model):
	nama_masalah = models.ForeignKey(Permasalahan, on_delete=models.CASCADE, blank=True, null=True)
	hama = models.ForeignKey(Hama, on_delete=models.CASCADE, blank=True, null=True)
	value = models.FloatField(blank=True, null=True, validators=[MinValueValidator(-1.0), MaxValueValidator(1.0)])
	def __str__(self):
		return "{}. | {} | {}".format(self.id, self.nama_masalah, self.hama)