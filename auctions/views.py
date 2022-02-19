# Wishlist
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from .models import User,Listing,Bids,Comment,Wishlist
from django.contrib.auth.decorators import login_required

def index(request):
    f=Listing.objects.filter(active=0)
    d="Active Listing"
    return render(request, "auctions/index.html",{ "items" : f,"d":d })

def category(request):
    return render(request, "auctions/category.html")

@login_required
def wishlist(request):
    f=Wishlist.objects.filter(user=request.user)
    f=f.filter(wishlist=True)
    l=[]
    for i in f:
        l.append(i.item)
    d="Wishlist"
    return render(request, "auctions/index.html",{ "items" : l ,"d":d})

def SpecificCategory(request,name):
    f=Listing.objects.filter(category=name)
    d=name
    return render(request, "auctions/index.html",{ "items" : f,"d":d })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

class newlisting(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['Title','Description','Base_Price','Image_URL','category']
        

@login_required
def create(request):
    context ={} 
  
    # create object of form 
    form = newlisting(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid():
        your_object = form.save(commit=False)
        your_object.user = request.user
        your_object.save()
        # return redirect('your_success_url')
        # save the form data to model 
        # form.save() 
        return HttpResponseRedirect(reverse("index"))
    context['form']= form 
    return render(request, "auctions/create.html", context) 

def activetoun(request,itemid):
    if request.method =='POST':
        item=Listing.objects.get(pk=itemid)
        item.active=1
        item.save()
    return HttpResponseRedirect(reverse("index"))

def item(request,itemid):
    try:
        item=Listing.objects.get(pk=itemid)
    except:
        return HttpResponse("<h1>This page does not exist</h1>")
    if item.active==1:
        n=Bids.objects.filter(item=item)[0]
        n=n.user.username
        if(n==request.user.username):
            n="you"
        return render(request, "auctions/late.html",{"n":n})
    error=""
    if request.method=='POST' and 'bid' in request.POST:
        bid=int(request.POST["Bid"])
        item=Listing.objects.get(pk=itemid)
        if bid>item.Base_Price:
            t=item.noofbids+1
            item.noofbids=t
            item.Base_Price=bid
            item.save()
            Bids(user=request.user, bids=bid,item=item).save()
            error="Bid has been placed"
        else:
            error="You are poor to place a bid"
    
    if request.method=='POST' and 'commentt' in request.POST:
        Comment(user=request.user, comment=request.POST['comment'],item=item).save()

    if request.method=='POST' and 'add' in request.POST:
        try:
            wi=Wishlist.objects.filter(user=request.user)
            wi=wi.get(item=item)
            if wi.wishlist==True:
                wi.wishlist=False
            else:
                wi.wishlist=True
            wi.save()
        except:
            Wishlist(user=request.user,wishlist=True,item=item).save()
            
    item=Listing.objects.get(pk=itemid)
    comments=Comment.objects.filter(item=item)
    a=0
    if request.user==item.user:
        a=1
    w="Add to wishlist"
    try:
        wi=Wishlist.objects.filter(user=request.user)
        wi=wi.get(item=item)
        if wi.wishlist==True:
            w="Remove from wishlist"
    except:
        pass
    return render(request, "auctions/item.html",{"item":item,"error":error,"a":a,"comments":comments,"w":w})
