from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01.models import Task
from app01.utils.form import TaskForm


def task_list(request):
    data_lst = Task.objects.all()
    form = TaskForm()
    return render(request, 'task_list.html', {'form': form, 'data_lst': data_lst})


@csrf_exempt
def task_add(request):
    form = TaskForm(data=request.POST)
    data_dict = {'status': True}
    if form.is_valid():
        form.save()
    else:
        data_dict['errors'] = form.errors
        data_dict['status'] = False
    print(request.POST)
    return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})
