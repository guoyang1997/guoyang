from django.shortcuts import render,redirect,reverse,HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm,LoginForm,ForgetPwdForm,ModifyPwdForm
from apps.utils.email_send import send_register_eamil
from apps.users.models import UserProfile,EmailVerifyRecord
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login


def index(request):
    sess = request.user

    return render(request, 'index.html', {'user':sess})


def user_login(request):
    if request.method == 'POST':
        # 获取用户提交的用户名和密码
        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)
        # 成功返回user对象,失败None
        user = authenticate(username=user_name, password=pass_word)
        print(user)
        # 如果不是null说明验证成功
        if user is not None:
            # 登录
            login(request, user)

            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})

    elif request.method == 'GET':
        return render(request, 'login.html')


def my_outlogin(request):
    logout(request)
    return redirect(reverse('index'))

class RegisterView(View):
    '''用户注册'''
    def get(self,request):
        register_form = RegisterForm()

        return render(request,'register.html',{'register_form':register_form})

    def post(self,request):
        print(1)
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print(2)
            user_name = request.POST.get('email')
            # 如果用户已存在，则提示错误信息
            capt_cha = request.POST.get('captcha')
            if UserProfile.objects.filter(email = user_name):

                return render(request, 'register.html', {'register_form':register_form,'msg': '用户已存在'})
            print(3)
            pass_word = request.POST.get('password')
            # 实例化一个user_profile对象
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            # 对保存到数据库的密码加密
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_eamil(user_name,'register')
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form,'msg': '验证码错误'})

# 激活用户

class ActiveUserView(View):
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code = active_code)

        if all_record:
            for record in all_record:
                # 获取到对应的邮箱
                email = record.email
                # 查找到邮箱对应的user
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
         # 验证码不对的时候跳转到激活失败页面
        else:
            return render(request,'active_fail.html')
        # 激活成功跳转到登录页面
        messages.success(request, "激活成功！")
        return render(request, "login.html")
        # return HttpResponse('<script>alert("激活成功,请前往登录");window.location="http://127.0.0.1:8000/active/{0}".format(code))<script>')

class ForgetPwdView(View):
    '''找回密码'''
    def get(self,request):
        forget_form = ForgetPwdForm()
        return render(request,'forgetpwd.html',{'forget_form':forget_form})

    def post(self,request):

        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            print(222)
            email = request.POST.get('email',None)
            send_register_eamil(email,'forget')
            return render(request, 'send_success.html')
        else:
            return render(request,'forgetpwd.html',{'forget_form':forget_form})

class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        print(all_records)
        if all_records:
            for record in all_records:
                email = record.email
                print(email)
                return render(request, "password_reset.html", {"email":email})
        else:
            return render(request, "active_fail.html")
        messages.success(request, "修改成功！")
        return render(request, "login.html")

class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email":email, "msg":"密码不一致！"})
            user = UserProfile.objects.filter(email=email).first()
            print(user)
            user.password = make_password(pwd2)
            user.save()
            return redirect(reverse('login'))
        else:

            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email":email, "modify_form":modify_form })










