from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from forestcollege import views

urlpatterns = [
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('vision/', views.vision, name='vision'),
    path('Governing_Board/',views.Governing_Board,name='Governing_Board'),
    path('Dean/',views.Dean,name='Dean'),
    path('Joint_Director/',views.Joint_Director,name='Joint_Director'),
    path('Deputy_Director/',views.Deputy_Director,name='Deputy_Director'),
    path('Organogram/',views.Organogram,name='Organogram'),
    path('Departments/',views.Departments,name="Departments"),
    path('DepartmentHead/',views.DepartmentHead,name="DepartmentHead"),
    path('StudentAchievements/',views.StudentAchievements,name="StudentAchievements"),
    path('StudentAchievements1/',views.StudentAchievements1,name="StudentAchievements1"),
    path('womenprotection/',views.womenprotection,name='womenprotection'),
    path('Antiragging/',views.Antiragging,name='Antiragging'),
    path('AdmissionComitte/',views.AdmissionComitte,name='AdmissionComitte'),
    path('DisciplinaryComitte/',views.DisciplinaryComitte,name='DisciplinaryComitte'),
    path('admissions1/',views.Admissions1,name='admissions1'),
    path('AcademicSchedule/',views.AcademicSchedule,name='AcademicSchedule'),
    path('AcademicNotification/',views.AcademicNotification,name='AcademicNotification'),
    path('Forestmuseum/',views.Forestmuseum,name='Forestmuseum'),
    path('cif/',views.Cif,name='Cif'),
    path('Boardroom/',views.Boardroom,name='Boardroom'),
    path('auditorium/',views.Auditorium,name='Auditorium'),
    path('seminarhall/',views.Seminarhall,name='Seminarhall'),
    path('Library/',views.Library,name='Library'),
    path('fcri/',views.Fcri,name='Fcri'),
    path('Cfi2/',views.Cfi2,name='Cfi2'),
    path('Nursery/',views.Nursery,name='Nursery'),
    path('Workshop/',views.Workshop,name='Workshop'),
    path('ContactUs/',views.ContactUs,name='ContactUs'),
    path('Resaarch/',views.ResearchProjects,name='ResearchProjects'),
    path('Mou/',views.Mou,name='Mou'),
    path('Publications/',views.Publications,name='Publications'),
    path('Awards/',views.Awards,name='Awards'),
    path('', include('cms.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
