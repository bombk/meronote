from django.shortcuts import render
from savefile.models import saveFile

from savefile.models import saveFile

def index(request):
    dataFile=saveFile.objects.all()
    data={
        'dataFile':dataFile,
    }
    
    return render(request,"index.html",data)

def home(request,id):
    dataFile=saveFile.objects.get(id=id)
    data={
        'dataFile':dataFile,
    }
    
    return render(request,"index.html",data)

def leftside(request):
    dataList=saveFile.objects.all()
    data={
        'dataList': dataList,
    }
    return render(request,'leftside.html',data)

def saveform(request):
    m=''
    if request.method=='POST':
        name1=request.POST.get('name')
        message1=request.POST.get('message')
        fname1=request.POST.get('fname')
        en=saveFile(name=name1,message=message1,fname=fname1) ##get all data in modelClass
        en.save()
        m="Data Insert Sucessfully"

    return render(request,'myform.html',{'m':m})
   
    