from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from .common_tool import encrypt
from .settings import SECRET_KEY
import json


class VerifyArgsMiddleware(MiddlewareMixin):

    def process_request(self, req):
        data = json.loads(req.body)
        orders = data["order"]
        args_str = ''
        for order in orders:
            args_str += str(data[order])
        if data['secret'] != encrypt(args_str + SECRET_KEY):
            return JsonResponse({'error': '参数验证失败'})
        return None
