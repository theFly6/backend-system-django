from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class M1(MiddlewareMixin):
    """ 中间件1 """

    def process_request(self, request):
        except_lst = ['/account/login', '/image/code']
        if request.session.get('info') is None and request.path not in except_lst:
            return redirect('/account/login')
        # print('当前用户：', request.session.get('info'), request.session.session_key)
        # print(dict(request.session))

    def process_response(self, request, response):
        return response


class M3(MiddlewareMixin):
    """ 中间件3 """

    def process_request(self, request):
        print("中间件3：进来了")

    def process_response(self, request, response):
        print("中间价3：出去了")
        return response


class M2(MiddlewareMixin):
    """ 中间件2 """

    def process_request(self, request):
        print("中间件2：进来了")

    def process_response(self, request, response):
        print("中间价2：出去了")
        return response
