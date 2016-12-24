from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.FloatField()
	author = models.ForeignKey(User, on_delete=models.SET_NULL)
	links = models.ManyToManyField(User)

	class Meta:
		db_table = 'qa_question'

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.SET_NULL)

	class Meta:
		db_table = 'qa_answer'

class QuestionManager(models.Manager):
	def new(self, count=10):
		return super(QuestionManager, self).get_queryset().order_buy("-added_at")[:count]

	def popular(self):
		return super(QuestionManager, self).get_queryset().order_buy("-rating")
