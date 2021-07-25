from django.contrib import admin

# Register your models here.
from .models import (
	JenisPenyakit,
	Hama,
	Solusi,
	Permasalahan,
	CFPakar,
	CFPengguna,
)

class JenisPenyakitAdmin(admin.ModelAdmin):
	list_display = ['kode','nama','deskripsi']
	search_fields = ['kode','nama','deskripsi']

class HamaAdmin(admin.ModelAdmin):
	list_display = ['kode','nama','deskripsi']
	search_fields = ['kode','nama','deskripsi']

class SolusiAdmin(admin.ModelAdmin):
	list_display = ['nama', 'deskripsi']
	search_fields =  ['nama', 'deskripsi']

class PermasalahanAdmin(admin.ModelAdmin):
	list_display = ['id','nama_masalah', 'penjelasan']
	search_fields = ['nama_masalah', 'penjelasan']

# admin.site.register(JenisPenyakit)
# admin.site.register(Hama)
# admin.site.register(Solusi)
# admin.site.register(Permasalahan)

admin.site.register(JenisPenyakit, JenisPenyakitAdmin)
admin.site.register(Hama, HamaAdmin)
admin.site.register(Solusi, SolusiAdmin)
admin.site.register(Permasalahan, PermasalahanAdmin)
admin.site.register(CFPakar)
admin.site.register(CFPengguna)


