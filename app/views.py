from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def htmlforms(request):
    if request.method=='POST':
        n=request.POST['un']
        p=request.POST['pw']
        d={'n':n,'p':p}
        return render(request,'data.html',d)
    return render(request,'htmlforms.html')

def insert_topic(request):
    if request.method=='POST':  
        tn=request.POST['tn']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is inserted successfully go and check in admin if u want')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        tn=request.POST.get('topic')
        n=request.POST.get('name')
        u=request.POST.get('url')
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=n,url=u)[0]
        W.save()
        return HttpResponse('Webpage is inserted successfully')
    return render(request,'insert_webpage.html',d)

def select_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=Webpage.objects.none()
        for i in tn:
            webpages=webpages | Webpage.objects.filter(topic_name=i)
        d1={'webpages':webpages}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_topic.html',d)
























    