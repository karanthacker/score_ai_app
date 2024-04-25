from rest_framework import serializers
from .models import Question, Answer, Score
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
        'password': {'write_only': True}
    }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
   
    

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ScoreSerializer(serializers.Serializer):
    class Meta:
        model = Score
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }