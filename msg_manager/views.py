from django.shortcuts import render
from django.http.response import HttpResponse
from msg_manager.models import Message
from django.views import View
from msg_manager.forms import MsgForm

# Create your views here.
class SendMessage(View):
    def get(self, request):
        form = MsgForm()
        return render(request,'home.html', {'form':form})

    def post(self, request):
        name =request.POST['name']
        msg = request.POST['msg']
        obj = Message.objects.create(msg=msg)
        print((obj.msg))
        return render(request,'response.html',{'name':name})
       

def view_msg(request):
    if(request.method=='GET'):
        viewm = Message.objects.all()
        return render(request,'view_msgs.html',{'viewm':viewm})