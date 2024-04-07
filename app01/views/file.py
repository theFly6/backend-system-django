from django import forms
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.core.management.commands.runserver import Command as Runserver
from app01.models import Boss, City
from app01.utils.form import BootStrapForm, BootStrapModelForm


def upload(request):
    if request.method == "GET":
        return render(request, 'file_upload.html')
    print(request.POST)
    print(request.FILES)
    file = request.FILES.get('my_file')
    print(file)
    print(file.name)
    print(type(file))
    with open(f'app01/download/{file.name}', 'wb')as f:
        for chunk in file.chunks():
            f.write(chunk)
    return HttpResponse('Success')


class UpForm(BootStrapForm):
    execlude_field = ['img']
    name = forms.CharField(label='姓名')
    age = forms.IntegerField(label='年龄')
    img = forms.FileField(label='头像')


# class UpForm(forms.Form):
#     name = forms.CharField(
#         label='姓名',
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     age = forms.IntegerField(
#         label='年龄',
#         widget=forms.NumberInput(attrs={'class': 'form-control'})
#     )
#     img = forms.FileField(
#         label='头像',
#         widget=forms.FileInput
#     )


def upload_form(request):
    bosses = list(Boss.objects.all().values())
    label_lst = [] if len(bosses)==0 else bosses[0].keys()
    content = {
        'title': 'Form上传',
        'form': UpForm(),
        'data_lst': Boss.objects.all(),
        'label_lst': label_lst,
        'lst_name': 'Boss'
    }
    if request.method == 'GET':
        return render(request, 'upload_form.html', content)
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        img_file = form.cleaned_data.get('img')
        # print(form.cleaned_data)
        # db_path = f'{Runserver.default_addr}:{Runserver.default_port}/static/img/{img_file.name}'
        # db_path = f'{settings.MEDIA_ROOT}/{img_file.name}'
        with open(f'media/{img_file.name}', 'wb')as f:
            for chunk in img_file.chunks():
                f.write(chunk)

        Boss.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
            img=img_file.name,
        )
    content['form'] = UpForm()
    return render(request, 'upload_form.html', content)


class UpModelform(BootStrapModelForm):
    execlude_field = ['img']

    class Meta:
        model = City
        fields = '__all__'


def upload_model_form(request):
    label_lst = list(City.objects.all().values())[0].keys()
    content = {
        'title': 'ModelForm上传',
        'form': UpModelform(),
        'data_lst': City.objects.all(),
        'label_lst': label_lst,
        'lst_name': 'City'
    }
    print(label_lst)
    if request.method == 'GET':
        return render(request, 'upload_form.html', content)
    form = UpModelform(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
    content['form'] = form
    return render(request, 'upload_form.html', content)
