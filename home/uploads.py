# -*- coding: utf-8 -*-
import datetime as dt
import json
import os
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_image(request, dir_name):
    """
    kindeditor图片上传返回数据格式说明
    :param request:Request Object
    :param dir_name:upload directory
    :return:'error':1,'message':'出错信息'},'error':0,'url':'图片地址'}
    """

    result = {'error': 1, 'message': '上传出错'}
    files = request.FILES.get('imgFile', None)
    if files:
        result = image_upload(files, dir_name)
    return HttpResponse(json.dumps(result), content_type="application/json")


# 创建目录
def upload_generation_dir(dir_name):
    today = dt.datetime.today()
    dir_name = dir_name + '/%d/%d/' % (today.year, today.month)
    if not os.path.exists(settings.MEDIA_ROOT + dir_name):
        os.makedirs(settings.MEDIA_ROOT + dir_name)
    return dir_name


# 图片上传
def image_upload(files, dirname):
    # 允许上传文件类型
    allow_suffix = ['jpg', 'png', 'jpeg', 'gif', 'bmp']
    file_suffix = files.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        return {'error': 1, 'message': '图片格式不正确'}

    relative_path = upload_generation_dir(dirname)
    path = os.path.join(settings.MEDIA_ROOT, relative_path)
    if not os.path.exists(path):    #如果目录不存在就创建目录
        os.makedirs(path)
    file_name = str(uuid.uuid1()) + "." + file_suffix
    path_file = os.path.join(path, file_name)
    file_url = settings.MEDIA_URL + relative_path + file_name
    open(path_file, 'wb').write(files.file.read())      #保存图片
    return {'error': 0, 'url': file_url}
