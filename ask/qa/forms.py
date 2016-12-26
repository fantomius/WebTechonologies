from django import forms

from .models import *

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question_id = forms.CharField(widget=forms.HiddenInput())

	def __init__(self, **kwargs):
		self._question = question
		super(AnswerForm, self).__init__(**kwargs)

	def save(self):
		return Answer.objects.create(**self.cleaned_data)