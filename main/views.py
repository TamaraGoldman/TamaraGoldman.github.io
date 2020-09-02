from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.utils import timezone
import datetime


#from .models import Question


def index(request):
    return render(request, 'main/index.html')

def video(request):
    return render(request, 'main/video.html')

def book(request):
    return render(request, 'main/book.html')

def feedback(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('thanks')
        else:
            error = 'Некорректное значение!'
    
    form = FeedbackForm()
    context = {
        'form': form
    }
    return render(request, 'main/feedback.html', context)
    
def thanks(request):
    return render(request, 'main/thanks.html')
