"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.urls import include, path

from links import views as linkviews

from links.views import LinkCreateView, LinkDetailView, LinkUpdateView, LinkDeleteView

urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', linkviews.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('links/create/', login_required(LinkCreateView.as_view()), name='create'),
    path('link/(?P<pk>\d+)/', LinkDetailView.as_view(), name='link_detail'),
    path('links/delete/(?P<pk>\d+)', login_required(LinkDeleteView.as_view()), name='link_delete'),
    path('links/update/(?P<pk>\d+)/', login_required(LinkUpdateView.as_view()), name='link_update'),
    path('comment/(?P<pk>\d+)', linkviews.link_comment, name='link_comment'),
    path('reply/(?P<pk>\d+)', linkviews.reply_comment, name='reply_comment'),
    path('', include('links.urls'))
]
