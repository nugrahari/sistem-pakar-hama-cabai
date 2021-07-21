from django.contrib import admin

# Register your models here.
from .models import (
	JenisPenyakit,
	Hama,
	Solusi,
	Permasalahan,
)

class JenisPenyakitAdmin(admin.ModelAdmin):
	# list_display = [field.name for field in JenisPenyakit._meta.get_fields()]
	list_display = ['nama','deskripsi','value1','value2']
	search_fields = ['nama','deskripsi','value1','value2']

class HamaAdmin(admin.ModelAdmin):
	list_display = ['nama','deskripsi','value1','value2']
	search_fields = ['nama','deskripsi','value1','value2']

class SolusiAdmin(admin.ModelAdmin):
	list_display = ['nama','deskripsi']
	search_fields =  ['nama','deskripsi']

class PermasalahanAdmin(admin.ModelAdmin):
	list_display = ['nama_masalah', 'penjelasan']
	search_fields = ['nama_masalah', 'penjelasan']

# admin.site.register(JenisPenyakit)
# admin.site.register(Hama)
# admin.site.register(Solusi)
# admin.site.register(Permasalahan)

admin.site.register(JenisPenyakit, JenisPenyakitAdmin)
admin.site.register(Hama, HamaAdmin)
admin.site.register(Solusi, SolusiAdmin)
admin.site.register(Permasalahan, PermasalahanAdmin)


