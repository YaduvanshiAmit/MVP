from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404, request

# Create your views here.
# Model -> View -> Template
# Model -> View -> Reacj.js/ vue.js

from .forms import EmailEntryForm ,EmailEntryUpdateForm
from .models import EmailEntry

# html_str = "<!doctype html><html></html>"

# create a function what model i used then wht function i allowed
# @login_required(login_url="/login")
# @staff_member_required(login_url="/login")

def email_entry_get_view(request,id=None,*arge,**kwargs):
    # get a single item stored in the database
    print (arge,kwargs)
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404    
    #return HttpResponse(f"<h1>Hello {obj.email}</h1>")
    return render(request,"emails/detail.html",{"object": obj})



# def email_entry_create_view():

def email_entry_create_view(request,*args,**kwargs):
    context = {}
    if request.user.is_authenticated:
        context['some_cool_stuff'] = "Whatever"

    print(request.user , request.user.is_authenticated)

    # if request.method == "POST":
    #     DONT DO THIS!

    #    print(dict (request.POST))
    #    data = dict(request.POST)
    #    try:
    #        del data ['csrfmiddlewaretoken']
    #   except:
    #       pass
    #   obj = EmailEntry(**data)
    #   obj.save()    

    form = EmailEntryForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        obj = form.save(commit=False)
        #obj.name = "Amit"
        obj.save()
        form = EmailEntryForm()
        context['added'] = True
        context['form'] = form
    return render (request, "home.html" ,context)    
    #return render (request, "form.html" ,{"form": form})




# def email_entry_update_view():
@staff_member_required(login_url="/login")
def email_entry_update_view(request,id=None,*arge,**kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404

    form = EmailEntryUpdateForm (request.POST or None, instance=obj)
    if form.is_valid():
        updated_obj = form.save()
        return redirect(f"/email/{updated_obj.id}")
    return render (request,"emails/update.html",{'object': obj,"form": form})          
        






# def email_entry_list_view():

@staff_member_required(login_url="/login")
def email_entry_list_view(request,id=None,*arge,**kwargs):
    # get a single item stored in the database
    print (arge,kwargs)
    qs = EmailEntry.objects.all() # .filter(email__icontains='abc')   
    #return HttpResponse(f"<h1>Hello {obj.email}</h1>")
    return render(request,"emails/list.html",{"object_list": qs})







# def email_entry_destroy_view():

@staff_member_required(login_url="/login")

def email_entry_destroy_view(request,id=None,*arge,**kwargs):
    # get a single item stored in the database
    print (arge,kwargs)
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404

    if request.method == "POST":
        obj.delete()
        return redirect("/")      
    #return HttpResponse(f"<h1>Hello {obj.email}</h1>")
    return render(request,"emails/destroy.html",{"object": obj})