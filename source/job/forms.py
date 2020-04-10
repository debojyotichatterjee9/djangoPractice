from django import forms

from .models import Job


class JobModelForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title'
        ]
    # the below validatio is just on the from level not model level
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not "JOB-" in title:
            raise forms.ValidationError("This is not a valid job title, add 'JOB-' in the title")
        return title
