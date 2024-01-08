import csv
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from .models import tour,restaurant
from rest_framework import viewsets
from django.http import HttpRequest
import json
from .serializers import tourSerializer,restaurantSerializer
request = HttpRequest()
request.method = 'POST'
request.content_type = 'application/json'
# Create your views here.
@csrf_exempt
def tourfind(request):
    if request.method == 'POST':
        # JSON 데이터를 가져옴
        json_data = request.body.decode('utf-8')

        try:
            # JSON 데이터를 파싱하여 필요한 처리 수행
            data = json.loads(json_data)
            name=data['place']
            tours = tour.objects.get(place=name)

            place=tours.place
            parking=tours.parking
            parking_lot=tours.parking_lot
            rating=tours.rating

            # 처리 결과를 JSON 응답으로 반환
            response_data = {
                'message': 'POST 요청이 성공적으로 처리되었습니다.',
                '장소': place,
                '주차장유무' : parking,
                '주차장위치': parking_lot,
                '평점': rating
            }
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            # JSON 데이터 파싱에 실패한 경우
            response_data = {
                'message': '잘못된 JSON 형식입니다.',
            }
            return JsonResponse(response_data, status=400)
    else:
        # POST 요청이 아닌 경우
        response_data = {
            'message': 'POST 요청이 아닙니다.',
        }
        return JsonResponse(response_data, status=405)
@csrf_exempt
def restaurantfind(request):
    if request.method == 'POST':
        # JSON 데이터를 가져옴
        json_data = request.body.decode('utf-8')

        try:
            # JSON 데이터를 파싱하여 필요한 처리 수행
            data = json.loads(json_data)
            name=data['place']
            restaurants = restaurant.objects.get(place=name)

            place=restaurants.place
            parking=restaurants.parking
            parking_lot=restaurants.parking_lot
            rating=restaurants.rating

            # 처리 결과를 JSON 응답으로 반환
            response_data = {
                'message': 'POST 요청이 성공적으로 처리되었습니다.',
                '장소': place,
                '주차장유무' : parking,
                '주차장위치': parking_lot,
                '평점': rating
            }
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            # JSON 데이터 파싱에 실패한 경우
            response_data = {
                'message': '잘못된 JSON 형식입니다.',
            }
            return JsonResponse(response_data, status=400)
    else:
        # POST 요청이 아닌 경우
        response_data = {
            'message': 'POST 요청이 아닙니다.',
        }
        return JsonResponse(response_data, status=405)

def tourinput(request):
    if request.method == "GET":

        f = open('C:/Users/37593/cdrive/place/관광.csv', 'r',encoding='euc-kr')
        rdr = csv.reader(f)
        next(rdr)
        for line in rdr:

            tour.objects.create(

                place=str(line[0]), parking=str(line[1]), parking_lot=str(line[2]), rating=str(line[3]))

        f.close()

    return render(request, 'place/index.html')

def restaurantinput(request):
    if request.method == "GET":

        f = open('C:/Users/37593/cdrive/place/맛집1.csv', 'r',encoding='euc-kr')
        rdr = csv.reader(f)
        next(rdr)
        for line in rdr:

            restaurant.objects.create(

                place=str(line[0]), parking=str(line[1]), parking_lot=str(line[2]), rating=str(line[3]))

        f.close()

    return render(request, 'place/index.html')

class tourViewset(viewsets.ModelViewSet):
    queryset = tour.objects.all()
    serializer_class = tourSerializer
    data=serializer_class.data

class restaurantViewset(viewsets.ModelViewSet):
    queryset = restaurant.objects.all()
    serializer_class = restaurantSerializer
    data=serializer_class.data