from django.urls import path,include
from apps.users import views


urlpatterns = [

    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/', views.user_login,name='login'),
    path('forget/', views.ForgetPwdView.as_view(),name = 'forget_pwd'),
    path('modify_pwd/', views.ModifyPwdView.as_view(), name='modify_pwd'),
    path('out_login/', views.my_outlogin, name='outlogin'),
]

