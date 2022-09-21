from telnetlib import GA
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect

from django.views import View
from django.db.models import Q

from . models import Game, BookmarkGame
from . forms import GameForm

# Create your views here.
class Gameview(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):

        games = Game.objects.exclude(Q(request_user = request.user) | Q(arranger=request.user) | Q(player_joined=request.user))
        form = GameForm()

        context = {
            'games':games,
            'form':form
        }

        return render(request, 'game_list.html', context)

    def post(self, request, *args, **kwargs):

        form = GameForm(request.POST)

        if form.is_valid():
            new_game = Game(
                sport_type = form.cleaned_data['sport_type'],
                location1 = form.cleaned_data['location1'],
                location2 = form.cleaned_data['location2'],
                date = form.cleaned_data['date'],
                arranger = request.user,
                occupied_player = form.cleaned_data['occupied_player'],
                player_needed = form.cleaned_data['player_needed'],
                court_status = form.cleaned_data['court_status'],
                court_name = form.cleaned_data['court_name'],
                court_price = form.cleaned_data['court_price'],
                price_per_player = form.cleaned_data['price_per_player'],
            )
            new_game.save()
            form = GameForm()

        return redirect('game-list') 

class GameDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        game = Game.objects.get(pk=pk)

        context = {
            'game':game,
        }

        return render(request, 'game_detail.html', context)

    # def post(self, request, pk, *args, **kwargs):
    #     pass

class BookmarkGameView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):

        user = request.user
        game = Game.objects.get(pk=pk)
        bookmark = BookmarkGame.objects.filter(user=user, game=game)

        if user not in game.bookmark.all():
            game.bookmark.add(user)
        else:
            game.bookmark.remove(user)

        if user.is_authenticated:
            if not bookmark:
                liked_post = BookmarkGame.objects.create(user=user, game=game)
            
            if bookmark:
                liked_post = BookmarkGame.objects.filter(user=user, game=game)
                liked_post.delete()

        next = request.POST.get('next', '')
        return HttpResponseRedirect(next)




