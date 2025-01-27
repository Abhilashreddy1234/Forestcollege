from django.shortcuts import render

# Home page view with breadcrumb
def home(request):
    breadcrumbs = [
        {"name": "Home", "url": "/"},
    ]
    return render(request, "home.html", {"breadcrumbs": breadcrumbs})

def about(request):
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "/about/"},
    ]
    return render(request, "about.html", {"breadcrumbs": breadcrumbs})

def vision(request):
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "/about/"},
        {"name": "Vision and Mission", "url": "/about/vision-and-mission/"},
    ]
    return render(request, "vision.html", {"breadcrumbs": breadcrumbs})

# Other views
def Governing_Board(request):
    return render(request, 'Governing_Board.html')

def Dean(request):
    return render(request, 'Dean.html')

def Joint_Director(request):
    return render(request, 'Joint-Director.html')

def Deputy_Director(request):
    return render(request, 'Deputy-Director.html')

def Organogram(request):
    return render(request, 'Organogram.html')

def Departments(request):
    return render(request, 'Departments.html')

def Faculty(request):
    return render(request, 'faculty.html')

def laboratory(request):
    return render(request, 'laboratory.html')

def StudentAchievements(request):
    return render(request, 'StudentAchievements.html')

def StudentAchievements1(request):
    return render(request, 'StudentAchievements1.html')

def womenprotection(request):
    return render(request, 'womenprotection.html')

def Antiragging(request):
    return render(request, 'womenprotection.html')

def AdmissionComitte(request):
    return render(request, 'womenprotection.html')

def DisciplinaryComitte(request):
    return render(request, 'womenprotection.html')

def Admissions1(request):
    return render(request, 'admissions1.html')

def AcademicSchedule(request):
    return render(request, 'AcdamicSchedule.html')

def AcademicNotification(request):
    return render(request, 'AdmissionNotification.html')

def Forestmuseum(request):
    return render(request, 'ForestMuseum.html')

def Cif(request):
    return render(request, 'cif.html')

def Boardroom(request):
    return render(request, 'Boardroom.html')

def Auditorium(request):
    return render(request, 'auditorium.html')

def Seminarhall(request):
    return render(request, 'seminarhall.html')

def Library(request):
    return render(request, 'Library.html')

def Fcri(request):
    return render(request, 'Fcri.html')

def Cfi2(request):
    return render(request, 'cf1.html')

def Nursery(request):
    return render(request, 'nursery.html')

def Workshop(request):
    return render(request, 'Workshop.html')

def ContactUs(request):
    return render(request, 'contactus.html')

def ResearchProjects(request):
    return render(request, 'ResearchProject.html')

def Mou(request):
    return render(request, 'mou.html')

def Publications(request):
    return render(request, 'publications.html')

def Awards(request):
    return render(request, 'awards.html')
