from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django_redis import get_redis_connection
from . import models
from ProjectManagement.common_tool import encrypt
import json,random


# Create your views here.


def register(req):
    """
    注册
    :param req:
    :return:
    """
    print("in register")
    data = json.loads(req.body)
    user_dict = {
        'name': data.get('name'),
        'sex': data.get('sex'),
        'age': data.get('age'),
        'telephone': data.get('telephone'),
        'department_ids': data.get('department_ids'),
        'password': encrypt(data.get('password', ''))
    }
    user = models.User.objects.filter(telephone=user_dict['telephone'], is_work=True)
    if user:
        return JsonResponse({"error": "电话号码已注册"}, status=200)

    # TODO 手机短信验证
    data = "1234567890zxcvbnmlkjhgfdsaqwertyuiop"
    captcha = random.sample(data,3)
    user_dict["captcha"]=captcha

    return JsonResponse(user_dict)


def register_msg(req):
    data = json.loads(req.body)
    user_dict = {
        'name': data.get('name'),
        'sex': data.get('sex'),
        'age': data.get('age'),
        'telephone': data.get('telephone'),
        'department_ids': data.get('department_ids'),
        'password': encrypt(data.get('password', ''))
    }
    if models.User.objects.count() == 0:
        user_dict['uid'] = 10000
        # level 现设定最高 4
        user_dict['job_level'] = 4
    new_user = models.User(**user_dict)
    new_user.save()
    user_dict['uid'] = new_user.uid
    return JsonResponse(user_dict, status=200)


def login(req):
    """
    登陆
    :param req:
    :return:
    """
    data = json.loads(req.body)
    telephone = data.get('telephone')
    user = models.User.objects.filter(telephone=telephone, is_work=True).first()
    if not user:
        return HttpResponse(data=json.dumps({'error': '未注册'}))
    if user.password != encrypt(data.get('password')):
        return HttpResponse(data=json.dumps({'error': '密码错误'}))
    user_dict = {
        'uid': user.uid,
        'name': user.name,
        'sex': user.sex,
        'age': user.age,
        'telephone': user.telephone,
        'job_level': user.job_level,
        'department_ids': user.department_ids
    }
    return JsonResponse(user_dict, status=200)


def get_postion(req):
    """
    获取职级
    :param req:
    :return:
    """
    data = json.loads(req.body)
    # 分配者的级别 在获取的时候处理 分配者 level 大于 被分配者
    level = data.get('level')
    # 获取电话号对应的人
    telephone = data.get('telephone')
    result = []
    if telephone:
        users = models.User.objects.filter(telephone=telephone, is_work=True)
    else:
        users = models.User.objects.filter(job_level__lt=level, is_work=True)
    for user in users:
        user_dict = {
            'uid': user.uid,
            'name': user.name,
            'sex': user.sex,
            'age': user.age,
            'telephone': user.telephone,
            'job_level': user.job_level,
            'department_ids': user.department_ids
        }
        result.append(user_dict)
    return JsonResponse(result)


def assign_postion(req):
    """
    分配职级
    :param req:
    :return:
    """
    data = json.loads(req.body)
    # 分配者的级别 在获取的时候处理 分配者 level 大于 被分配者
    # level = data['level']
    # 被分配者的uid
    uid = data['uid']
    uid_level = data['uid_level']
    user = models.User.objects.order_by(uid).filter(uid=uid).first()
    user.job_level = int(uid_level)
    user.save()
    return JsonResponse({'uid': user.uid, 'job_level': user.job_level})
