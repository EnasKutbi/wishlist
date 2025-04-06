from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Wish
from .forms import wishForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@csrf_exempt
def wishlist(request):
    search_val = request.GET.get('search', '')
    if search_val:
        wish = Wish.objects.filter(name__icontains=search_val)  
    else:
        wish = Wish.objects.all()

    form = wishForm()
    context = {
        'form': form,
        'wish': wish
    }
    
    return render(request, 'wishlist.html', context)

def addWish(request):
    template = loader.get_template('add.html')
    form = wishForm()
    return HttpResponse(template.render({'form': form}))

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
        return JsonResponse({'success': True})  # Return a success response
    return JsonResponse({'success': False}, status=400)

def edit(request, id):
    template = loader.get_template('edit.html')
    wish = Wish.objects.get(id=id)
    items = {
        'wish': wish
    }
    return HttpResponse(template.render(items))

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