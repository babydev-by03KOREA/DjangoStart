from django.db import models

# blog 앱에서 DB 내부에 Post table 생성 / name,content 갖도록 했고, id 자동 생성
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
