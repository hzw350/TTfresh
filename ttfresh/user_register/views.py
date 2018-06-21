# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from hashlib import sha1
from user_register.models import *
from user_register import user_decorator


def register(request):
    context = {'title':  '天天生鲜-注册'}
    return render(request, 'user_register/register.html', context)


def register_exist(request):
    print "123"
    uname = request.GET.get('userName')
    print request
    print uname
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':  count})


def register_handle(request):
    # 接收用户注册信息
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    cpwd = post.get('cpwd')
    uemail = post.get('email')

    if upwd != cpwd:
        # 重定向到登陆页面
        return redirect('/user/register')

    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd2 = s1.hexdigest()
    # 保存进数据库
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd2
    user.uemail = uemail
    user.save()
    return redirect('/user/login')


def login(request):
    uname = request.COOKIES.get('username','')
    context = {'title': '用户登陆',  'error_name': 0,  'error_pwd': 0, 'uname': uname}
    return render (request, 'user_register/login.html', context)


def login_handle(request):
    # 接收login页面的post请求
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    # 根据用户名查询客户是否存在
    user = UserInfo.objects.filter(uname=uname)

    # 判断：若用户存在且身份信息正确，跳转到用户中心，若不正确，跳转回登陆界面
    if len(user) == 1:
        s1 = sha1()
        s1.update(upwd)
        upwd2 = s1.hexdigest()
        # 比对密码
        if upwd2 == user[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            # 记住用户名
            if jizhu == 1:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname','',max_age = -1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = user[0].uname
            return red
        # 密码错误
        else:
            context = {'title': '用户登录', 'error_name':0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request,'user_register/login.html', context)
    # 账号错误
    else:
        context = {'title': '用户登陆', 'error_name':1, 'error_pwd':0, 'uname': uname, 'upwd': upwd}
        return render(request,'user_register/login.html', context)


def logout(request):
    request.session.flush()
    return render(request,'user_register/user_center_info.html')


@user_decorator.login
def info(request):
    uemail = UserInfo.objects.get(id=request.session['user_id']).uemail
    uphone = UserInfo.objects.get(id=request.session['user_id']).uphone
    uaddress = UserInfo.objects.get(id=request.session['user_id']).uaddress
    if uphone == '':
        uphone = '未填写'
    if uaddress == '':
        uaddress = '未填写'
    context = {
        'title': '天天生鲜用户中心',
        'user_name': request.session['user_name'],
        'uemail': uemail,
        'uphone': uphone,
        'uaddress': uaddress,
    }
    return render(request,'user_register/user_center_info.html',context)


@user_decorator.login
def user_order(request):
    return render(request,'user_register/user_center_order.html')


@user_decorator.login
def user_site(request):
    rsite = ReceiverInfo.objects.filter(ruser=request.session['user_id'])
    if rsite.count() == 0:
        context = {
            'title': '天天生鲜用户中心',
            'raddress': '',
            'rname': '',
            'rphone': ''
        }
    else:
        raddress = rsite[0].raddress
        rname = rsite[0].rname
        rphone = rsite[0].rphone
        context = {
            'title': '天天生鲜用户中心',
            'raddress': raddress,
            'rname': rname,
            'rphone': rphone
        }
    return render(request,'user_register/user_center_site.html',context)


def user_site_handle(request):
    # 接收Post传来的用户收货地址信息
    post = request.POST
    rname = post.get('rname')
    raddress = post.get('raddress')
    rcode = post.get('rcode')
    rphone = post.get('rphone')
    # 根据session查找user信息
    user = UserInfo.objects.get(id=request.session['user_id'])
    if user.receiverinfo_set.all().count() == 0:
        # 将信息存入数据库
        rsite = ReceiverInfo()
        rsite.rname = rname
        rsite.raddress = raddress
        rsite.rcode = rcode
        rsite.rphone = rphone
        rsite.ruser = user
        rsite.save()
    else:
        rsite = ReceiverInfo.objects.filter(ruser=user.id)
        rsite.rname = rname
        rsite.raddress = raddress
        rsite.rcode = rcode
        rsite.rphone = rphone
        rsite.ruser = user
    rphone = rphone[0:3] + '****' + rphone[-4:]
    context = {
        'title': '天天生鲜用户中心',
        'raddress': raddress,
        'rname': rname,
        'rphone': rphone
    }
    return render(request, 'user_register/user_center_site.html', context)


