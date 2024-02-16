from django.shortcuts import render,redirect
from django.contrib.auth import logout
from website.models import *
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount


def home(request):
    if (request.user.is_authenticated):
        remail=request.user.email
        if (user_table.objects.filter(uemail=remail).exists()  or  agency_table.objects.filter(aemail=remail).exists()):
            extra_data = SocialAccount.objects.get(user=request.user).extra_data
            extra={'extra': extra_data }
        else:
            extra=None
    else:
        extra=None
    return render(request,"index.html",extra)

#User's View Function

def login_user(request):
    if (request.user.is_authenticated):
        remail=request.user.email
        if user_table.objects.filter(uemail=remail).exists():
            request.session['email_id'] = remail
            return redirect('user_dashboard')
        elif agency_table.objects.filter(aemail=remail).exists():
            auth.logout(request)
            messages.warning(request,"Signed in as %s"%remail)
            messages.warning(request,"Email Already registered as Agency. If you want to register as Parent use another email.")
        else:
            return redirect('user_form')
    else:
        messages.warning(request,"Google Login Error!")
        return redirect('home')
    return redirect('home')


@login_required(login_url='home')
def user_form(request):
    userdata={'userdata':request.user}
    remail=request.user.email
    if request.method=="POST":
        mfname = request.POST.get('malefname')
        mmname = request.POST.get('malemname')
        mlname = request.POST.get('malelname')
        mdob = request.POST.get('maledob')
        mnationality = request.POST.get('malenationality')
        moccupation = request.POST.get('maleoccupation')
        mincome = request.POST.get('maleincome')
        mwork = request.POST.get('maleplace')
        mstate = request.POST.get('malestate')
        ffname = request.POST.get('femalefname')
        fmname = request.POST.get('femalemname')
        flname = request.POST.get('femalelname')
        fdob = request.POST.get('femaledob')
        fnationality = request.POST.get('femalenationality')
        foccupation = request.POST.get('femaleoccupation')
        fincome = request.POST.get('femaleincome')
        fwork = request.POST.get('femaleplace')
        fstate = request.POST.get('femalestate')
        bchild = request.POST.get('biochild')
        achild = request.POST.get('adoptchild')
        uaddress = request.POST.get('useradd')
        upincode = request.POST.get('userpincode')
        uemail = remail
        uphone = request.POST.get('userphone')

        user=user_table( mfname = mfname,mmname = mmname,mlname = mlname,mdob = mdob,mnationality = mnationality,moccupation = moccupation,mincome = mincome,mwork = mwork,mstate = mstate,ffname = ffname,fmname = fmname,flname = flname,fdob = fdob,fnationality = fnationality,foccupation = foccupation,fincome = fincome,fwork = fwork,fstate = fstate,bchild = bchild,achild = achild,uaddress = uaddress,upincode = upincode,uemail = uemail,uphone = uphone)
        user.save()
        messages.success(request, "Registration Form Submitted and Profile Created Successfully")

        request.session['email_id'] = uemail
        return redirect('user_dashboard')

    return render(request,'user/user-form.html',userdata)

@login_required(login_url='home')
def user_dashboard(request):
    if request.method=="POST" and request.POST.get('state')!="None":
        value=request.POST.get('state')
        agencydata=agency_table.objects.filter(astate=value)
        extra_data = SocialAccount.objects.get(user=request.user).extra_data
        result={
            'agencydata':agencydata,
            'extra': extra_data,
            'value':value
        }
        return render(request,'user/user-dashboard.html',result)
    else:
        agencydata=agency_table.objects.all()
        extra_data = SocialAccount.objects.get(user=request.user).extra_data
        result={
            'agencydata':agencydata,
            'extra': extra_data
        }
        return render(request,'user/user-dashboard.html',result)

    

@login_required(login_url='home')
def rules(request):
    extra_data = SocialAccount.objects.get(user=request.user).extra_data
    extra={'extra': extra_data }
    return render(request,"user/rules.html",extra)

@login_required(login_url='home')
def edit_profile(request):
    remail=request.user.email
    if user_table.objects.filter(uemail=remail).exists():
        extra_data = SocialAccount.objects.get(user=request.user).extra_data
        user = user_table.objects.get(uemail = remail)
        userdata={'userdata':user,'extra': extra_data}
        if request.method=="POST":
            user.moccupation = request.POST.get('maleoccupation')
            user.mincome = request.POST.get('maleincome')
            user.mwork = request.POST.get('maleplace')
            user.mstate = request.POST.get('malestate')
            user.foccupation = request.POST.get('femaleoccupation')
            user.fincome = request.POST.get('femaleincome')
            user.fwork = request.POST.get('femaleplace')
            user.fstate = request.POST.get('femalestate')
            user.bchild = request.POST.get('biochild')
            user.achild = request.POST.get('adoptchild')
            user.uaddress = request.POST.get('useradd')
            user.upincode = request.POST.get('userpincode')
            user.uphone = request.POST.get('userphone')
            user.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('edit_profile')
        return render(request,"user/edit-profile.html",userdata)
    else:
        messages.warning(request,"%s not registered as Parent"%remail)
        return redirect('home')
    





#Agency's View Function

def login_agency(request):
    if (request.user.is_authenticated):
        remail=request.user.email
        if agency_table.objects.filter(aemail=remail).exists():
            request.session['email_id'] = remail
            return redirect('agency_dashboard')
        elif user_table.objects.filter(uemail=remail).exists():
            auth.logout(request)
            messages.success(request,"Signed in as %s"%remail)
            messages.warning(request,"Email Already registered as Parent. If you want to register as Agency use another email.")
        else:
            return redirect('agency_form')
    else:
        messages.warning(request,"Google Login Error!")
        return redirect('home')
    return redirect('home')


@login_required(login_url='home')
def agency_form(request):
    agencydata={'agencydata':request.user}
    remail=request.user.email
    if request.method=="POST":
        aname = request.POST.get('agencyname')
        aemail = remail
        aphone = request.POST.get('agencynumber')
        aaddress = request.POST.get('agencyadd')
        astate = request.POST.get('agencystate')
        apincode = request.POST.get('agencypincode')
        mzerotofive = request.POST.get('malezerotofive')
        mfivetoten = request.POST.get('malefivetoten')
        mtentofifteen = request.POST.get('maletentofifteen')
        mabovefifteen = request.POST.get('maleabovefifteen')
        fzerotofive = request.POST.get('femalezerotofive')
        ffivetoten = request.POST.get('femalefivetoten')
        ftentofifteen = request.POST.get('femaletentofifteen')
        fabovefifteen = request.POST.get('femaleabovefifteen')

        agency = agency_table(aname = aname,aemail = aemail,aphone = aphone,aaddress = aaddress,astate=astate,apincode = apincode,mzerotofive = mzerotofive,mfivetoten = mfivetoten,mtentofifteen = mtentofifteen,mabovefifteen = mabovefifteen,fzerotofive = fzerotofive,ffivetoten = ffivetoten,ftentofifteen = ftentofifteen,fabovefifteen = fabovefifteen)
        agency.save()
        messages.success(request, "Registration Form Submitted and Profile Created Successfully")

        request.session['email_id'] = aemail
        return redirect('agency_dashboard')
    return render(request,'agency/agency-form.html',agencydata)


@login_required(login_url='home')
def agency_dashboard(request):
    remail=request.user.email
    if agency_table.objects.filter(aemail=remail).exists():
        agencdata = agency_table.objects.get(aemail = remail)
        agencydata={'agencydata':agencdata}
        if request.method=="POST":
            agencdata.aaddress = request.POST.get('agencyadd')
            agencdata.astate = request.POST.get('agencystate')
            agencdata.apincode = request.POST.get('agencypincode')
            agencdata.mzerotofive = request.POST.get('malezerotofive')
            agencdata.mfivetoten = request.POST.get('malefivetoten')
            agencdata.mtentofifteen = request.POST.get('maletentofifteen')
            agencdata.mabovefifteen = request.POST.get('maleabovefifteen')
            agencdata.fzerotofive = request.POST.get('femalezerotofive')
            agencdata.ffivetoten = request.POST.get('femalefivetoten')
            agencdata.ftentofifteen = request.POST.get('femaletentofifteen')
            agencdata.fabovefifteen = request.POST.get('femaleabovefifteen')
            agencdata.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('agency_dashboard')
        return render(request,'agency/agency-dashboard.html',agencydata)
    else:
        messages.warning(request,"%s not registered as Agency"%remail)
        return redirect('home')


#Login View Function

def login(request):
    remail=request.user.email
    if agency_table.objects.filter(aemail=remail).exists():
        return redirect('agency_dashboard')
    else:
        return redirect('user_dashboard')

@login_required(login_url='home')
def acc_logout(request):
    logout(request)
    request.session.flush()
    return redirect('home')