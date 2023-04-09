from django.contrib import admin

# Register your models here.

from .models import Product, Inbound,Outbound,Invetory

# Register your models here.
admin.site.register(Product)
admin.site.register(Inbound)
admin.site.register(Invetory)
admin.site.register(Outbound) # 이 코드가 나의 UserModel을 Admin에 추Outbound