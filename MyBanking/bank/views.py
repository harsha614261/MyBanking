from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
# Create your views here.
from .models import Query,transaction
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=="POST":
        fname=request.POST['Firstname']
        sname = request.POST['Lastname']
        email=request.POST['E-mail']
        num=request.POST['number']
        uname=fname+sname
        pass1=request.POST['fpassword']
        pass2=request.POST['spassword']
        if pass1==pass2:
            post_man(fname,sname,email,num,uname)
            user=User.objects.create_user(username=uname, email=email, password=pass1, first_name=fname, last_name=sname,)
            user.save()
            return redirect('login')
        else:
            return HttpResponse("Password Mismatch")
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        usern=request.POST['uname']
        passw=request.POST['password']
        user=auth.authenticate(username=usern,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('safe')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def Message(request):
    if request.method=="POST":
        Name = request.POST['name']
        Email = request.POST['email']
        Contact = request.POST['number']
        Querymes = request.POST['message']
        nor=Query(Name=Name,Email=Email,Contact=Contact,Querymes=Querymes)
        nor.save()
        return HttpResponse("Successfully Submitted")

def safe(request):
    if request.user.is_authenticated:
        p=transaction.objects.all()
        for t in p:
            if request.user.first_name==t.Name and request.user.email==t.email:
                w=t.account
        return render(request,'safe.html',{'name':request.user.username,'acc':w})
    else:
        return redirect('login')
def post_man(fname,sname,email,num,uname):
    a=transaction(Name=fname,email=email,username=uname,account=num,amount=0,message="")
    a.save()

def addfunds(request):
    if request.user.is_authenticated:
        acc=request.POST['account_no']
        amount=request.POST['amount']
        ledger=transaction.objects.all()
        p="\n"
        for t in ledger:
            if (t.email==request.user.email and t.account==acc and t.username==request.user.username):
                t.amount=t.amount+int(amount)
                t.message=t.message+"/"+"Added funds INR "+str(amount)+"/"
                t.save()
                return HttpResponse("amount added successfully")
def balance(request):
    if request.user.is_authenticated:
        deal=transaction.objects.all()
        name=request.user.first_name
        uname=request.user.username
        email=request.user.email
        for t in deal:
            if t.Name==name and t.username==uname and t.email==email:
                print(t.amount)
                return render(request,'balance.html',{'bal':t.amount})
def statements(request):
    if request.user.is_authenticated:
        deal=transaction.objects.all()
        name=request.user.first_name
        uname=request.user.username
        email=request.user.email
        for t in deal:
            if t.Name==name and t.username==uname and t.email==email:
                return render(request,'statements.html',{'message':t.message})
def transfer(request):
    if request.user.is_authenticated:
        cname=request.user.first_name
        cmail=request.user.email
        rname=request.POST['sname']
        raccount=request.POST['account_no']
        ramount=request.POST['amount']
        que=transaction.objects.all()
        if userornot(rname,raccount):
            for i in que:
                if i.Name==cname and i.email==cmail:
                    if i.amount>=int(ramount):
                        i.amount=i.amount-int(ramount)
                        i.message=i.message+"amount sent successfully to "+str(rname)+" with a/c "+raccount
                        i.save()
                        updaterec(que,cname,i.account,ramount,rname,raccount)
                        return HttpResponse('Amount sent successfully')
                    else:
                        return HttpResponse('Insufficient Funds')
        else:
            return HttpResponse('Invalid receiver details')
def userornot(rname,raccount):
    print(rname,raccount)
    que=transaction.objects.all()
    for t in que:
        if t.Name==rname and t.account==raccount:
            return 1
    return 0

def updaterec(que,cname,acc,ramount,rname,racc):
    for t in que:
        if t.Name==rname and t.account==racc:
            t.amount=t.amount+int(ramount)
            t.message=t.message+"Received funds successfullly from "+cname+" with a/c "+acc
            t.save()




