from django.shortcuts import render, redirect
#product/models.py
from django.db import models
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import Product, Inbound, Outbound, Invetory

# Create your views here.



# view
@login_required
def product_list(request):
    if request.method == 'GET':
        product__list = Product.objects.all()
    # 입출고 리스트 + -
	# 재고 리스트 합산
        print(product__list,'프로덕트리스트')
        return render (request, 'product/IM.html',{'product':product__list})
    elif request.method == 'POST':
        print(request.POST,'리퀘스트포스트메쏘드')
       
        product = Product()
        # product.author = user
        product.description = request.POST.get('description','')
        name = request.POST.get('name','')
        code = request.POST.get('code','')
        price = request.POST.get('price','')
        size = request.POST.get('size','')
        
        
        print(product.name,product.code,product.price,product.size,'입력완료')
        
        
        product.name = name
        product.code = code
        product.price = price
        product.size = size
        product.save()
        return redirect('/IM/')

    
    # 등록 된 상품의 리스트를 볼 수 있는 view


@login_required
def product_create(request):
	
    
   if request.method == 'POST':
        print(request.POST)
        user = request.user
        product = Product()
        # product.author = user
        product.description = request.POST.get('description','')
        name = request.POST.get('name','')
        code = request.POST.get('code','')
        price = request.POST.get('price','')
        size = request.POST.get('size','')
        
        print(product.name,product.code,product.price,product.size)
        
        
        product.name = name
        product.code = code
        product.price = price
        product.size = size
        product.save()
        return redirect('/IM/')
   
@login_required
def product_delete(request,id):
    
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/IM/')
             
    
  
# @login_required
# def delete_tweet(request,id):
#     my_tweet = TweetModel.objects.get(id=id)
#     my_tweet.delete()
#     return redirect('/tweet')


   
             

    
    # 상품 등록 views

# ----> 여기서부터 IM2 를 댓글창 만들었던 것처럼 활용할 것임

# view
@login_required
@transaction.atomic
def inbound_create(request, product_id):
    
  if request.method == 'POST':
    inbound = Inbound()
    # inbound.product = request.POST.
    inbound.date = request.POST.get('inbound-date','')
    inbound.price = request.POST.get('inbound-price','')
    inbound.quantity = request.POST.get('inbound-quantity','')
    
    inbound.save()
    render (request, '/IM2/')
    
  
    

    
    # 상품 입고 view
    # 입고 기록 생성
    
		# 입고 수량 조정



@login_required
def outbound_create(request, product_id):
    
    outbound = Outbound()
    # outbound.product = request.POST.get('product','')
    outbound.date = request.POST.get('outbound-date','')
    outbound.price = request.POST.get('outbound-price','')
    outbound.quantity = request.POST.get('outbound-quantity','')
    outbound.save()    
    
		# 상품 출고 view
    # 출고 기록 생성
    
		# 재고 수량 조정



@login_required
def inventory(request, product_id):
    
	inventory = Invetory()
        
	inventory.quantity = Inbound.quantity - Outbound.quantity
    


	sum = Outbound.price - Inbound.price 
        

	qua = inventory.quantity
        
	render ( request, 'product/IM2.html' , {'inventory-quantity': qua }, {'inventory-sum':sum})
        
	# """
	# inbound_create, outbound_create view에서 만들어진 데이터를 합산합니다.
	# Django ORM을 통하여 총 수량, 가격등을 계산할 수 있습니다.
	# """
    
	# 총 입고 수량, 가격 계산

	# 총 출고 수량, 가격 계산




    
# def tweet(request):
#     if request.method == 'GET':
#         user = request.user.is_authenticated

#         if user:
#             # 트윗 모ㄹㅔ 저ㅇㅏㄴ 모ㄴ 데터ㄹ 불러오겠다 순서는 데이터베이스에 저장된 순서대로 불러온다. -를 붙이 면  역순
#             all_tweet = TweetModel.objects.all().order_by('-created_at')
#             # 화면에 넘겨주기{'tweet':all_tweet} 위 변수에 저정해서 딕셔너리 형태로 넘겨줌

#             return render(request, 'tweet/home.html', {'tweet':all_tweet})
        
#         else:
#             return redirect('/sign-in/')
        
#     elif request.method == 'POST':
#         user = request.user
#         my_tweet = TweetModel()
#         my_tweet.author = user
#         my_tweet.content = request.POST.get('my-content','')
#         my_tweet.save()
#         return redirect('/tweet/')
    
    
 
# def home(request):
#     user = request.user.is_authenticated
#     if user:
#         return redirect ('/tweet')
#     else:
#         return redirect('/sign-in/')
    
    
# def tweet(request):
#     if request.method == 'GET':
#         user = request.user.is_authenticated

#         if user:
#             # 트윗 모ㄹㅔ 저ㅇㅏㄴ 모ㄴ 데터ㄹ 불러오겠다 순서는 데이터베이스에 저장된 순서대로 불러온다. -를 붙이 면  역순
#             all_tweet = TweetModel.objects.all().order_by('-created_at')
#             # 화면에 넘겨주기{'tweet':all_tweet} 위 변수에 저정해서 딕셔너리 형태로 넘겨줌

#             return render(request, 'tweet/home.html', {'tweet':all_tweet})
        
#         else:
#             return redirect('/sign-in/')
        
#     elif request.method == 'POST':
#         user = request.user
#         my_tweet = TweetModel()
#         my_tweet.author = user
#         my_tweet.content = request.POST.get('my-content','')
#         my_tweet.save()
#         return redirect('/tweet/')
    
    
 
#  ''''''

# @login_required
# def delete_tweet(request,id):
#     my_tweet = TweetModel.objects.get(id=id)
#     my_tweet.delete()
#     return redirect('/tweet')

# @login_required
# def detail_tweet(request, id):
#     my_tweet = TweetModel.objects.get(id=id)
#     tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
#     return render(request,'tweet/tweet_detail.html',{'tweet':my_tweet,'comment':tweet_comment})


# @login_required
# def write_comment(request, id):
#     if request.method == 'POST':
#         comment = request.POST.get("comment","")
#         current_tweet = TweetModel.objects.get(id=id)

#         TC = TweetComment()
#         TC.comment = comment
#         TC.author = request.user
#         TC.tweet = current_tweet
#         TC.save()

#         return redirect('/tweet/'+str(id))


# @login_required
# def delete_comment(request, id):
#     comment = TweetComment.objects.get(id=id)
#     current_tweet = comment.tweet.id
#     comment.delete()
#     return redirect('/tweet/'+str(current_tweet))