from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import EmailSubscriptionForm
import requests
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm  # Correct import
from django import forms
from django.core.exceptions import ValidationError
import re
 
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
# views.py
# views.py

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Create form instance
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Sending email to admin
            subject = f"New Contact Form Submission from {name}"
            message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            recipient_email = '20eg110119@anurag.edu.in'  # Change this to your email

            try:
                send_mail(subject, message_body, email, [recipient_email], fail_silently=False)
                
                # Send confirmation email to user
                user_subject = "Thank you for contacting us!"
                user_message = f"Hi {name},\n\nThank you for reaching out. We have received your message and will get back to you soon.\n\nBest regards,\nYour Team"
                send_mail(user_subject, user_message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

                return redirect('contact_success')  # Redirect after successful form submission
            except Exception as e:
                print(f"Error sending email: {e}")
                return HttpResponse("An error occurred while sending the email. Please try again later.")
        else:
            return render(request, 'contactus.html', {'form': form})  # Return form with errors if not valid
    else:
        form = ContactForm()  # Create empty form for GET request
        return render(request, 'contactus.html', {'form': form})



def contact_success(request):
    return render(request, 'contact_success.html')


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
        {"name":"FCRI Cares"},
    ]
    return render(request, 'fcri.html',{"breadcrumbs":breadcrumbs,"form":form})
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
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Contact Us"},
    ]
    return render(request, 'contactus.html',{"breadcrumbs":breadcrumbs,"form":form})

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


def Fcri_news(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Media"},
        {"name":"Fcri News"},
    ]    
    return render(request, 'fcri_news.html',{"breadcrumbs":breadcrumbs,"form":form})


def VideoGallary(request):
    form = EmailSubscriptionForm()
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Media"},
        {"name":"video Gallary"},
    ]    
    return render(request, 'videogallary.html',{"breadcrumbs":breadcrumbs,"form":form})


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValidationError('Name should only contain letters and spaces.')
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\d{10}$', phone):
            raise ValidationError('Phone number should be exactly 10 digits.')
        return phone
