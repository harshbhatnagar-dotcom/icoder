from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.models import Post
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        

        
        messages.success(request, "Your message has been sent successfully. We will get back to you soon!")
        

    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET.get('search')
    if len(query) >78:
        allposts=Post.objects.none()
    else:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsAdd=Post.objects.filter(content__icontains=query)
        allposts = allpostsTitle.union(allpostsAdd)


    if allposts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")

    params={
        "allposts":allposts,
        "query": query
    }

    return render(request, 'home/search.html',params)

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        conf_password=request.POST.get("pass2")


        if len(username)>10:
            messages.error(request,"username must be under 10 characters")
            return redirect("home")
        
        if password != conf_password:
            messages.error(request,"Password not match")
            return redirect("home")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return redirect("home")


        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname

        myuser.save()
        messages.success(request,"Your Account has been Succesfully Created")
        return redirect("home")



    else:
        return HttpResponse("Not Found")
    
def handlelogin(request):
    if request.method=="POST":
        loginuser=request.POST.get("username")
        loginpass=request.POST.get("password")

        user=authenticate(username=loginuser,password=loginpass)
        
        if user is not None:
            login(request,user)
            messages.success(request,"successfully Logged In")
            return redirect('home')
        
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('home')
        
    else:
        return HttpResponse("Chal bhag")



def handlelogout(request):
    
        logout(request)
        messages.success(request,"Logout Succesfully")
        return redirect('home')

    


