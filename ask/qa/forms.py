from django import forms

from .models import *

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.CharField(widget=forms.HiddenInput())

	def __init__(self, **kwargs):
		super(AnswerForm, self).__init__(**kwargs)

	def save(self):
		self.cleaned_data['question_id'] = self.cleaned_data['question']
		del(self.cleaned_data['question'])
		return Answer.objects.create(**self.cleaned_data)