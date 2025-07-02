from django.db import models
from common.models import CommonModel
from users.models import User
class Video(CommonModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    link = models.URLField()
    category = models.CharField(max_length= 20)
    view_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField()
    video_file = models.FileField(upload_to = 'storage/') # 저장 경로를 알려줘야함


    user = models.ForeignKey(User, on_delete=models.CASCADE)
# User : Video 1:N