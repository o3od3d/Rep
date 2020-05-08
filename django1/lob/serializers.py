from rest_framework import  serializers
from .models import Board
from .models import Comment

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('board_title', 'board_contents', 'board_writer', 'board_date')

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = ('comment_contents', 'comment_writer', 'comment_date')