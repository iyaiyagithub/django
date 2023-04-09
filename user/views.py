
from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 사용자가 데이터 베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/IM/')
        else:
            return render(request, 'user/signup.html')
    
    elif request.method == 'POST':
        
        username =request.POST.get('username','')
        password = request.POST.get('password','')
        password2 =request.POST.get('password2','')
       
# redirect 는 앞에 꼭 / 붙여줘야됨 . 안 그랬더니 signup 하고 그 뒤로 붙어서 signin signup/signin 이렇게 들어가서 페이없다고 나옴
                              
        if password != password2:
            
            return render(request, 'user/signup.html',{'error':'패스워드를 확인 해 주세요'})
        else:
            if username == '' or password == '':
                
                return render(request, 'user/signup.html',{'error':'사용자 이름과 비밀번호는 필수값입니다.'})  
            exist_user = get_user_model().objects.filter(username=username)
            # exist_user = UserModel.object.filter(username=username)
            if exist_user:
            
                return render(request, 'user/signup.html',{'error':'이미 존재하는 사용자입니다'})
            else:
                UserModel.objects.create_user(username=username,password=password)
                # 장고에서 기본적으로 제공하는 코드

                # new_user = UserModel()
                # new_user.username = username
                # new_user.password = password
                # new_user.bio = bio 
                # new_user.save()
                # 안쓰면 이렇게 길어짐

                return redirect('/signin/')

        

def sign_in(request):
    if request.method == 'POST':
        
        username = request.POST.get ('username','')
        password = request.POST.get ('password','')

        
        me =auth.authenticate(request, username=username, password=password)
        # me = UserModel.objects.get(username = username)

        # if me.password == password:
        if me is not None:
            # request.session['user'] = me.username
            auth.login(request,me)
            
            return render(request, 'product/IM.html')
        else:
            
            return render(request,'user/signin.html',{'error' : '유저이름 혹은 패스워드를 확인해주세요'})
                
        
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect ('/')
        else:
            return render(request, 'user/signin.html')
    


    # return render(request, 'user/signin.html')

# 로그아웃 / 사용자가 있다면 트윗 없다면 로그인 
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/signin/')

