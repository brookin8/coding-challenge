from django.shortcuts import render
from django.http import HttpResponse
from .models import Referral
from .serializers import ReferralSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def index(request):
    return HttpResponse("Landing page")

@api_view(['GET','DELETE','PUT'])
def get_delete_update_referral(request, pk):
	try:
		referral = Referral.objects.get(pk=pk)
	except Referral.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		return Response({})
	elif request.method == 'DELETE':
		return Response({})
	elif request.method == 'PUT':
		return Response({})

@api_view(['GET', 'POST'])
def get_post_referrals(request):
	if request.method == 'GET':
		return Response({})
	elif request.method == 'POST':
		return Response({})
