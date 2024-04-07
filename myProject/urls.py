"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

import app01
from app01 import view
from app01.views import depart, user, pretty, admin, account, task, order, chart, file

urlpatterns = [
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # 主页
    path('', view.index),

    # 部门管理
    path('depart/list', depart.depart_lst),
    path('depart/add', depart.depart_add),
    path('depart/del', depart.depart_del),
    path('depart/<int:depart_id>/edit', depart.depart_edit),
    path('depart/upload', depart.depart_upload),

    # 用户管理
    path('user/list', user.user_lst),
    path('user/add', user.user_add),
    path('user/add2', user.user_add2),
    path('user/<int:user_id>/edit', user.user_edit),
    path('user/<int:user_id>/del', user.user_del),

    # 靓号管理
    path('pretty/list', pretty.pretty_lst),
    path('pretty/add', pretty.pretty_add),
    path('pretty/<int:pretty_id>/del', pretty.pretty_del),
    path('pretty/<int:pretty_id>/edit', pretty.pretty_edit),

    # 管理员管理
    path('admin/list', admin.admin_lst),
    path('admin/add', admin.admin_add),
    path('admin/<int:admin_id>/del', admin.admin_del),
    path('admin/<int:admin_id>/edit', admin.admin_edit),
    path('admin/<int:admin_id>/reset', admin.admin_reset),

    # 账户
    path('account/login', account.login),
    path('account/logout', account.logout),
    path('image/code', account.image_code),

    # 任务管理(ajax)
    path('task/list', task.task_list),
    path('task/add', task.task_add),

    # 订单管理
    path('order/list', order.order_list),
    path('order/add', order.order_add),
    path('order/del', order.order_del),
    path('order/detail', order.order_detail),

    # 数据统计
    path('chart/list', chart.chart_list),
    path('chart/bar', chart.chart_bar),
    path('chart/pie', chart.chart_pie),
    path('chart/highchars', chart.highchars),

    # 文件上传
    path('file/upload', file.upload),
    path('file/form', file.upload_form),
    path('file/model/form', file.upload_model_form),
]
