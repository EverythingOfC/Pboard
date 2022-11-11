from django.urls import path
from django.contrib.auth import views as auth_views # 로그인,로그아웃 앱 사용
from . import views

app_name = 'common'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
                # django.contrib.auth앱의 LoginView를 사용하도록 지정

    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
                # django.contrib.auth앱의 LogoutView를 사용하도록 지정
    path('signup/',views.signup,name='signup'),
                # 현재 경로의 views파일의 signup함수 호출
]
