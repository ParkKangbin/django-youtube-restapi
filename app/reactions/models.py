from django.db import models
from common.models import CommonModel
# Create your models here.

class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete= models.CASCADE)
    video = models.ForeignKey('videos.Video',on_delete=models.CASCADE)  
    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE , 'Like'),
        (DISLIKE,'Dislike'),
        (NO_REACTION,'No Reaction')
    )

    reaction = models.IntegerField(
        choices = REACTION_CHOICES,
        default = NO_REACTION
    )