from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from app01.models import PrettyNumber
from app01.utils.form import PrettyModel, PrettyEditModel


def pretty_lst(request):
    params = request.GET.copy()  # 复制原有的所有参数
    params.update({'param_new': 'value_new'})  # 添加新的参数
    print(params.urlencode())
    search_word = request.GET.get('q', '')
    param_dict = {} if search_word == '' else {'mobile__contains': search_word}
    queryset = PrettyNumber.objects.filter(**param_dict).order_by('-level')

    from app01.utils.pagination import Pagination
    pagination = Pagination(request, queryset, page_size=15)
    page_html = pagination.html()
    content = {
        'data_lst': pagination.page_queryset,
        'search_word': search_word,
        'page_li_str': mark_safe(page_html)
    }
    return render(request, 'pretty_list.html', content)


def pretty_add(request):
    if request.method == 'GET':
        print(request.method)
        form = PrettyModel()
        return render(request, 'pretty_add.html', {'form': form})
    form = PrettyModel(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list')
    print('error', form.errors)
    return render(request, 'pretty_add.html', {'form': form})


def pretty_del(request, pretty_id):
    PrettyNumber.objects.filter(id=pretty_id).delete()
    return redirect('/pretty/list')


def pretty_edit(request, pretty_id):
    print(PrettyNumber.objects.filter())
    print(PrettyNumber.objects.all())

    instance = PrettyNumber.objects.filter(id=pretty_id).first()
    if request.method == 'GET':
        form = PrettyEditModel(instance=instance)
        return render(request, 'pretty_edit.html', {'form': form})
    form = PrettyEditModel(data=request.POST, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list')
    return render(request, 'pretty_edit.html', {'form': form})
