from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def saveform(request):
    return render(request,'myform.html')