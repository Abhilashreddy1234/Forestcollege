from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import EmailSubscriptionForm
import requests
from django.conf import settings

from django.contrib import messages
def home1(request):
    form = EmailSubscriptionForm()
    
    if request.method == "POST":
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Save email to database (uncomment if using a model)
            # Subscription.objects.create(email=email)

            return JsonResponse({"message": "Subscription successful!"}, status=200)  
        else:
            return JsonResponse({"error": "Invalid email address"}, status=400)

    return render(request, "home.html", {"form": form})


def contact_view(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get("g-recaptcha-response")
        data = {
            "secret": settings.RECAPTCHA_SECRET_KEY,
            "response": recaptcha_response,
        }
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
        result = r.json()

        if result["success"]:
            # Process the form data and send email
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            message = request.POST.get("message")

            # Example: Save to database or send email
            # Contact.objects.create(name=name, email=email, phone=phone, message=message)

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        else:
            messages.error(request, "Invalid reCAPTCHA. Please try again.")

    return render(request, "contact1.html")


# Home page view with breadcrumb
def home(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name": "Home", "url": "/"},
    ]
    return render(request, "home.html", {"breadcrumbs": breadcrumbs,"form":form})

def about(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "/about/"},
    ]
    return render(request, "about.html", {"breadcrumbs": breadcrumbs,"form":form})

def vision(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "/about/"},
        {"name": "Vision", "url": "/vision/"},
    ]
    return render(request, "vision.html", {"breadcrumbs": breadcrumbs,"form":form})

# Other views
def Governing_Board(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "/about/"},
        {"name": "Governing Board", "url": "/about/vision/Governing_Board/"},
    ]
    return render(request, 'Governing_Board.html', {"breadcrumbs": breadcrumbs,"form":form})
def Academic_counsil(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "/about/"},
        {"name": "Governing Board", "url": "/about/vision/Academic_counsil/"},

    ]
    return render(request, 'Academic_counsil.html', {"breadcrumbs": breadcrumbs,"form":form})
def Dean(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name":"Administration",},
        {"name":"Dean"},
    ]
    return render(request, 'Dean.html',{"breadcrumbs": breadcrumbs,"form":form})

def Joint_Director(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name": "Home", "url":"/"},
        {"name":"Administraation"},
        {"name":"Joint Director"},
    ]
    return render(request, 'joint-Director.html',{"breadcrumbs": breadcrumbs,"form":form})

def Deputy_Director(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name": "Home", "url":"/"},
        {"name":"Administraation"},
        {"name":"Deputy Director"},
    ]

    return render(request, 'Deputy-Director.html',{"breadcrumbs": breadcrumbs,"form":form})

def Organogram(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Administration"},
        {"name":"Organogram"},
    ]
    return render(request, 'Organogram.html',{"breadcrumbs":breadcrumbs,"form":form})

def Departments(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Departments"},
        {"name":"List of Departments"},
    ]
    return render(request, 'Departments.html',{"breadcrumbs":breadcrumbs})
def DepartmentHead(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Departments"},
        {"name":"DepartmentHead"},
        
    ]
    return render(request,'DepartmentHead.html',{"breadcrumbs":breadcrumbs})
def Faculty(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Departments"},
        {"name":"Faculty"},
    ]
    
    return render(request, 'faculty.html',{"breadcrumbs":breadcrumbs})

def StudentAchievements(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"StudentAchievements"},
        {"name":"year of 2016"},
        
    ]
    return render(request, 'StudentAchievements.html',{"breadcrumbs":breadcrumbs})

def StudentAchievements1(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"StudentAchievements"},
        {"name":"year of 2017"},
        
    ]
    return render(request, 'StudentAchievements1.html',{"breadcrumbs":breadcrumbs})

def womenprotection(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"WomenProtectionCommitee"},
    ]
    return render(request, 'womenprotection.html',{"breadcrumbs":breadcrumbs})

def Antiragging(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"AntiraggingCommitee"},
    ]
    return render(request, 'womenprotection.html',{"breadcrumbs":breadcrumbs})

def AdmissionComitte(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"AdmissionComitte"},
    ]
    return render(request, 'womenprotection.html',{"breadcrumbs":breadcrumbs})

def DisciplinaryComitte(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"DisciplinaryComitte"},
    ]
    
    return render(request, 'womenprotection.html')

def Admissions1(request):
    breadcrumbs = [
        {"name":"Home","url":'/'},
        {"name":"Admissions"},
        {"name":"Courses Offered"},
         {"name":"B.sc Hons Foresty"},
    ]
    return render(request, 'admissions1.html',{"breadcrumbs":breadcrumbs})

def AcademicSchedule(request):
    return render(request, 'AcdamicSchedule.html')

def AcademicNotification(request):
    return render(request, 'AdmissionNotification.html')

def Forestmuseum(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"ForestMuseum"},
    ]
    return render(request, 'ForestMuseum.html',{"breadcrumbs":breadcrumbs})

def Cif(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"CentralInstrumentationFaculty"},
    ]
    return render(request, 'cif.html',{"breadcrumbs":breadcrumbs})

def Boardroom(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"Boardroom"},
    ]
    return render(request, 'Boardroom.html',{"breadcrumbs":breadcrumbs})

def Auditorium(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"Auditorium"},
    ]
    return render(request, 'auditorium.html',{"breadcrumbs":breadcrumbs})

def Seminarhall(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"SeminarHall"},
    ]
    return render(request, 'seminarhall.html',{"breadcrumbs":breadcrumbs})

def Library(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"library"},
    ]
    return render(request, 'Library.html',{"breadcrumbs":breadcrumbs})

def Fcri(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"FCRI Careers"},
    ]
    return render(request, 'Fcri.html',{"breadcrumbs":breadcrumbs})

def Cfi2(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"CFI"},
    ]

    return render(request, 'cf1.html',{"breadcrumbs":breadcrumbs})

def Nursery(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"Nursery"},
    ]
    return render(request, 'nursery.html',{"breadcrumbs":breadcrumbs})

def Workshop(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"Workshop"},
    ]
    return render(request, 'Workshop.html',{"breadcrumbs":breadcrumbs})
 
def ContactUs(request):
    return render(request, 'contactus.html')

def ResearchProjects(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Research"},
        {"name":"Research Projects"},
    ]
    return render(request, 'ResearchProject.html',{"breadcrumbs":breadcrumbs})

def Mou(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Research"},
        {"name":"Mou"},
    ]
    return render(request, 'mou.html',{"breadcrumbs":breadcrumbs})

def Publications(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Research"},
        {"name":"Publications"},
    ]
    return render(request, 'publications.html',{"breadcrumbs":breadcrumbs})

def Awards(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Research"},
        {"name":"Awards"},
    ]    
    return render(request, 'awards.html',{"breadcrumbs":breadcrumbs})
