from django.shortcuts import render, redirect

from app01.models import UserInfo, Department
from app01.utils.form import UserModelForm


def user_lst(request):
    data_lst = UserInfo.objects.all()
    return render(request, 'user_list.html', {'data_lst': data_lst})


def user_add(request):
    if request.method == 'GET':
        param = {
            'gender_choices': UserInfo.gender_choices,
            'depart_choices': Department.objects.all()
        }
        return render(request, 'user_add.html', param)

    # 获取用户提交数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    ac = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender_id = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    # 添加到数据库
    UserInfo.objects.create(name=user, password=pwd,
                            age=age, account=ac,
                            create_time=ctime,
                            gender=gender_id,
                            depart_id=depart_id)
    return redirect('/user/list')


def user_add2(request):
    if request.method == 'GET':
        print(request.method)
        form = UserModelForm()
        return render(request, 'user_add2.html', {'form': form})
    # 用户POST提交数据,数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        print('Success', form.cleaned_data)
        return redirect('/user/list')
    else:
        print('Error', form.errors)
    return render(request, 'user_add2.html', {'form': form})


def user_edit(request, user_id):
    tar_user = UserInfo.objects.filter(id=user_id).first()
    # GET方法
    if request.method == 'GET':
        return render(request, 'user_edit.html', {'form': UserModelForm(instance=tar_user)})
    # POST方法
    form = UserModelForm(data=request.POST, instance=tar_user)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    # 如果有不合法内容仍留在此页面并打印提示信息
    return render(request, 'user_edit.html', {'form': form})


def user_del(request, user_id):
    UserInfo.objects.filter(id=user_id).delete()
    return redirect('/user/list')