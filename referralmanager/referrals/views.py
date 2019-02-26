from django.shortcuts import render
from django.http import HttpResponse
from .models import Referral
from .serializers import ReferralSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def index(request):
    return HttpResponse("Landing page placeholder")

@api_view(['GET','PUT','DELETE'])
def get_delete_update_referral(request, pk):
	try:
		referral = Referral.objects.get(pk=pk)
	except Referral.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	# get single referral
	if request.method == 'GET':
		serializer = ReferralSerializer(referral)
		return Response(serializer.data)
	# update referral
	elif request.method == 'PUT':
		serializer = ReferralSerializer(referral, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	# delete referral
	elif request.method == 'DELETE':
		referral.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def get_post_referrals(request):
	# get all referrals
	if request.method == 'GET':
		referrals = Referral.objects.all()
		serializer = ReferralSerializer(referrals, many=True)
		return Response(serializer.data)
	# create new referral
	elif request.method == 'POST':
		data = {
			'title': request.data.get('title'),
			'clicks': 0 if request.data.get('clicks') is None else request.data.get('clicks')
		}
		serializer = ReferralSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def increment_referral_click(request, pk):
	# increment referral clicks
	try:
		referral = Referral.objects.get(pk=pk)
	except Referral.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	
	referral.clicks += 1
	referral.save()
	return Response(status=status.HTTP_204_NO_CONTENT)
