# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-5 22:40                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : urls.py                                                           =
#    @Program: website5                                                        =
# ==============================================================================

import djoser.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from rest_framework_nested import routers

import Blossom.views.class_
import Blossom.views.person
import account.views
import appstore.views

router = routers.DefaultRouter()
router.register(r'users', account.views.UserViewSet)
router.register(r'app', appstore.views.AppViewSet)
router.register(r'blossom/person', Blossom.views.person.PersonViewSet)
router.register(r'blossom/class', Blossom.views.class_.ClassViewSet)
router.register(r'blossom/class_membership', Blossom.views.class_.ClassMembershipViewSet)

class_router = routers.NestedDefaultRouter(router, r'blossom/class', lookup="class")
class_router.register(r"member", Blossom.views.class_.ClassMemberViewSet, basename="class-member")

urlpatterns = [  # 管理员系统
    # re_path(r'^admin/', admin.site.urls), # 自己搭一个，这个不用了
]
urlpatterns += [
    re_path(rf"^{settings.BASE_URL}token/login/?$", djoser.views.TokenCreateView.as_view(), name="login"),
    re_path(rf"^{settings.BASE_URL}token/logout/?$", account.views.TokenDestroyView.as_view(), name="logout"),
]
urlpatterns += [  # api
    path(settings.BASE_URL, include(router.urls)),
    path(settings.BASE_URL, include(class_router.urls)),
]

# 媒体静态文件 设计成由django处理但是不由django路由
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
