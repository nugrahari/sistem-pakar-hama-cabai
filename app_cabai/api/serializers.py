from rest_framework import serializers
from app_cabai.models import (
	JenisPenyakit,
	Hama,
	Solusi,
	Permasalahan,

    CFPakar,
    CFPengguna,
) 

class JenisPenyakitSerializer(serializers.ModelSerializer):
	class Meta:
		model = JenisPenyakit
		fields = '__all__'

class HamaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hama
		fields = '__all__'

class SolusiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Solusi
		fields = '__all__'

class PermasalahanSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permasalahan
		fields = '__all__'

class CFPakarSerializer(serializers.ModelSerializer):
	class Meta:
		model = CFPakar
		fields = '__all__'

class CFPenggunaSerializer(serializers.ModelSerializer):
	class Meta:
		model = CFPengguna
		fields = '__all__'

class CFPenggunaSerializer2(serializers.ModelSerializer):
	hama = HamaSerializer()
	class Meta:
		model = CFPengguna
		fields = '__all__'



