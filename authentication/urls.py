from django.urls import path
from authentication.views import login_user, register, logout, login4flutter, create_news_flutter

app_name = 'authentication'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('login4flutter/', login4flutter, name='loginforflutter'),
    path('create-flutter/', create_news_flutter, name='create_news_flutter'),
]