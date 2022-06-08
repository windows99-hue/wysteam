from django.shortcuts import render, redirect
from django.http import HttpResponse
from pc_or_mobile import judge_pc_or_mobile
from django.http import HttpResponse
from django.urls import reverse
from . import models
from django import forms
from . import captcha_
from io import BytesIO
import hashlib



def captcha(request):
    pass

def captcha_img(request):
    stream = BytesIO()
    img, code = captcha_.veri_code()
    img.save(stream, 'PNG')
    request.session['check_code'] = code
    return HttpResponse(stream.getvalue())



def index(request):
    # 判断手机还是电脑
    #这步是为了返回浏览器打开网页时候的headers，因为user-agent是存在于headers中的
    total = request.headers
    #ua就是通过字典取值的方式拿到返回的user-agent,最后传递到pc_or_mobile.py中的ua
    ua = total["User-Agent"]
    #调用pc_or_mobile.py文件里面的函数judge_pc_or_mobile开始判断
    #将ua的值传到该函数的参数预留项里
    mobile = judge_pc_or_mobile(ua)
    #输出一下查看状态
    print("判断访问是不是手机：  ", mobile)
    #######################
    #开始判断，如果不是手机访问，返回content_w.html，即电脑页面
    if mobile == False:
        return render(request,'index/index.html')
    #否则，就要返回content.html即手机界面
    else:
        #return HttpResponse("phone")
        return render(request,'index/index-m.html')
    
def login(request):
    # 判断手机还是电脑
    #这步是为了返回浏览器打开网页时候的headers，因为user-agent是存在于headers中的
    total = request.headers
    #ua就是通过字典取值的方式拿到返回的user-agent,最后传递到pc_or_mobile.py中的ua
    ua = total["User-Agent"]
    #调用pc_or_mobile.py文件里面的函数judge_pc_or_mobile开始判断
    #将ua的值传到该函数的参数预留项里
    mobile = judge_pc_or_mobile(ua)
    #输出一下查看状态
    print("判断访问是不是手机：  ", mobile)
    #######################
    #开始判断，如果不是手机访问，返回content_w.html，即电脑页面
    if mobile == False:
        status = request.session.get('is_login')
        if status:
            return redirect(reverse('index:user_view'))
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            check_code = request.POST.get('captcha')
            if check_code and check_code.lower() == request.session.get('check_code').lower():
                pass
            else:
                error_name = '验证码不正确！'
                return render(request,'login/index.html',{'error_msg':error_name})
            print(request.session.get('is_login'))
            obj_user = models.Users.objects.filter(name=username, password=password)
            if obj_user:
                print(obj_user)
                request.session["is_login"] = True
                request.session["user"] = username
                return redirect(reverse('index:user_view'))
            error = '用户名或密码错误'
            return render(request, 'login/index.html', {"error_msg":error})
        return render(request,'login/index.html')
    #否则，就要返回content.html即手机界面
    else:
        #return HttpResponse("phone")
        return render(request,'login/index-m.html')
    
def register(request):
    # 判断手机还是电脑
    #这步是为了返回浏览器打开网页时候的headers，因为user-agent是存在于headers中的
    total = request.headers
    #ua就是通过字典取值的方式拿到返回的user-agent,最后传递到pc_or_mobile.py中的ua
    ua = total["User-Agent"]
    #调用pc_or_mobile.py文件里面的函数judge_pc_or_mobile开始判断
    #将ua的值传到该函数的参数预留项里
    mobile = judge_pc_or_mobile(ua)
    #输出一下查看状态
    print("判断访问是不是手机：  ", mobile)
    #######################
    #开始判断，如果不是手机访问，返回content_w.html，即电脑页面
    if mobile == False:
        if request.method == 'POST':
            check_code = request.POST.get('captcha')
            if check_code and check_code.lower() == request.session.get('check_code').lower():
                pass
            else:
                error_name = '验证码不正确！'
                return render(request,'register/index.html',{'error_name':error_name})
            username = request.POST.get('username')
            password = request.POST.get('password')
            password_a = request.POST.get('password_again')
            user_list = models.Users.objects.filter(name=username)
            error_name = []
            if not username:
                error_name = '用户名不能为空'
                return render(request,'register/index.html',{'error_name':error_name})
            if not password:
                error_name = '密码不能为空'
                return render(request,'register/index.html',{'error_name':error_name})
            if password != password_a:
                error_name = '前后两次密码不同'
                return render(request,'register/index.html',{'error_name':error_name})
            if len(password) < 8:
                error_name = '密码不能小于8位'
                return render(request,'register/index.html',{'error_name':error_name})
            if user_list:
                error_name = '用户名已经存在'
                return render(request,'register/index.html',{'error_name':error_name})
            else:
                password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                username = models.Users.objects.create(name=username,password=password)
                username.save()
                return redirect(reverse('index:login'))
        else:
            return render(request,'register/index.html')
    #否则，就要返回手机界面
    else:
        #return HttpResponse("phone")
        return render(request,'register/index-m.html')
    
def logout(request):
    request.session.flush() # 删除一条记录包括(session_key session_data expire_date)三个字段
    return redirect(reverse("index:login"))

def user_view(request):
    status = request.session.get('is_login')
    if status:
        username = request.session.get('user')
        return render(request, 'user_view/index.html', {"username":username})
    else:
        return HttpResponse('''"<script>alert('会话已过期，请重新登录!');window.location.href="/login/";</script>"''')
        #return redirect('index')
