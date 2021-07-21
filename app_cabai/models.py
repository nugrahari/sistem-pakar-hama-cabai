from django.db import models

# Create your models here.
class JenisPenyakit(models.Model):
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField(blank=True, null=True)
	value1 = models.FloatField(blank=True, null=True)
	value2 = models.FloatField(blank=True, null=True)
	def __str__(self):
		return "{}. {}".format(self.id, self.nama)

class Hama(models.Model):
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField(blank=True, null=True)
	value1 = models.FloatField(blank=True, null=True)
	value2 = models.FloatField(blank=True, null=True)
	def __str__(self):
		return "{}. {}".format(self.id, self.nama)

class Solusi(models.Model):
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField(blank=True, null=True)
	def __str__(self):
		return "{}. {}".format(self.id, self.deskripsi)

class Permasalahan(models.Model):
	nama_masalah 		=	models.CharField(max_length=100)
	hama 				= 	models.ManyToManyField(Hama)
	solusi        		=   models.ManyToManyField(Solusi, blank=True, null=True)
	jenis_penyakit 		=   models.ManyToManyField(JenisPenyakit, blank=True, null=True)
	penjelasan			=	models.TextField(blank=True, null=True)

	def __str__(self):
		return "{}. {}".format(self.id, self.nama_masalah)