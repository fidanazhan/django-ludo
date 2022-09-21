from django.urls import path

from . views import Gameview, GameDetailView, BookmarkGameView


urlpatterns = [
    path('', Gameview.as_view(), name='game-list'),
    path('<int:pk>', GameDetailView.as_view(), name='game-detail'),
    path('<int:pk>', BookmarkGameView.as_view(), name='game-bookmark'),

]
