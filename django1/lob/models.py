from django.db import models

class Board(models.Model):
    board_title = models.CharField(max_length=200)
    board_contents = models.TextField()
    board_writer = models.CharField(max_length=200)
    board_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment_contents = models.TextField()
    comment_writer = models.CharField(max_length=200)
    comment_date= models.DateTimeField(auto_now_add=True)
    #comment_date = models.DateTimeField('date published')
# Create your models here.
