from django.shortcuts import render

# Create your views here.
def gen_sta(request):
    return render(request,'gen_sta.html')