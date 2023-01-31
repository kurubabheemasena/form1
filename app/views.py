from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('topic details is done')

    return render(request,'topic.html')

def webpage(request):
    topics=Topic.objects.all()
    d={'topic':topics}
    if request.method=="POST":
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()

        return HttpResponse('webpage details is done')

    return render(request,'webpage.html',d)

def access(request):
    topics=Topic.objects.all()
    web=Webpage.objects.all()
    d={'web':web,'topic':topics}

    if request.method=="POST":
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        date=request.POST['date']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        A=Accessrecords.objects.get_or_create(name=W,date=date)[0]
        A.save()

        return HttpResponse('access is done')
    return render(request,'access.html',d)
