from django import forms

from .models import *

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)

	def __init__(self, question, **kwargs):
		self._question = question
		super(AnswerForm, self).__init__(**kwargs)

	def save(self):
		self.cleaned_data['question'] = self._question
		return Answer.objects.create(**self.cleaned_data)