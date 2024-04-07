from django.forms import CharField
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from app01.models import Admin
from app01.utils.form import AdminModelForm, AdminResetModelForm


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        info = request.session.get('info')
        if info is None:
            return redirect('/account/login')
        return view_func(request, *args, **kwargs)
    return wrapper


@login_required
def admin_lst(request):
    queryset = Admin.objects.filter()
    from app01.utils.pagination import Pagination
    pagination = Pagination(request, queryset, page_size=15)
    page_html = pagination.html()
    content = {
        'data_lst': pagination.page_queryset,
        'search_word': '',
        'page_li_str': mark_safe(page_html)
    }
    return render(request, 'admin_list.html', content)


def admin_add(request):
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'admin_add.html', {'form': form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'admin_add.html', {'form': form})


def admin_del(request, admin_id):
    Admin.objects.filter(id=admin_id).delete()
    return redirect('/admin/list')


def admin_edit(request, admin_id):
    admin_instance = Admin.objects.filter(id=admin_id).first()
    if request.method == 'GET':
        form = AdminModelForm(instance=admin_instance)
        return render(request, 'admin_edit.html', {'form': form})
    form = AdminModelForm(
        instance=admin_instance,
        data=request.POST
    )
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'admin_edit.html', {'form': form})


def admin_reset(request, admin_id):
    admin_instance = Admin.objects.filter(id=admin_id).first()
    title = f'重置密码 - {admin_instance.username}'
    if request.method == 'GET':
        print(admin_instance.password)
        form = AdminResetModelForm()
        return render(request, 'changes.html', {'form': form, 'title': title})
    form = AdminResetModelForm(
        instance=admin_instance,
        data=request.POST
    )
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/admin/list')
    return render(request, 'changes.html', {'form': form, 'title': title})
