
from django.urls import path,include
from .views import home, register, login_page, logout_page, product_detail,add_product,edit_profile,profile
from .views import google_start

urlpatterns = [
    path('', login_page, name='root_login'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('accounts/google/start/', google_start, name='google_start'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
]
