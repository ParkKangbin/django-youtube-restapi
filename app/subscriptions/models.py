from django.db import models
from common.models import CommonModel
# Create your models here.


class Subscription(CommonModel):
    Subscriber = models.ForeignKey('users.User',on_delete=models.CASCADE,related_name='subscriptions')
    Subscribed_to = models.ForeignKey('users.User',on_delete=models.CASCADE,related_name='subscribers')
    
