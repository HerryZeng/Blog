from django.shortcuts import render
from models import *
# Create your views here.

def index(request):
    try:
        category_list = Category.objects.all()
    except Exception as e:
        print(e)
    return render(request, 'index.html', locals())