from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

import datetime
import json

def acc_login(request):
    error_msg = ''
    today_str = datetime.date.today().strftime("%Y%m%d")
    # verify_code_img_path = "%s/%s" %(settings.VERIFICATION_CODE_IMGS_DIR,
    #                                  today_str)
    # if not os.path.isdir(verify_code_img_path):
    #     os.makedirs(verify_code_img_path,exist_ok=True)
    # #print("session:",request.session.session_key)
    # ##print("session:",request.META.items())
    # random_filename = "".join(random.sample(string.ascii_lowercase,4))
    # random_code = verify_code.gene_code(verify_code_img_path,random_filename)
    # cache.set(random_filename, random_code,30)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)  # 用户认证
        if user:
            login(request, user)  # 用户登录
            request.session.set_expiry(60 * 60)
            return HttpResponseRedirect(request.GET.get("next") if request.GET.get("next") else "/ymx01/product/")
        else:
            error_msg = "您输入的账号或者密码有误，请重新输入！"

    return render(request, 'login.html', {'error_msg': error_msg})


def acc_logout(request):
    logout(request)
    return redirect('/account/login/')