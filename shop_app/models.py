from django.db import models
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20,null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    TYPE_CHOICES = [
        ('kg','kg'),
        ('dona','dona'),
        ('litr','litr'),
        ('metr','metr')
    ]

    name = models.CharField(max_length=100,unique=True,help_text='Mahsulot nomi',validators=[MinLengthValidator(3)])
    product_type = models.CharField(max_length=10, choices=TYPE_CHOICES,default='kg')
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name