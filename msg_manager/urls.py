
from django.urls import include,path
from .views import send_msg

urlpatterns = [
    path('', send_msg)
]