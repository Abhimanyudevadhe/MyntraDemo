from django.shortcuts import render
from .forms import FeedbackForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(r):
    return render(r,'homeapp/index.html')

def feedback(r):
    form= FeedbackForm()
    if r.method=='POST':
        form=FeedbackForm(r.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    return render(r,'homeapp/feedback.html',{'form':form})