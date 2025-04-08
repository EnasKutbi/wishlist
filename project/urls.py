"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wishlist import views as _wishlist
from friends import views as _friends
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', _wishlist.index, name='index'),
    path('wishlist/', _wishlist.wishlist, name='wishlist'),
    path('addWish/', _wishlist.addWish, name='add'),
    path('create/', _wishlist.create, name='create'),
    path('delete/<int:id>/', _wishlist.delete, name='delete'),
    path('edit/<int:id>', _wishlist.edit, name='edit'),
    path('update', _wishlist.update, name='update'),
    path('addtocart/', _wishlist.add_to_cart, name='add_to_cart'),
    path('friends/', _friends.friends, name='friends')

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
