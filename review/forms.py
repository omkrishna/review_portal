from django import forms
from .models import Review


class CreateReviewForm(forms.ModelForm):
	class Meta:
		model  = Review
		fields = [
			'title',
			'P_name',
			'quality',
			'difficulty',
			'would_take_again',
			'comments',
			'overall',
		 	]
		