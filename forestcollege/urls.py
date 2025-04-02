from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from forestcollege import views
from .views import home1
from .views import contact_view

urlpatterns = [
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('vision/', views.vision, name='vision'),
    path('Governing_Board/',views.Governing_Board,name='Governing_Board'),
    path('Academic_counsil/',views.Academic_counsil,name='Academic_counsil'),
    path('Dean/',views.Dean,name='Dean'),
    path('Joint_Director/',views.Joint_Director,name='Joint_Director'),
    path('Deputy_Director/',views.Deputy_Director,name='Deputy_Director'),
    path('Organogram/',views.Organogram,name='Organogram'),
    path('Departments/',views.Departments,name="Departments"),
    path('DepartmentHead/',views.DepartmentHead,name="DepartmentHead"),
    path('laboratories/',views.laboratories,name="laboratories"),
    path('StudentAchievements/',views.StudentAchievements,name="StudentAchievements"),
    path('StudentAchievements1/',views.StudentAchievements1,name="StudentAchievements1"),
    path('womenprotection/',views.womenprotection,name='womenprotection'),
    path('Antiragging/',views.Antiragging,name='Antiragging'),
    path('Redressal/',views.Redressal,name="Redressal"),
    path('ethics/',views.EthicComitte,name='ethics'),
    path('AdmissionComitte/',views.AdmissionComitte,name='AdmissionComitte'),
    path('DisciplinaryComitte/',views.DisciplinaryComitte,name='DisciplinaryComitte'),
    path('admissions1/',views.Admissions1,name='admissions1'),
    path('mscforestry/',views.Mscforestry, name='mscforestry'),
    path('Phdforestry/',views.Phdforestry, name='Phdforestry'),
    path('AcademicSchedule/',views.AcademicSchedule,name='AcademicSchedule'),
    path('AcademicNotification/',views.AcademicNotification,name='AcademicNotification'),
    path('Forestmuseum/',views.Forestmuseum,name='Forestmuseum'),
    path('cif/',views.Cif,name='Cif'),
    path('Boardroom/',views.Boardroom,name='Boardroom'),
    path('auditorium/',views.Auditorium,name='Auditorium'),
    path('seminarhall/',views.Seminarhall,name='Seminarhall'),
    path('hostel/',views.hostel,name='hostel'),
    path('canteen/',views.canteen,name='canteen'),
    path('Library/',views.Library,name='Library'),
    path('Fcri/',views.Fcri,name='Fcri'),
    path('fcricarers/',views.Fcricarers,name='fcricarers'),
    path('Cfi2/',views.Cfi2,name='Cfi2'),
    path('Nursery/',views.Nursery,name='Nursery'),
    path('Workshop/',views.Workshop,name='Workshop'),
    path('Wif/',views.Wif,name='Wif'),
    path('ContactUs/',views.ContactUs,name='ContactUs'),
    path('Resaarch/',views.ResearchProjects,name='ResearchProjects'),
    path('Mou/',views.Mou,name='Mou'),
    path('Publications/',views.Publications,name='Publications'),
    path('Awards/',views.Awards,name='Awards'),
    path('Blog/',views.Blog,name="Blog"),
    path('PhotoGallary/',views.PhotoGallary,name='PhotoGallary'),
    path('pressrelease/',views.PressRelease,name="pressrelease"),
    path('fcri_news',views.Fcri_news,name='fcri_news'),
    path('videogallary/',views.VideoGallary,name='videogallary'),
    path('contact/', views.contact_view, name='contact'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('health-check/', views.health_check, name='health_check'),
    path("", home1, name="home1"),
    path('', include('cms.urls')),
    path('', contact_view, name='contact1'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
