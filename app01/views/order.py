import random
from datetime import datetime

from django.forms import CharField, TextInput
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01.models import Order, Admin
from app01.utils.form import BootStrapModelForm


class OrderForm(BootStrapModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        exclude = ['oid', 'admin']


def order_list(request):
    data_lst = Order.objects.all()
    form = OrderForm()
    return render(request, 'order_list.html', {'form': form, 'data_lst': data_lst})


@csrf_exempt
def order_add(request):
    if request.POST.get('type') == '新建':
        form = OrderForm(data=request.POST)
    # elif request.POST.get('type') == '编辑':
    else:
        uid = request.POST.get('uid')
        instance = Order.objects.filter(id=uid).first()
        form = OrderForm(data=request.POST, instance=instance)
    data_dict = {
        'status': True
    }
    if form.is_valid():
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(0, 10000))
        u_id = request.session['info']['id']
        form.instance.admin_id = u_id
        form.save()
        return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})
    data_dict['status'] = False
    data_dict['errors'] = form.errors
    return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def order_del(request):
    u_id = request.POST.get('u_id')
    Order.objects.filter(id=u_id)[0].delete()
    print(u_id)
    data_dict = {
        'status': True
    }
    return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})


def order_detail(request):
    uid = request.GET.get('uid')
    order = Order.objects.filter(id=uid).first()
    # order_dict = Order.objects.filter(id=uid).values('title', 'price').first()
    data_dict = {
        'status': True,
        'order': {
            'title': order.title,
            'price': order.price,
            'status': order.status,
        }
    }
    return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})
