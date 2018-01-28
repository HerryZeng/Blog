# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from models import *


# Create your views here.

def index(request):
    try:
        archive_list = Article.objects.distinct_date()
        # for archive in archive_list:
        #     print(type(archive))
        #     print(archive)
        #     print(archive.decode('utf-8'))

        # 分类信息获取（导航数据）
        category_list = Category.objects.all()
        # 广告数据

        # 最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 10)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger) as error:
            article_list = paginator.page(1)
    except Exception as e:
        print(e)
    return render(request, 'index.html', locals())


def archive(request):
    try:
        archive_list = Article.objects.distinct_date()
        # article_list = Article.objects.distinct_date()
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        # print(year)
        # print(month)
        article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
        paginator = Paginator(article_list, 1)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger) as error:
            article_list = paginator.page(1)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)

    return render(request, 'archive.html', locals())
