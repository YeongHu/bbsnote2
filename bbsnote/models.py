from django.db import models

# Create your models here.
class Board(models.Model):      #게시글 모델
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):  #제목만 가져와 보여주는 게시판목록
        return self.subject

class Comment(models.Model):    #댓글 모델
    board = models.ForeignKey(Board, on_delete=models.CASCADE)  #models.CASCADE : 엮인 데이터와 연속적으로 작동
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):  #제목만 가져와 보여주는 게시판목록
        return self.content