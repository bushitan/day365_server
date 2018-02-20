# -*- coding: utf-8 -*-


from django.conf.urls import url
from lite.views import *



urlpatterns = [

    #365天初始化
    url(r'^day/index/$', DayIndex.as_view()),

    #我的初始化
    url(r'^my/index/$', MyIndex.as_view()),
    url(r'^my/set/clock/$', MySetClock.as_view()),
    url(r'^my/set/logo/$', MySetLogo.as_view()),

    #上传文件
    url(r'^upload/get/token/$', UploadGetToken.as_view()),
    url(r'^upload/callback/$', UploadCallback.as_view()),

    #用户登录
    url(r'^user/login/$', UserLogin.as_view()),
]