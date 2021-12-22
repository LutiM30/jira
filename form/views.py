from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm,SnippetForm
# Create your views here.


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            descriptions = form.cleaned_data['descriptions']
            jira_project_id = form.cleaned_data['jira_project_id']

            print(title,descriptions,jira_project_id)

    form = ContactForm()
    return render(request, 'form.htm', {'form': form})

def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            print('VALID')
    form = SnippetForm()
    return render(request, 'form.htm', {'form': form})
