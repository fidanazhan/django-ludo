from django import forms
from . models import Game

class GameForm(forms.Form):
    SPORT_TYPE= [
    ('Futsal', 'Futsal'),
    ('Badminton', 'Badminton'),
    ('Football', 'Football'),
    ('Volleyball', 'Volleyball'),
    ('Rugby', 'Rugby'),    
    ('Tennis', 'Tennis'),
    ('Squash', 'Squash'),
    ('Basketball', 'Basketball'),
    ]

    COURT_STATUS = [
        ('1', 'Book'), 
        ('2', 'Not book')]

    sport_type = forms.CharField(
        label="Sport", max_length=100, widget=forms.Select(choices=SPORT_TYPE)
    )

    location1 = forms.CharField(max_length=100)
    location2 = forms.CharField(max_length=100)
    date = forms.DateField()
    # arranger = forms.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='arranged_player')
    occupied_player = forms.IntegerField()
    player_needed = forms.IntegerField()
    court_status = forms.CharField(widget=forms.Select(choices=COURT_STATUS))
    court_name = forms.CharField(max_length=100)
    court_price = forms.IntegerField()
    price_per_player = forms.IntegerField()


class GameForm1(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    # favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
