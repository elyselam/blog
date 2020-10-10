from django.shortcuts import render
from django.http import HttpResponse, HttpRequest




def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

posts = [
    {
        'author': 'elyse',
        'title': 'how to airflow',
        'content': 'here is how to do it',
        'date_posted': 'august 1, 2020'
    },
{
        'author': 'elyse',
        'title': 'how to sql',
        'content': 'here is how to do it',
        'date_posted': 'september 1, 2020'
    }
]