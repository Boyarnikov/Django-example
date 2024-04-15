from django.db import models


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=500)
    subtext = models.CharField(max_length=500, default="")
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.text


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    count = models.IntegerField()
