from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import usersSerializers
from .models import users
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token



# Create your views here.
#@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def landing_page(request):

    if request.method == 'GET':
        user=users.objects.all()
        serializer=usersSerializers(user,many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method == 'POST':     
        #data=JSONParser().parse(request)
        # token = Token.objects.create(user=request.data['username'])
        # print(token.key)
        serializer=usersSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    if request.method == 'PUT':     
        #data=JSONParser().parse(request)
        user=users.objects.get(username=request.data['username'])
        serializer=usersSerializers(user,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors,status=400)        
   


