from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics,response
from .models import Question, Answer, Score
from .serializers import QuestionSerializer, AnswerSerializer, ScoreSerializer, UserSerializer
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated,AllowAny
from random import sample
# Create your views here.
def get_answer(request):
        dict_a = {'q':'a'}
        return HttpResponse(dict_a.values())
       # return response.Response(dict_a)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class AnswerView(generics.ListAPIView):
    
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerResponseView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class RandomQuestionView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.order_by('?')[:3]
    

    
