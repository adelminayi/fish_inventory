from django.shortcuts import render, redirect
from .models import FishInventory, UserCredential
from django.contrib import messages

def public_view(request):
    search = request.GET.get('search', '')
    fishes = FishInventory.objects.all()
    if search:
        fishes = fishes.filter(name__icontains=search)
    return render(request, 'inventory/public_view.html', {'fishes': fishes})

def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        try:
            user = UserCredential.objects.get(phone=phone, password=password)
            request.session['user_phone'] = user.phone
            return redirect('user_view')
        except UserCredential.DoesNotExist:
            messages.error(request, 'Invalid phone number or password.')

    return render(request, 'inventory/login.html')

# def user_view(request):
#     if 'user_phone' not in request.session:
#         return redirect('login')
#     fishes = FishInventory.objects.all()
#     return render(request, 'inventory/user_view.html', {'fishes': fishes})
def user_view(request):
    phone = request.session.get('user_phone')
    if not phone:
        return redirect('login')

    search = request.GET.get('search', '')
    fishes = FishInventory.objects.all()
    if search:
        fishes = fishes.filter(name__icontains=search)

    return render(request, 'inventory/user_view.html', {'fishes': fishes})


def logout_view(request):
    request.session.flush()
    return redirect('public_view')

def about_view(request):
    return render(request, 'inventory/about.html')


def goods_view(request):
    phone = request.session.get('user_phone')
    search = request.GET.get('search', '')
    fishes = FishInventory.objects.all()
    if search:
        fishes = fishes.filter(name__icontains=search)

    return render(request, 'inventory/goods.html', {
        'fishes': fishes,
        'logged_in': bool(phone),
        'search': search
    })

