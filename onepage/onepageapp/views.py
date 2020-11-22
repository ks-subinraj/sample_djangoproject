from django.shortcuts import render
from .models import work,features
# Create your views here.
def home(request):
    obj=work.objects.all()
    obj1=features.objects.all()
    return render(request,'index.html',{'results':obj,'res':obj1})