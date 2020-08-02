from django.shortcuts import render
from . import forms
from testapp.models import feedback
from testapp.forms import FeedBackForm
# Create your views here.
def  home(request):
    return render(request,'testapp/home.html')

def  product(request):
    return render(request,'testapp/products.html')

def  gallery(request):
    return render(request,'testapp/gallery.html')

def  contact(request):
    return render(request,'testapp/contact.html')

def feedback_view(request):
    form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Student Name:',form.cleaned_data['name'])
            print('Student Feedback:',form.cleaned_data['feedback'])
            form.save(commit=True)
            return render(request,'testapp/thankyou1.html',{'name':form.cleaned_data['name']})
    return render(request,'testapp/feedback.html',{'form':form})
