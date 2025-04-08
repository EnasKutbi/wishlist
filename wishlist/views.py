from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Wish
from .forms import wishForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if 'cart_count' not in request.session:
        request.session['cart_count']=0
    context = {
        'cart_count': request.session['cart_count']
        }
    return render(request, 'index.html', context)

@login_required
@csrf_exempt
def wishlist(request):
    if 'cart_count' not in request.session:
        request.session['cart_count']=0
    search_val = request.GET.get('search', '')
    if search_val:
        wish = Wish.objects.filter(name__icontains=search_val)  
    else:
        wish = Wish.objects.all()

    form = wishForm()
    context = {
        'form': form,
        'wish': wish,
        'cart_count': request.session['cart_count']
    }
    
    return render(request, 'wishlist.html', context)

def addWish(request):
    if 'cart_count' not in request.session:
        request.session['cart_count']=0
    form = wishForm()
    data = {
        'form': form,
        'cart_count': request.session['cart_count']
    }
    return render(request, 'add.html', data)

@csrf_exempt
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        store = request.POST.get('store')
        wish = Wish(name=name, description=description, image=image, store=store)
        wish.save()
        return redirect('wishlist')
    return redirect('wishlist')

def delete(request,id):
    if request.method == 'GET':  # Ensure it responds to GET requests
        wish = Wish.objects.get(id=id)
        wish.delete()  # Delete the item
        request.session['cart_count'] = request.session.get('cart_count', 1) - 1
        request.session.modified = True
        return JsonResponse({'success': True, 'cart_count': request.session['cart_count']})  # Return a success response
    return JsonResponse({'success': False}, status=400)

def edit(request, id):
    if 'cart_count' not in request.session:
        request.session['cart_count']=0
    wish = Wish.objects.get(id=id)
    items = {
        'wish': wish,
        'cart_count': request.session['cart_count']
    }
    return render(request, 'edit.html', items)

@csrf_exempt
def update(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        store = request.POST.get('store')

        wish = Wish.objects.get(id=id)

        wish.name=name
        wish.description=description
        wish.image=image
        wish.store=store

        wish.save()
        return redirect('wishlist')
    return redirect('wishlist')

@csrf_exempt
def add_to_cart(request):
    request.session['cart_count'] = request.session.get('cart_count', 0) + 1
    request.session.modified = True
    return JsonResponse({'cart_count': request.session['cart_count']})
