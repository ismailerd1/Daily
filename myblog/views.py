from django.http.response import HttpResponse
from django.shortcuts import render ,redirect, get_object_or_404
from .models import News, Topic, Feedbacks


# Create your views here.

def home(request):
    all_topic = Topic.objects.all()
    all_news_order = News.objects.filter(topics__in=all_topic, is_active=True).distinct() 
    all_news_order = reversed(all_news_order)

    context={
        'sub_news' : all_news_order
    }
    return render(request,"blog/homepage.html", context)

def createnews (request):

    if request.method == 'POST':
        sender = request.POST.get('sender')
        source = request.POST.get('source')
        title = request.POST.get('title')
        content = request.POST.get('content')

        news = News(
        sender=sender,
        source=source,
        title=title,
        content=content,
        is_active=False
        )
        if 'image' in request.FILES:
            news.image = request.FILES['image']

        topics = request.POST.getlist('topics')

        news.save()

        for topic_name in topics:
            topic = Topic.objects.get(name=topic_name)
            news.topics.add(topic)


        return render(request,"blog/complete.html", {"message":"Your news was created, will be shared after approval."})

    return render(request,"blog/createnews.html")


def sendfeedback(request):

    if request.method == 'POST':
        sender = request.POST.get('sender')
        title = request.POST.get('title')
        content = request.POST.get('content')

        feedback = Feedbacks(
        sender=sender,
        title=title,
        content=content,
        )
        feedback.save()
        return render(request,"blog/complete.html",{"message":"Thank you for your feedback"})

    return render(request,"blog/sendfb.html")

def complete(request):
    return render(request,"blog/complete.html")


def tech_news(request):
    tech_topic = Topic.objects.get(name='Technology')
    tech_news_order = News.objects.filter(topics=tech_topic, is_active=True)
    tech_news_order = reversed(tech_news_order)

    context={
        'sub_news' : tech_news_order
    }
    return render(request,"blog/tech_news.html",context)

def finance_news(request):
    finance_topic = Topic.objects.get(name='Finance')
    finance_news_order = News.objects.filter(topics=finance_topic, is_active=True)
    finance_news_order = reversed(finance_news_order)

    context={
    'sub_news' : finance_news_order
    }

    return render(request,"blog/finance_news.html",context)


def news_detail(request,id):
    news = get_object_or_404(News, pk=id)

    return render(request, 'blog/news_detail.html', {'news': news})