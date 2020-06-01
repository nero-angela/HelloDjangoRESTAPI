from django.db import models

"""
모델 수정시 마이그레이션 필요
$ python manage.py makemigrations

admin에서 해당 모델을 보기 위해선 `admin.py`에 아래 내용 추가 필요
```
from .models import Language
admin.site.register(Language)
```
"""
class Language(models.Model):
  name = models.CharField(max_length=50)
  paradigm = models.CharField(max_length=50)

  # admin에 노출될 컬럼 이름
  def __str__(self):
    return self.name