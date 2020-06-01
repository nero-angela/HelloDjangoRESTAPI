from rest_framework import serializers
from .models import Language

# HyperlinkedModelSerializer를 상속받으면 url을 추가할 수 있다.
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Language
    fields = ('id', 'url', 'name', 'paradigm')