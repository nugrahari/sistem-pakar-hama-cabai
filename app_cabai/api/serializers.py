from rest_framework import serializers
from app_cabai.models import (
	JenisPenyakit,
	Hama,
	Solusi,
	Permasalahan,
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

		



