from rest_framework.serializers import ModelSerializer
from polls.models import Question

class QuetionSerialice(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'