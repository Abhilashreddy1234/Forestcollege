from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import EmailSubscriptionForm
import requests
from django.conf import settings

from django.contrib import messages

def health_check(request):
    return JsonResponse({'status': 'ok'})

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
    return render(request, 'Joint-Director.html',{"breadcrumbs": breadcrumbs,"form":form})

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
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Departments"},
        {"name":"List of Departments"},
    ]
    return render(request, 'departments.html',{"breadcrumbs":breadcrumbs,"form":form})
def DepartmentHead(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Departments"},
        {"name":"DepartmentHead"},
        
    ]
    return render(request,'DepartmentHead.html',{"breadcrumbs":breadcrumbs,"form":form})
def Faculty(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Departments"},
        {"name":"Faculty"},
    ]
    
    return render(request, 'faculty.html',{"breadcrumbs":breadcrumbs})
def laboratories(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Departments"},
        {"name":"laboratories"},
    ]
    
    return render(request, 'laboratories.html',{"breadcrumbs":breadcrumbs,"form":form})
def StudentAchievements(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"StudentAchievements"},
        {"name":"year of 2016"},
        
    ]
    return render(request, 'studentAchievements.html',{"breadcrumbs":breadcrumbs,"form":form})

def StudentAchievements1(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"StudentAchievements"},
        {"name":"year of 2017"},
        
    ]
    return render(request, 'StudentAchievements1.html',{"breadcrumbs":breadcrumbs,"form":form})

def womenprotection(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"WomenProtectionCommitee"},
    ]
    return render(request, 'womenprotection.html',{"breadcrumbs":breadcrumbs,"form":form})

def Antiragging(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"AntiraggingCommitee"},
    ]
    return render(request, 'womenprotection.html',{"breadcrumbs":breadcrumbs,"form":form})

def Redressal(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"Redressal of Grievance "},
    ]
    return render(request, 'Redressal.html',{"breadcrumbs":breadcrumbs,"form":form})

def EthicComitte(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"Institutional Ethic Comitte "},
    ]
    return render(request, 'Ethicscommitee.html',{"breadcrumbs":breadcrumbs,"form":form})
def AdmissionComitte(request):
    form = EmailSubscriptionForm()    
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"AdmissionComitte"},
    ]
    return render(request, 'AdmissionComitte.html',{"breadcrumbs":breadcrumbs,"form":form})

def DisciplinaryComitte(request):
    form = EmailSubscriptionForm() 
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Academics"},
        {"name":"Committes"},
        {"name":"DisciplinaryComitte"},
    ]
    
    return render(request, 'Disciplinary.html',{"breadcrumbs":breadcrumbs,"form":form})

def Admissions1(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":'/'},
        {"name":"Admissions"},
        {"name":"Courses Offered"},
         {"name":"B.sc Forestry"},
    ]
    return render(request, 'admissions1.html',{"breadcrumbs":breadcrumbs,"form":form})
def Mscforestry(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":'/'},
        {"name":"Admissions"},
        {"name":"Courses Offered"},
         {"name":"M.sc Forestry"},
    ]
    return render(request, 'mscforestry.html',{"breadcrumbs":breadcrumbs,"form":form})
def Phdforestry(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":'/'},
        {"name":"Admissions"},
        {"name":"Courses Offered"},
         {"name":"P.hd Forestry"},
    ]
    return render(request, 'phdforestry.html',{"breadcrumbs":breadcrumbs,"form":form})
def AcademicSchedule(request):
    return render(request, 'AcdamicSchedule.html')

def AcademicNotification(request):
    return render(request, 'AdmissionNotification.html')

def Forestmuseum(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"ForestMuseum"},
    ]
    return render(request, 'ForestMuseum.html',{"breadcrumbs":breadcrumbs,"form":form})

def Cif(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"CentralInstrumentationFaculty"},
    ]
    return render(request, 'cif.html',{"breadcrumbs":breadcrumbs,"form":form})

def Boardroom(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"Boardroom"},
    ]
    return render(request, 'Boardroom.html',{"breadcrumbs":breadcrumbs,"form":form})

def Auditorium(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"Auditorium"},
    ]
    return render(request, 'auditorium.html',{"breadcrumbs":breadcrumbs,"form":form})

def Seminarhall(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"SeminarHall"},
    ]
    return render(request, 'seminarhall.html',{"breadcrumbs":breadcrumbs,"form":form})

def Library(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"library"},
    ]
    return render(request, 'Library.html',{"breadcrumbs":breadcrumbs,"form":form})

def Fcri(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"FCRI Careers"},
    ]
    return render(request, 'Fcri.html',{"breadcrumbs":breadcrumbs,"form":form})
def Fcricarers(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"FCRI Study Circle"},
    ]
    return render(request, 'fcricircle.html',{"breadcrumbs":breadcrumbs,"form":form})
def hostel(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"hostel"},

    ]
    return render(request, 'hostel.html',{"breadcrumbs":breadcrumbs,"form":form})
def canteen(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Infrastructure"},
        {"name":"canteen"},

    ]
    return render(request,'canteen.html',{"breadcrumbs":breadcrumbs,"form":form})

def Cfi2(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"CFI"},
    ]

    return render(request, 'cif2.html',{"breadcrumbs":breadcrumbs,"form":form})

def Nursery(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"Nursery"},
    ]
    return render(request, 'nursery.html',{"breadcrumbs":breadcrumbs,"form":form})
def Wif(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"Wood Identificaftion Toolkit"},
    ]
    return render(request, 'wif.html',{"breadcrumbs":breadcrumbs,"form":form})
def Workshop(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Services"},
        {"name":"Workshop"},
    ]
    return render(request, 'Workshop.html',{"breadcrumbs":breadcrumbs,"form":form})
 
def ContactUs(request):
    return render(request, 'contactus.html')

def ResearchProjects(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Research"},
        {"name":"Research Projects"},
    ]
    return render(request, 'ResearchProject.html',{"breadcrumbs":breadcrumbs,"form":form})

def Mou(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Research"},
        {"name":"Mou"},
    ]
    return render(request, 'mou.html',{"breadcrumbs":breadcrumbs,"form":form})

def Publications(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Research"},
        {"name":"Publications"},
    ]
    return render(request, 'publications.html',{"breadcrumbs":breadcrumbs,"form":form})

def Awards(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Research"},
        {"name":"Awards"},
    ]    
    return render(request, 'awards.html',{"breadcrumbs":breadcrumbs,"form":form})

def Blog(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Media"},
        {"name":"Blog"},
    ]    
    return render(request, 'Blog.html',{"breadcrumbs":breadcrumbs,"form":form})

def PhotoGallary(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Media"},
        {"name":"Photogallary"},
    ]    
    return render(request, 'Photogallary.html',{"breadcrumbs":breadcrumbs,"form":form})

def PressRelease(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Media"},
        {"name":"Press Release"},
    ]    
    return render(request, 'Pressrelease.html',{"breadcrumbs":breadcrumbs,"form":form})

def VideoGallary(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Media"},
        {"name":"video Gallary"},
    ]    
    return render(request, 'videogallary.html',{"breadcrumbs":breadcrumbs,"form":form})
