from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.htm')

def layout(request):
    return render(request,'layout.htm')

def position(request):
    return render(request,'position.htm')

def profile1(request):
    return render(request,'position.htm',{'name':'หลวงพี่เท่ง','number':'IT001','position':'ห้อง 201','image':'1'})

def profile2(request):
    return render(request,'position.htm',{'name':'หลวงพี่แจ๊ส','number':'IT001','position':'ห้อง 301','image':'2'})

def profile3(request):
    return render(request,'position.htm',{'name':'สารชา','number':'60011052','position':'ห้อง 401','image':'3'})

def profile4(request):
    return render(request,'position.htm',{'name':'พิชญุตม์','number':'60010704','position':'ห้อง 501','image':'4'})