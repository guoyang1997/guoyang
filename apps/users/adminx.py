import xadmin

from .models import UserProfile
from xadmin import views

class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    '''
    设置网站标题和页脚
    '''
    site_title = "在线教育平台"
    site_footer = "Powered By 1906C - 2020"
    menu_style = 'accordion'     # 设置菜单折叠
class UserProfileAdmin(object):
    list_display = ["username","gender","mobile","adress"]
    search_fields = ["username","gender","mobile","adress"]
    list_filter = ["username","gender","mobile","adress"]
    model_icon = 'fa fa-user'
    style_fields = {"adress": "ueditor"}
    ordering = ['date_joined']              #排序
    readonly_fields = ['nick_name']   #只读字段
    exclude = ['gender']                     #不显示字段
    list_editable = ['mobile']               # 可编辑自动
    refresh_times = [3,5]                   # 定时刷新

xadmin.site.unregister(UserProfile)
xadmin.site.register(views.BaseAdminView,BaseSettings)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(UserProfile,UserProfileAdmin)

