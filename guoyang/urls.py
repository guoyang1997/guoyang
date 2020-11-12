import xadmin
from django.urls import path,include,re_path
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.views.generic import TemplateView
from apps.users.views import ActiveUserView
from apps.users.views import ModifyPwdView,ResetView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('xadmin/', xadmin.site.urls),
    #文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('user/', include('apps.users.urls')),
    path('org/', include(('apps.organization.urls', 'org'),namespace='org')),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
# 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    path("course/", include(('apps.course.urls','course'), namespace="course")),

]
