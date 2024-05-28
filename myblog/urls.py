from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path("",views.home, name='home'),
    path("send-news",views.createnews, name='createnews'),
    path("send-feedback",views.sendfeedback, name='sendfb'),
    path("complete",views.complete, name='complete'),
    path("technology-news",views.tech_news, name='technews'),
    path("finance-news",views.finance_news, name='financenews'),
    path('news/<int:id>/', views.news_detail, name='newsdetail'),
    ]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)