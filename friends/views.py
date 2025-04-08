from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def friends(request):
    if 'cart_count' not in request.session:
        request.session['cart_count']=0
    template = loader.get_template('friends.html')
    return HttpResponse(template.render({'cart_count': request.session['cart_count']}))
