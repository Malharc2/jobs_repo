from django.shortcuts import render
from jobsapp.models import Hydjobs,Bangalorejobs,Punejobs
# Create your views here.
def homepage_view(request):
    return render(request,'jobsapp/index.html')

def Hydjobs_view(request):
    jobs_list=Hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/hydjobs.html',context=my_dict)