from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from forestcollege import views

urlpatterns = [
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('admin/', admin.site.urls),
    path('vision/', views.vision, name='vision'),
    path('Governing_Board/',views.Governing_Board,name='Governing_Board'),
    path('Dean/',views.Dean,name='Dean'),
    path('Joint_Director/',views.Joint_Director,name='Joint_Director'),
    path('Deputy_Director/',views.Deputy_Director,name='Deputy_Director'),
    path('Organogram/',views.Organogram,name='Organogram'),
    path('', include('cms.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
