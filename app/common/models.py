from django.db import models

class CommonModel(models.Model):
    #데이터 생성 시간
    created_at = models.DateTimeField(auto_now_add=True)

    # 데이터가 업데이트된 시간을 데이터가 업데이트 될떄마다 계속 갱신
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True # 데이터 베이스 테이블에 추가하지말라~