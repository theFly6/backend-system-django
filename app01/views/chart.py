from django.http import JsonResponse
from django.shortcuts import render


def chart_list(request):
    return render(request, 'chart_list.html')


def chart_bar(request):
    series = [
        {
            'name': '销量',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
        },
        {
            'name': '收入',
            'type': 'bar',
            'data': [15, 30, 26, 20, 16, 30]
        }
    ]
    data = {
        'status': True,
        'series': series
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def chart_pie(request):
    series = [
        {'value': 1048, 'name': 'IT部门'},
        {'value': 735, 'name': '运营部门'},
        {'value': 580, 'name': '人力资源部门'},
    ]
    data = {
        'status': True,
        'series': series
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def highchars(request):
    return render(request, 'highchars.html')