from django.shortcuts import render
from .models import Topic


# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    topic = Topic.objects.order_by('date_added')
    context = {'topics': topic}

    return render(request, 'learning_logs/topics.html', context)
