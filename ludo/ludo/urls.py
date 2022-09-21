from django.contrib import admin
from django.urls import path, include

from account.views import LoginView, RegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', include('account.urls')),
    path('game/', include('game.urls')),
    path('join/', include('join.urls')),
    path('notification/', include('notification.urls')),
]
