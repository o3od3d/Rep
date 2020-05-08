from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BoardSerializer, CommentSerializer
from .models import Board, Comment

class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# Create your views here.
