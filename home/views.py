from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    views = {}
    # ORM -> Object Relational Mapping
    views['services'] = Services.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    return render(request, 'index.html', views)


def about(request):
    views = {}
    views['feedbacks'] = Feedback.objects.all()
    return render(request, 'about.html', views)


def contact(request):
    views = {}
    views['informations'] = Information.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if Contact.objects.filter(email=email).exists():
            messages.error(
                request, "Email already exist, Please choose unique email!")
        else:
            data = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            data.save()
            messages.success(
                request, "Thank you for contacting us, Please visit again.")
    return render(request, 'contact.html', views)


def portfolio(request):

    return render(request, 'portfolio.html')


def services(request):
    views = {}
    views['services'] = Services.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    return render(request, 'services.html', views)


def newsletter(request):
    if request.method == "POST":
        email = request.POST['email']
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'This Email is already submitted!')
        else:
            data = Newsletter.objects.create(
                email=email
            )
            data.save()
            messages.success(request, 'Thanks for submitting your Email!')
    return redirect('/')


def handleSignup(request):
    if request.method == "POST":
        # Get the request parameter
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # Check for errorneous inputs
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(
                request, "Username must be under 10 characters")
            return redirect('home')

        # username should be alphanumeric
        if not username.isalnum():
            messages.error(
                request, "Username should only contain letters and numbers")
            return redirect('home')

        # passwords should  match
        if password != cpassword:
            messages.error(
                request, "Passwords do not match!")
            # return redirect('home')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken!')
            # return render('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already registered!')
            # return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, "Your account has been successfully created!")
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,
                            password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "You are Successfully Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again.")
            return redirect('home')

    return HttpResponse('404 - Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request, "You are Successfully Logged out!")
    return redirect('home')

def bloghome(request):
    
    return render(request, 'blog-home.html')


def blogsingle(request):


    return render(request, 'blog-single.html')
