from operator import and_
from telnetlib import GA
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView

from django.views import View
from django.db.models import Q
from .models import CustomUser

from game.models import Game
from join.models import JoinRequest
from notification.models import Notification

from .forms import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        games = Game.objects.filter(Q(player_joined = request.user) | Q(arranger=request.user)).order_by('-date').distinct()

        join_request = JoinRequest.objects.filter(Q(sender=request.user) & Q(is_active=True)).count()
        game_arranged_count = games.filter(Q(arranger=request.user) & Q(is_active=True)).count()

        for game in games:
            print(game.pk)

        context = {
            'games' : games,
            'join_request' : join_request,
            'game_arranged_count':game_arranged_count,
        }

        return render(request, 'index.html', context)

class HostGameListtView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        games = Game.objects.filter(arranger = request.user, is_active=True)

        context = {
            'games':games
        }

        return render(request, 'host_game_list.html', context)

class Joiner_JoinRequestListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        join_requests = JoinRequest.objects.filter(sender=request.user, is_active=True)
        join_request_count = join_requests.count()

        context = {
            'join_request_count' : join_request_count,
            'join_requests' : join_requests
        }

        return render(request, 'joiner_join_list.html', context)


class Host_JoinRequestListView(LoginRequiredMixin, View):
    def get(self, request, game_pk, *args, **kwargs):

        game = Game.objects.get(pk=game_pk)
        join_requests = JoinRequest.objects.filter(game__pk = game_pk).values('request_id','game_id','sender__username',
         'response', 'is_active')

        context = {
            'game' : game, 
            'join_requests' : join_requests,
        }

        return render(request, 'host_join_list_game.html', context)

class Host_RemovePlayerView(LoginRequiredMixin, View):
    def post(self, request, user, game_pk, *args, **kwargs):
        
        game = Game.objects.get(pk=game_pk)
        account = CustomUser.objects.get(username=user)

        game.player_needed_count_increase()
        game.remove_player(account)

        notification = Notification.objects.create(notification_types = 3, 
                                                    game = game,
                                                    sender=request.user, 
                                                    receiver=account)

        return redirect('host-join-list', game_pk = game_pk)

class Joiner_CancelRequestView(LoginRequiredMixin, View):
    def post(self, request, game_pk, *args, **kwargs):

        sender = request.user
        game = Game.objects.get(pk=game_pk)
        receiver = game.arranger

        if sender in game.request_user.all():
            game.request_user.remove(sender)
        
            join_request = JoinRequest.objects.filter(sender=sender, game=game, receiver=receiver, is_active=True).first()
            join_request.delete()

            notification = Notification.objects.filter(notification_types = 1, 
                                                       game = game,
                                                       sender=request.user, 
                                                       receiver=game.arranger).first()
            notification.delete() 
        

        return redirect('join-list-joiner')        

class Joiner_UnjoinView(LoginRequiredMixin, View):
    def post(self, request, game_pk, *args, **kwargs):

        sender = request.user
        game = Game.objects.get(pk=game_pk)

        if sender in game.player_joined.all():
            game.remove_player(sender)
            game.player_needed_count_increase()

            notification = Notification.objects.create(notification_types = 4, 
                                                       game = game,
                                                       sender=request.user, 
                                                       receiver=game.arranger)
       

        return redirect('dashboard') 

