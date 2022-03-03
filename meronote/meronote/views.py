from django.shortcuts import render
def home(request):
    c=''
    try:
        if request.method=="POST":
            n1=float(request.POST.get('num1'))
            n2=float(request.POST.get('num2'))
            opr=request.POST.get('opr')

            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2

    except:
        c="Invalid Operation.."
    print(c)
    return render(request,"index.html",{'c':c})
def saveform(request):
    c=''
    try:
        if request.method=="POST":
            n1=float(request.POST.get('num1'))
            n2=float(request.POST.get('num2'))
            opr=request.POST.get('opr')

            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2

    except:
        c="Invalid Operation.."
    print(c)
    return render(request,"myform.html",{'c':c})

    