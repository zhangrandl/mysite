from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models


# Create your views here.

def db_handle(request):
    # request 用户请求的所有内容
    # request.GET   用户以POST提交
    # request.POST  用户以GET提交
    # 增加
    # models.UserInfo.objects.create(username='zhang', password='123456', age=11)
    # dic = {
    #     "username": 'zhangran',
    #     "password": '12313123',
    #     "age": 23
    # }
    # models.UserInfo.objects.create(**dic)
    # 删除
    # models.UserInfo.objects.filter(username='zhangran').delete()
    # 修改
    # models.UserInfo.objects.all().update(age=18)
    # 查找
    # models.UserInfo.objects.all() #查到所有数据
    # models.UserInfo.objects.all(age=18)   # 查到所有age=18的用户
    # models.UserInfo.objects.all(age=18).first()   # 查到所有age=18的用户的第一条数据
    # user_list_obj = models.UserInfo.objects.all()
    # for line in user_list_obj:
    #     print(line.username, line.age)
    if request.method == "POST":
        print(request.POST)
        models.UserInfo.objects.create(username=request.POST['username'],
                                       password=request.POST['password'],
                                       age=request.POST['age'])
    user_list_obj = models.UserInfo.objects.all()
    return render(request, 'app01/t1.html', {'li': user_list_obj})


def home(request):
    return HttpResponse("OK")


def news(request, nid1, nid2):
    response = "OK" + nid1 + nid2
    return HttpResponse(response)


def page(request, n2, n1):
    response = "OK" + n1 + n2
    return HttpResponse(response)


def special_case_2003(request):
    print("matched 2003")
    return HttpResponse("matched...")