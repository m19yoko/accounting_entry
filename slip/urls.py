from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# URLパターンを逆引きできるよう名前をつける
app_name = 'slip'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
