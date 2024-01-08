from django.shortcuts import render
from rest_framework import viewsets
from .models import user,Bookmark,marker
from .serializers import userSerializer, BookmarkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
import csv
def index(request):
    context={}

    return render(request,'login/index.html',context)

class userViewset(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer
    data=serializer_class.data

class bookmarkViewset(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = BookmarkSerializer
    data=serializer_class.data

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # JSON 데이터를 가져옴
        json_data = request.body.decode('utf-8')

        try:
            # JSON 데이터를 파싱하여 필요한 처리 수행
            data = json.loads(json_data)
            id=data['id']
            passwd=data['password']
            users = user.objects.get(user_id=id)

            name = users.name
            email = users.email
            mbti = users.mbti
            if passwd==users.passwd:
                response_data = {
                    'message': '로그인 성공',
                    'success': '1',
                    'id': id,
                    'passwd': passwd,
                    'name': name,
                    'email': email,
                    'mbti': mbti
                }


            # 처리 결과를 JSON 응답으로 반환

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
def register(request):
    if request.method == 'POST':
        # JSON 데이터를 가져옴
        json_data = request.body.decode('utf-8')

        try:
            # JSON 데이터를 파싱하여 필요한 처리 수행
            data = json.loads(json_data)
            id=data['user_id']
            passwd=data['passwd']
            name=data['name']
            email=data['email']
            mbti=data['mbti']

            rs = user.objects.filter(user_id=id)
            if rs.exists():
                response_data={
                    'message': '아이디가 중복됩니다',
                    'sucess' : '0'
                }
            else:
                user.objects.create(
                    user_id=id,passwd=passwd,name=name,email=email,mbti=mbti
                )
                response_data = {
                    'message': '회원가입 완료',
                    'success': '1'

                }

            # 처리 결과를 JSON 응답으로 반환

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
def update(request):
    if request.method == 'POST':
        # JSON 데이터를 가져옴
        json_data = request.body.decode('utf-8')

        try:
            # JSON 데이터를 파싱하여 필요한 처리 수행
            data = json.loads(json_data)
            id=data['user_id']
            bpasswd=data['bpasswd']
            passwd=data['passwd']
            name=data['name']
            email=data['email']
            mbti=data['mbti']

            rs = user.objects.get(user_id=id)
            if (rs.passwd==bpasswd):
                rs.name = name
                rs.email = email
                rs.passwd = passwd
                rs.mbti = mbti
                rs.save()
                response_data = {
                    'message': '수정완료',
                    'sucess': '1'
                }





            # 처리 결과를 JSON 응답으로 반환

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
def bookmark(request):
    if request.method == 'POST':
        # JSON 데이터를 가져옴
        json_data = request.body.decode('utf-8')

        try:
            # JSON 데이터를 파싱하여 필요한 처리 수행
            data = json.loads(json_data)
            id=data['user_id']

            bl=Bookmark.objects.filter(user_id=id)
            bookmark_list=[]

            for i in bl:
                bookmark_data={
                    'place': i.place,
                    'rating': i.rating,
                    'stamp': i.stamp,
                }
                bookmark_list.append(bookmark_data)

            response_data = {
                'message': '북마크 리스트',
                'sucess': '0',
                'data' : bookmark_list

            }


            # 처리 결과를 JSON 응답으로 반환

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
def addbookmark(request):
    if request.method == 'POST':
        # JSON 데이터를 가져옴
        json_data = request.body.decode('utf-8')

        try:
            # JSON 데이터를 파싱하여 필요한 처리 수행
            data = json.loads(json_data)
            id=data['id']
            place=data['place']
            rating=data['rating']
            stamp=data['stamp']

            rs = Bookmark.objects.filter(user_id=id, place=place)
            if stamp=="0":
                response_data = {
                    'message': '도장을 찍지 않았습니다.',
                    'sucess': '0'
                }
            elif rs.exists():
                response_data = {
                    'message': '중복된 북마크',
                    'sucess': '0'
                }
            else:
                Bookmark.objects.create(
                    user_id=id, place=place, rating=rating, stamp=stamp
                )
                response_data = {
                    'message': '북마크 등록 완료',
                    'success': '1'

                }


            # 처리 결과를 JSON 응답으로 반환

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


def markerinput(request):
    if request.method == "GET":

        f = open('C:/Users/37593/cdrive/login/spot.csv', 'r',encoding='euc-kr')
        rdr = csv.reader(f)
        next(rdr)
        for line in rdr:

            marker.objects.create(

                place=str(line[0]), parking=str(line[1]), address=str(line[2]), rating=str(line[3]),lat=str(line[4]),lng=str(line[5]))

        f.close()

    return render(request, 'login/index.html')


@csrf_exempt
def getmarker(request):
    if request.method == 'GET':
        # JSON 데이터를 가져옴
        json_data = request.body.decode('utf-8')

        try:
            # JSON 데이터를 파싱하여 필요한 처리 수행

            mk=marker.objects.all()
            marker_list=[]

            for i in mk:
                bookmark_data={
                    'place': i.place,
                    'parking': i.parking,
                    'address': i.address,
                    'rating' : float(i.rating),
                    'lat': float(i.lat),
                    'lng': float(i.lng),
                }
                marker_list.append(bookmark_data)

            response_data = {
                'message': '북마크 리스트',
                'success': '0',
                'data' : marker_list

            }


            # 처리 결과를 JSON 응답으로 반환

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