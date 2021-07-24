from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from app_cabai.models import (
    JenisPenyakit,
    Hama,
    Solusi,
    Permasalahan,
    CFPakar,
    CFPengguna,
) 
from .serializers import (
    JenisPenyakitSerializer,
    HamaSerializer,
    SolusiSerializer,
    PermasalahanSerializer,
)


class JenisPenyakitAPI(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = JenisPenyakit.objects.all()
        serializer = JenisPenyakitSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JenisPenyakitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JenisPenyakitDetailAPI(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return JenisPenyakit.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = JenisPenyakitSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = JenisPenyakitSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------------------

class HamaAPI(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Hama.objects.all()
        serializer = HamaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HamaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HamaDetailAPI(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Hama.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = HamaSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = HamaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------------------

class SolusiAPI(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Solusi.objects.all()
        serializer = SolusiSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SolusiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SolusiDetailAPI(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Solusi.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SolusiSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SolusiSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------------------

class PermasalahanAPI(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Permasalahan.objects.all()
        serializer = PermasalahanSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PermasalahanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PermasalahanDetailAPI(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Permasalahan.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PermasalahanSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PermasalahanSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -----------------------------------------------------------------------------------------------------------------
def cf_formula(num1, num2):

    result = num1 + num2 * (1-num1)
    return result

# @permission_classes([permissions.IsAuthenticated])
# @authentication_classes([authentication.TokenAuthentication])
@csrf_exempt
@api_view(['GET', ])
def diagnosis(request, id_masalah):
    try:
        
        data_masalah = Permasalahan.objects.get(id=id_masalah)
        data_cf_penggunas = CFPengguna.objects.filter(nama_masalah=data_masalah)
        data_cf_pakars = CFPakar.objects.all()
        data_penyakits = JenisPenyakit.objects.all()

        cf_result = []
        cf_min = -1000000
        penyakit = None 
        for data_penyakit in data_penyakits:
            # print(data_penyakit.kode)
            cfpakars = data_cf_pakars.filter(jenis_penyakit=data_penyakit.id)

            cfs = []
            for cf_pakar in cfpakars:
                cf_pengguna = data_cf_penggunas.get(hama__kode=cf_pakar.hama.kode)
                # print(cf_pakar.hama.kode, cf_pakar.value)
                # print(cf_pengguna.hama.kode, cf_pengguna.value)
                cfs.append(cf_pakar.value * cf_pengguna.value)

            cf_old = cfs[0]
            for x in range(1,len(cfs)):
                cf_old = cf_formula(cf_old, cfs[x])

            if cf_min < cf_old:
                cf_min = cf_old
                penyakit = data_penyakit 
            
            cf_result.append({
                'penyakit'      : data_penyakit.nama,
                'presentase'    : round(cf_old*100,2)
            })

        print(penyakit.nama, round(cf_min*100,2))
        cf_result = list(reversed(sorted(cf_result, key=lambda k: k['presentase'])))
        

        data_masalah.jenis_penyakit.add(penyakit)
        data_masalah.penjelasan = cf_result
        data_masalah.keterangan = 'Sudah dilakukan diagnosis penyakit'
        data_masalah.save()
        status = 200
        response={
            'status'                : status,
            'data'                  : {
                'identifikasi_penyakit' : penyakit.nama,
                'presentase'            : (cf_min*100,2),
                'cf_result'             : cf_result,
            },
            'message'               : 'sukses'
        }
        return Response(response, status)
    except Exception as e:   
        status = 404
        response={
            'status'                : status,
            'data'                  : {},
            'message'               : f'Error, {e}'
        }
        return Response(response, status)
# -----------------------------------------------------------------------------------------------------------------
@csrf_exempt
@api_view(['POST', ])
def input_cf_pengguna(request):
    try:
        id_masalah      = request.POST['id_masalah']
        id_hama         = request.POST['id_hama']
        value           = request.POST['value']



        data_masalah = Permasalahan.objects.get(id=id_masalah)
        data_hama = Hama.objects.get(id=id_hama)

        cf_pengguna = CFPengguna()
        cf_pengguna.nama_masalah    = Permasalahan.objects.get(id=id_masalah)
        cf_pengguna.hama            = Hama.objects.get(id=id_hama)
        cf_pengguna.value           = value
        cf_pengguna.save()

        status = 201
        response={
            'status'                : status,
            'data'                  : {
                'hama'  : cf_pengguna.hama.nama,
                'value' : cf_pengguna.value,
            },
            'message'               : f'sukses'
        }
        return Response(response, status)

    except Exception as e:
        status = 404
        response={
            'status'                : status,
            'data'                  : {},
            'message'               : f'Error, {e}'
        }
        return Response(response, status)