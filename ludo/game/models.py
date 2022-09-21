from django.db import models

from account.models import CustomUser

# Create your models here.
class Game(models.Model):
    SPORT_TYPE= [
    ('futsal', 'Futsal'),
    ('badminton', 'Badminton'),
    ('football', 'Football'),
    ('volleyball', 'Volleyball'),
    ('rugby', 'Rugby'),    
    ('tennis', 'Tennis'),
    ('squash', 'Squash'),
    ('basketball', 'Basketball'),
    ]

    COURT_STATUS = ((1, 'Book'), (2, 'Not book'))

    sport_type = models.CharField(max_length=100, null=True, blank=True)
    location1 = models.CharField(max_length=100, null=True, blank=True)
    location2 = models.CharField(max_length=100, null=True, blank=True)
    # game_type = models.IntegerField()
    date = models.DateField()
    arranger = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='arranged_player', null=True, blank=True)
    occupied_player = models.PositiveSmallIntegerField(null=True, blank=True)
    player_needed = models.PositiveSmallIntegerField(null=True, blank=True)
    court_status = models.IntegerField(choices=COURT_STATUS)
    court_name = models.CharField(max_length=100, null=True, blank=True)
    court_price = models.SmallIntegerField()
    price_per_player = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)
    player_joined = models.ManyToManyField(CustomUser, related_name='joined_player')
    bookmark = models.ManyToManyField(CustomUser, blank=True, related_name='bookmark_game')
    request_user = models.ManyToManyField(CustomUser, related_name='request_joined_player')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sport_type

    def add_player(self, account):

        if not account in self.player_joined.all():
            self.player_joined.add(account)
            self.save()

    def remove_player(self, account):

        if account in self.player_joined.all():
            self.player_joined.remove(account)

    def remove_request_user(self, account):
        
        if account in self.request_user.all():
            self.request_user.remove(account)

    def unjoin_or_removed_joined_player(self, account):

        # Remove joined_player from game Model
        remove_joined_player_by_arranger = self
        remove_joined_player_by_arranger.remove_player(account)

    def get_request_user_count(self):
        return self.game_joiner.filter(is_active=True).count()

    def player_needed_count_decrease(self):
        self.player_needed = self.player_needed - 1
        self.save()

    def player_needed_count_increase(self):
        self.player_needed = self.player_needed + 1
        self.save()

class Gamelist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    game_arranger = models.ManyToManyField(Game, related_name='arranged_game')
    game_joiner = models.ManyToManyField(Game, related_name='joined_game')

    def __str__(self):
        return str(self.user)

    def user_game_arranged(self):
        # self.game_arranger
        game_arranged = Game.objects.filter(arranged=self.user)
        return game_arranged

    def user_game_joined(self):
        #self.game_joiner
        game_joined = Game.objects.filter(player_joined=self.user)
        return game_joined

class BookmarkGame(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True , blank=True , related_name='user_bookmark')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name = 'game_bookmark', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    