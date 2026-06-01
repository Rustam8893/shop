

from django.shortcuts import render, redirect
from .forms import ProductForm,CustomUserForm
from .models import CustomUser, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

try:
    from allauth.socialaccount.models import SocialApp
except Exception:
    SocialApp = None


@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Bu foydalanuvchi nomi band!')
            return render(request, 'register.html')
            
        user = CustomUser.objects.create_user(username=username, password=password, phone=phone)
        return redirect('login')
    return render(request, 'register.html')

def login_page(request):
    next_url = request.GET.get('next', '') or request.POST.get('next', '')
    
    if request.user.is_authenticated:
        return redirect('home')

    
    google_enabled = False
    try:
        if SocialApp is not None:
            google_enabled = SocialApp.objects.filter(
                provider='google',
                sites__id=settings.SITE_ID,
            ).exclude(client_id__isnull=True).exclude(client_id__exact='').exclude(secret__isnull=True).exclude(secret__exact='').exists()
    except Exception:
        google_enabled = False

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Xush kelibsiz, {username}!')
            return redirect(next_url if next_url else 'home')
        else:
            messages.error(request, 'Foydalanuvchi nomi yoki parol xato!')
            return render(request, 'login.html', {'next': next_url, 'username': username, 'google_enabled': google_enabled})

    return render(request, 'login.html', {'next': next_url, 'google_enabled': google_enabled})


def logout_page(request):
    logout(request)
    return redirect('home')


def google_start(request):
    """Safe entry point for Google social login.
    - If a Google SocialApp is configured (has client id/secret attached to the SITE), redirect to the allauth provider start URL.
    - Otherwise, show a friendly message and redirect to the normal register page.
    """
    google_enabled = False
    try:
        if SocialApp is not None:
            google_enabled = SocialApp.objects.filter(
                provider='google',
                sites__id=settings.SITE_ID,
            ).exclude(client_id__isnull=True).exclude(client_id__exact='').exclude(secret__isnull=True).exclude(secret__exact='').exists()
    except Exception:
        google_enabled = False

    if google_enabled:
        # Start the allauth flow for Google
        return redirect('/accounts/google/login/')
    else:
        messages.info(request, "Google sozlanmagan — oddiy ro'yxatdan o'tish sahifasiga yo'naltirilyapti.")
        return redirect('register')


def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return redirect('home')
    return render(request, 'product_detail.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ProductForm()
    return render(request, 'add_product.html', {'form': form})



def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil muvaffaqiyatli yangilandi!')
            return redirect('home')
    else:
        form = CustomUserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html', {'user': request.user})




