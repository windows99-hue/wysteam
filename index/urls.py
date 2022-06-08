from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
               path("", views.index, name="index"),
               path("register", views.register, name="register"),
               path("register/", views.register, name="register"),
               path("captcha", views.captcha, name="captcha"),
               path('captcha_img/', views.captcha_img, name='captcha_img'),
               path("user_view",views.user_view,name="user_view"),
               path("user_view/",views.user_view,name="user_view"),
               path("login", views.login, name="login"),
               path("login/", views.login, name="login"),
               path("logout",views.logout,name="logout"),
               path("logout/",views.logout,name="logout")]