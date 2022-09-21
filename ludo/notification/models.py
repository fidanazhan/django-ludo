from django.db import models

from game.models import Game
from account.models import CustomUser

# Create your models here.
class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'request'), (2, 'approved'), (3, 'removed'), (4, 'unjoin'))

    game= models.ForeignKey(Game, on_delete=models.CASCADE, related_name = 'notification', null=True, blank=True)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'noti_from_user')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'noti_to_user')
    notification_types = models.IntegerField(choices = NOTIFICATION_TYPES)
    is_seen = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
