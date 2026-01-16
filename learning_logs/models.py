from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Userが学んでいるTopicを表す"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """modelの文字列表現を返す"""
        return self.text
    

class Entry(models.Model):
    """Topicに関して学んだ具体的なこと"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."