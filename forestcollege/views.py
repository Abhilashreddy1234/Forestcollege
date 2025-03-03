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
        {"name": "About"},
        {"name": "vision"},
    ]
    return render(request, "vision.html", {"breadcrumbs": breadcrumbs})

# Other views
def Governing_Board(request):
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "/about/"},
        {"name": "Governing Board", "url": "/about/vision/Governing_Board/"},
    ]
    return render(request, 'Governing_Board.html', {"breadcrumbs": breadcrumbs})

def Dean(request):
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name":"Administration",},
        {"name":"Dean"},
    ]
    return render(request, 'Dean.html',{"breadcrumbs": breadcrumbs})

def Joint_Director(request):
    breadcrumbs = [
        {"name": "Home", "url":"/"},
        {"name":"Administraation"},
        {"name":"Joint Director"},
    ]
    return render(request, 'joint-Director.html',{"breadcrumbs": breadcrumbs})

def Deputy_Director(request):
    breadcrumbs = [
        {"name": "Home", "url":"/"},
        {"name":"Administraation"},
        {"name":"Deputy Director"},
    ]

    return render(request, 'Deputy-Director.html',{"breadcrumbs": breadcrumbs})

def Organogram(request):
    breadcrumbs = [
        {"name":"Home","url":"/"},
        {"name":"Administration"},
        {"name":"Organogram"},
    ]
    return render(request, 'Organogram.html',{"breadcrumbs":breadcrumbs})

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
