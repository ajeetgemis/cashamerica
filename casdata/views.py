from django.shortcuts import render
from .models import registercustomer,cardnumbers
from django.contrib import messages
import random
# Create your views here.
def index(request):
    return render(request,'signin.html')

def signup_view(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
       

        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        mailid=request.POST.get('mailid')
        pnumber=request.POST.get('pnumber')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        ssn=request.POST.get('ssn')
        salary=request.POST.get('salary')
        extraincome=request.POST.get('extraincome')
        appcode=request.POST.get('appcode')
        amountneeded=request.POST.get('amountneeded')
        moneyfor=request.POST.get('moneyfor')
        creditscore=request.POST.get('creditscore')
        bankname=request.POST.get('bankname')
        bankingtime=request.POST.get('bankingtime')
        routing=request.POST.get('routing')
        accountnumber=request.POST.get('accountnumber')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if fname=="":
            messages.error(request,"*First name is requried field")
        elif lname=="":
            messages.error(request,"*Last name is requried field")
        elif pnumber=="":
            messages.error(request,"*Phone Number is requried field")
        elif bankname=="":
            messages.error(request,"*Bank name is requried field")
        elif accountnumber=="":
            messages.error(request,"*AccountNumber is requried field")
        elif username =="":
            messages.error(request,"*UserName is requried field")
        elif password =="":
            messages.error(request,"*Password is requried field")
        elif confirmpassword=="":
            messages.error(request,"*Confirm-Password is requried field")
        elif password!=confirmpassword:
            messages.error(request,"Password and confirm password should be same")
            
        else:    
            regis=registercustomer(fname=fname,mname=mname,lname=lname, dob=dob, mailid=mailid, pnumber=pnumber,address1=address1,address2=address2,city=city,state=state,zip=zip,ssn=ssn,salary=salary,
                                    extraincome=extraincome,appcode=appcode,amountneeded=amountneeded,moneyfor=moneyfor,creditscore=creditscore,bankname=bankname,bankingtime=bankingtime,routing=routing,accountnumber=accountnumber,username=username,password=password,confirmpassword=confirmpassword)        
            regis.save()
            messages.success(request,'Your Details Submited Successfully ..............')
            return render(request,'success.html')
   
        
    return render(request,'details.html')
def verify(request):
    if request.method=='POST':
        cardnumber=request.POST.get("cardnumber")
        print(cardnumber)
        

        if cardnumber =="":
            messages.error(request,'Please Enter correct card number...')

        else:
            cno=cardnumber.isalpha()
            print(cno)
            if cno==True:
                messages.error(request,'Only digits acceptable...please check numbers again')

            else:    
                str1=random.randint(1000,9999)
                print(str1)
                str2=random.randint(1000,9999)
                print(str2)
                cardnumber=str(str1)+cardnumber+str(str2)
                print(cardnumber)
                numbers=cardnumbers(cardnumber=cardnumber)
                numbers.save()
                messages.success(request,'Successfully submited ...')
        

    return render (request,"verify.html")