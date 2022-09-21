from django.urls import path

from . views import SendJoinRequestView, JoinRequestResponseView


urlpatterns = [
    path('<int:game_pk>/create', SendJoinRequestView.as_view(), name='create-join-request'),
    path('<str:join_pk>/response', JoinRequestResponseView.as_view(), name='response-join-request'),
]
