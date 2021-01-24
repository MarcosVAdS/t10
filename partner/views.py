from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from partner.serializers import PartnerSerializer
from rest_framework import viewsets, permissions
from .models import Partner

# Create your views here.
@csrf_exempt
def listPartners(request):
    if request.method == 'GET':
        partners = Partner.objects.all()
        serializer = PartnerSerializer(partners, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer = PartnerSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def detailedPartner(request, id):
    try: 
        partner = Partner.objects.get(pk=id)
    except Partner.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer =  PartnerSerializer(partner)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        request_data = JSONParser().parse(request)
        serializer = PartnerSerializer(partner, data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        partner.delete()
        return HttpResponse(status=204)


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]

