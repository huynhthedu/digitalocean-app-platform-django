from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
import homepage.views


def home(request):
    return JsonResponse({"hello": "world!"})


urlpatterns = [
    path('', homepage.views.home, name='home'), 
    path("admin/", admin.site.urls),
]
