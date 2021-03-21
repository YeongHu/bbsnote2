from django.contrib.auth import views as auth_views
from django.urls import path
from . import views # views모델에 있는 모든 것을 참조하겠다.

app_name = 'common'

urlpatterns = [
    #장고의 로그인 기능을 그대로 사용
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]