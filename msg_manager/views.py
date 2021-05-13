from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def send_msg(request):
    if('message' in request.POST):
        name =request.POST['name']
        return render(request,'response.html',{'name':name})
    else:
        return render(request,'home.html')