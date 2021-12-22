from django import forms
from .models import Snippet


class RequiredFieldsMixin():

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        fields_required = getattr(self.Meta, 'fields_required', None)

        if fields_required:
            for key in self.fields:
                if key not in fields_required:
                    self.fields[key].required = False

class ContactForm(forms.Form):
    title = forms.CharField()
    descriptions = forms.CharField(widget=forms.Textarea)
    jira_project_id = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[0-9]+', 'title': 'Enter numbers Only '}))


class SnippetForm(RequiredFieldsMixin,forms.ModelForm):

    class Meta:
        model=Snippet
        fields = ('title','descriptions','project_id')
        fields_required = '__all__'
        