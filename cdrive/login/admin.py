from django.contrib import admin

# Register your models here.
from .models import user,Bookmark,marker

class userAdmin(admin.ModelAdmin):
    # 내가 출력하고 싶은 제목명인 필드명 member_id과 name 을 표시한다.
    list_display = ('user_id', 'name','email','mbti')
admin.site.register(user, userAdmin)

class bookmarkAdmin(admin.ModelAdmin):
    # 내가 출력하고 싶은 제목명인 필드명 member_id과 name 을 표시한다.
    list_display = ('user_id', 'place','rating','stamp')

admin.site.register(Bookmark, bookmarkAdmin)

class markerAdmin(admin.ModelAdmin):
    # 내가 출력하고 싶은 제목명인 필드명 member_id과 name 을 표시한다.
    list_display = ('place', 'parking','address','rating','lat','lng')

admin.site.register(marker, markerAdmin)