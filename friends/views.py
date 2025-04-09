from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from accounts.models import FriendRequest,User

# Create your views here.

@login_required
def friends(request):
    if 'cart_count' not in request.session:
        request.session['cart_count']=0
    # friend_requests = request.user.received_requests.all()
    context = {
        'cart_count': request.session['cart_count'],
        # 'friend_requests': friend_requests
    }
    return render(request, 'friends/friends.html', context)

@login_required
def send_friend_request(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    if request.user != receiver:
        FriendRequest.objects.get_or_create(sender=request.user, receiver=receiver)
    return redirect('friends', user_id = user_id)

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