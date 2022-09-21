from django.urls import path

from . views import (HomeView, 

                    # Host View
                    HostGameListtView, Host_JoinRequestListView, Host_RemovePlayerView, 
                    
                    # Joiner View
                    Joiner_JoinRequestListView, Joiner_CancelRequestView, Joiner_UnjoinView)

urlpatterns = [
    path('', HomeView.as_view(), name='dashboard'),
    path('games/', HostGameListtView.as_view(), name='host-list'),

    # Frm Host Perspective
    path('games/host/<int:game_pk>/', Host_JoinRequestListView.as_view(), name='host-join-list'), # Join request list
    path('games/host/<str:user>/<int:game_pk>/remove', Host_RemovePlayerView.as_view(), name='host-remove-player'),


    # From rom Joiner Perspective
    path('join-list/', Joiner_JoinRequestListView.as_view(), name='join-list-joiner'),
    path('games/host/<int:game_pk>/remove', Joiner_CancelRequestView.as_view(), name='joiner-cancel-request'),
    path('games/host/<int:game_pk>/unjoin', Joiner_UnjoinView.as_view(), name='joiner-unjoin'),

    # As host - Removed player
    
]
