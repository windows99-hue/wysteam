from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
               path("", views.index, name="index"),
               path("register/", views.register, name="register"),
               path("captcha/", views.captcha, name="captcha"),
               path('captcha_img/', views.captcha_img, name='captcha_img'),
               path("login/", views.login, name="login")]