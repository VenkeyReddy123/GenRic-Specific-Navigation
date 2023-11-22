from django.shortcuts import render

# Create your views here.
def Gen1(request):
    return render(request,'Gen1.html')
def Gen2(request):
    return render(request,'Gen2.html')