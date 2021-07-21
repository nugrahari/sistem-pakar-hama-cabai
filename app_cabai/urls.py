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
]