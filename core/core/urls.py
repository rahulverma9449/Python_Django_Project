"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.core.mail import send_mail
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
path('', home, name='home'),
path('receipes/', receipes, name='receipes' ),
path('contact/', contact, name='contact'),
path('about/', about, name='about'),

# Login Page
path('login/', login_page, name='login'),
# Logout_page
path('logout/', logout_page, name='logout_page'),

# Register Page
path('register/', register, name='register'),




path('delete-receipe/<id>/', delete_receipe, name='delete_receipe'),
path('update-receipe/<slug>/', update_receipe, name='update_receipe'),

path('success-page/', success_page, name='success_page'),
path('students/', get_students, name='get_students'),
    
path('students/see_marks/<student_id>' , see_marks, name='see_marks'),
path('send_email/', send_mail, name='send_email'),
    
    
    
    # path('seed_db/,', seed_db, name='seed_db'),
    # path('StudentID/', StudentID, name='StudentID'),
    # path('Student/', Student, name='Student'),
 

path('admin/', admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

