from django.shortcuts import render, redirect

from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from notification.models import Notification


from . models import JoinRequest
from game . models import Game, Gamelist

# Create your views here.
class SendJoinRequestView(LoginRequiredMixin, View):
    def post(self, request, game_pk,*args, **kwargs):
        
        sender = request.user
        game = Game.objects.get(pk=game_pk)
        receiver = game.arranger

        if sender not in game.request_user.all():
            game.request_user.add(sender)
        
        if sender.is_authenticated:
            join_request = JoinRequest.objects.create(sender=sender, game=game, receiver=receiver)

            notification = Notification.objects.create(notification_types = 1, 
                                                       game = game,
                                                       sender=request.user, 
                                                       receiver=game.arranger) 
        

        return redirect('game-list')

class JoinRequestResponseView(LoginRequiredMixin, View):
    def post(self, request, join_pk, *args, **kwargs):

        join_request = JoinRequest.objects.get(pk=join_pk)
        sender = join_request.sender

        game = Game.objects.get(pk=join_request.game.pk)

        join_response = request.POST['host-decision']

        if join_response == 'Accept':

            join_request.response_accept()

            game.add_player(sender)
            game.player_needed_count_decrease()
            game.remove_request_user(sender)

            notification = Notification.objects.create(notification_types = 2, 
                                                       game = game,
                                                       sender=request.user, 
                                                       receiver=sender) 

        elif join_response == "Decline":

            join_request.response_reject()

            game.remove_request_user(sender)

        else:
            return redirect('host-join-list', game_pk = join_request.game.pk)
        
        return redirect('host-join-list', game_pk = join_request.game.pk)


