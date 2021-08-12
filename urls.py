"""septima URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include

from mainapp import views

urlpatterns = [
	path('', views.Main.as_view(), name='Main'),
    path('contacts/', views.Contacts.as_view(), name='Contacts'),
    path('about/', views.About.as_view(), name='About'),
    path('audit/', views.Audit.as_view(), name='Audit'),
	path('upravlenie-reputaciej/', views.Services.as_view(), name='Services'),
    path('digital/', views.Digital.as_view(), name='Digital'),
	path('upravlenie-reputaciej/analiz-infopolya/', views.Ysluga.as_view(), name='Ysluga'),
    path('upravlenie-reputaciej/analitika/', views.Analitika.as_view(), name='Analitika'),
    path('upravlenie-reputaciej/podderzhka/', views.Podderzhka.as_view(), name='Podderzhka'),
    path('admin/', admin.site.urls),
    path('blog/', views.BlogListView.as_view(), name='home'),


] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
