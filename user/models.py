from django.db import models

# Create your models here.
#user/models.py


# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"