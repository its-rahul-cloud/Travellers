
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.db.models.signals import post_save
import  datetime

class Traveller(models.Model) :
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    contact_no=models.IntegerField(max_length=10,default=1)
    image=models.ImageField(upload_to='traveller',default="default.jpeg",null=True,blank=True)
    verification=models.FileField(upload_to='pdf',default='default.jpg',null=True,blank=True)

    def __str__(self):
        return str(self.id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Houseown(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    contact_no=models.IntegerField(max_length=10,default=1)
    image=models.ImageField(upload_to='Houseownimg')
    verification=models.FileField(upload_to='ownpdfs',default='default.jpg',null=True,blank=True)


    def __str__(self):
        return str(self.id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class House(models.Model):
    title=models.CharField(max_length=200,default='local')
    facility=models.CharField(max_length=200)
    image=models.ImageField(upload_to='House',null=True,blank=True)
    location = models.CharField(max_length=100,default='None')
    houseown=models.ForeignKey(Houseown,on_delete=models.CASCADE)
    space=models.IntegerField(max_length=20)
    price=models.IntegerField(default=100)


    
    def __str__(self):
        return str(self.id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

d = datetime.date(2022, 10, 19)
class Bookedhouse(models.Model):
    house=models.ForeignKey(House,on_delete=models.CASCADE)
    traveller=models.ForeignKey(Traveller,on_delete=models.CASCADE)
    start_date=models.DateField(default=d)
    end_date=models.DateField(default=d)

    def __str__(self):
        return str(self.id)

class Review(models.Model):
    house=models.ForeignKey(House,on_delete=models.CASCADE)
    author=models.ForeignKey(Traveller,on_delete=models.CASCADE)
    date_posted=models.DateTimeField( default=timezone.now)
    comment=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='post',default ="10.jpeg",null=True,blank = True)

    def __str__(self):
        return str(self.id)
