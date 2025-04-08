from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import FriendRequest
from django.contrib.auth import get_user_model
from django.db import transaction

# Create your views here.

User = get_user_model()

@login_required
def friends(request):
    if 'cart_count' not in request.session:
        request.session['cart_count']=0
    friend_requests = request.user.received_requests.all()
    context = {
        'cart_count': request.session['cart_count'],
        'friend_requests': friend_requests
    }
    return render(request, 'friends/friends.html', context)

@login_required
def send_friend_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Get username from form data
        try:
            receiver = User.objects.get(username=username)  # Find user by username
            if request.user != receiver:  # Ensure not sending a request to themselves
                FriendRequest.objects.get_or_create(sender=request.user, receiver=receiver)
        except User.DoesNotExist:
            # Handle case where user does not exist, perhaps by showing a message
            pass

    return redirect('friends')

@login_required
def view_friend_requests(request):
    friend_requests = request.user.received_requests.all()
    return render(request, 'friends/friend_requests.html', {'friend_requests': friend_requests})

@login_required
def accept_friend_request(request, request_id):
        friend_request = get_object_or_404(FriendRequest, id=request_id)

        if friend_request.receiver == request.user:
            # request.user.friends.add(friend_request.sender)
            # friend_request.sender.friends.add(request.user)
            friend_request.delete()  # Delete the request after acceptance
        # Optionally add a success message here
        else:
        # Handle an invalid request
            print("Invalid friend request.")
        return redirect('friends') 

@login_required
def decline_friend_request(request, request_id):
    # Get the friend request by ID and delete it
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if friend_request.receiver == request.user:  # Ensure that the user is the intended receiver
        friend_request.delete()  # Delete the request if conditions are met
    return redirect('friends')
