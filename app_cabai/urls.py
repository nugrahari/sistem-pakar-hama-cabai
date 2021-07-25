from django.urls import path
from app_cabai.api.views import(

	JenisPenyakitAPI,
	JenisPenyakitDetailAPI,
	HamaAPI,
	HamaDetailAPI,
	SolusiAPI,
	SolusiDetailAPI,
	PermasalahanAPI,
	PermasalahanDetailAPI,
	diagnosis,
	input_cf_pengguna,
	CFPenggunaAPI,
	CFPenggunaFilterAPI,
	CFPenggunaDetailAPI
)


urlpatterns = [
    path('api/JenisPenyakitAPI', JenisPenyakitAPI.as_view(), name='JenisPenyakitAPI'),
    path('api/JenisPenyakitAPI/<pk>', JenisPenyakitDetailAPI.as_view(), name='JenisPenyakitDetailAPI'),

    path('api/HamaAPI', HamaAPI.as_view(), name='HamaAPI'),
    path('api/HamaAPI/<pk>', HamaDetailAPI.as_view(), name='HamaDetailAPI'),

    path('api/SolusiAPI', SolusiAPI.as_view(), name='SolusiAPI'),
    path('api/SolusiAPI/<pk>', SolusiDetailAPI.as_view(), name='SolusiDetailAPI'),

    path('api/PermasalahanAPI', PermasalahanAPI.as_view(), name='PermasalahanAPI'),
    path('api/PermasalahanAPI/<pk>', PermasalahanDetailAPI.as_view(), name='PermasalahanDetailAPI'),


    path('api/CFPenggunaAPI', CFPenggunaAPI.as_view(), name='CFPenggunaAPI'),
    path('api/CFPenggunaFilterAPI/<id>', CFPenggunaFilterAPI.as_view(), name='CFPenggunaFilterAPI'),
    path('api/CFPenggunaAPI/<pk>', CFPenggunaDetailAPI.as_view(), name='CFPenggunaDetailAPI'),


    path('api/input_cf_pengguna', input_cf_pengguna, name='input_cf_pengguna'),
    path('api/diagnosis/<id_masalah>', diagnosis, name='diagnosis'),

]