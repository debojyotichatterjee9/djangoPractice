from django import forms

from .models import Job


class JobModelForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("This is not a valid job title")
        return title
