from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from . models import Notification

# Create your views here.
class NotificationView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        
        notifications = Notification.objects.filter(receiver=request.user)

        for notification in notifications:
            print(notification)

        context = {
            'notifications':notifications
        }

        return render(request, 'notification.html', context)