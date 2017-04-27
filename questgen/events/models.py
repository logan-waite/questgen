from django.db import models
from games.models import Meter
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class Event_Type(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Event(models.Model):
    event_type = models.ForeignKey(Event_Type)
    choice = models.BooleanField(default=False)
    story = models.BooleanField(default=False)
    story_order = models.IntegerField(null=True)

class Action(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey(Event)
    meter = models.ForeignKey(Meter)
    meter_value = models.IntegerField()

    def __str__(self):
        return str(self.name)
