from django.contrib import admin

# Register your models here.
from .models import tour,restaurant

class tourAdmin(admin.ModelAdmin):
    # 내가 출력하고 싶은 제목명인 필드명 member_id과 name 을 표시한다.
    list_display = ('place','parking','parking_lot','rating')

admin.site.register(tour, tourAdmin)

class restaurantAdmin(admin.ModelAdmin):
    # 내가 출력하고 싶은 제목명인 필드명 member_id과 name 을 표시한다.
    list_display = ('place','parking','parking_lot','rating')

admin.site.register(restaurant, restaurantAdmin)