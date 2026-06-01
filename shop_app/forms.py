from django.forms import ModelForm
from .models import Product,CustomUser


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category','quantity', 'description', 'image']



class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']