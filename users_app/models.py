from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# from users_app.models import *
# User.objects.all()
# User.objects.create(first_name="Bob",last_name="Ross",email_address="bobross@123.123",age=56)
# User.objects.create(first_name="Marshawn",last_name="Lynch",email_address="beastmode@123.123",age=32)
# User.objects.create(first_name="Boss",last_name="Mann",email_address="theboss@123.123",age=41)
# User.objects.all()
# User.objects.all()[2]
# User.objects.all()[0]
# c = User.objects.get(id=3)
# c.last_name = "Pancakes"
# c.save()
# User.objects.all()[2].last_name
# c = User.objects.get(id=2)
# c.delete()
# User.objects.all().order_by("first_name")  
# User.objects.all().order_by("first_name")