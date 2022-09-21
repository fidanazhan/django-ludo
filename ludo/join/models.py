from django.db import models

from account . models import CustomUser
from game . models import Game

from shortuuid.django_fields import ShortUUIDField

# Create your models here.
JOIN_RESPONSE = [
    ('Not Confirm', 'Not Confirm'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected')
]


class JoinRequest(models.Model):
    request_id = ShortUUIDField(primary_key=True, length=11, max_length=11, editable=False)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='sender')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='receiver')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True, related_name='game_joiner')
    response = models.CharField(max_length=12, choices=JOIN_RESPONSE, null=True, blank=True, default='Not Confirm')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)    
    updated_on = models.DateField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.request_id

    def response_accept(self):
        self.response = 'Accepted'
        self.is_active = False
        self.save()

    def response_reject(self):
        self.response = 'Rejected'
        self.is_active = False
        self.save()