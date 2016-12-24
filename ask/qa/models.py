from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class QuestionManager(models.Manager):
	def new(self):
		return super(QuestionManager, self).get_queryset().order_buy("-added_at")

	def popular(self):
		return super(QuestionManager, self).get_queryset().order_buy("-rating")

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255, default="")
	text = models.TextField(default="")
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User)

	objects = QuestionManager()

	def get_url(self):
		return reverse("question_details", args=(self.pk,))

	class Meta:
		db_table = 'qa_question'

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

	class Meta:
		db_table = 'qa_answer'
