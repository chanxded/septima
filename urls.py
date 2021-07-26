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
from django.urls import path
from mainapp import views

urlpatterns = [
	path('', views.Main.as_view(), name='Main'),
	path('services/', views.Services.as_view(), name='Services'),
	path('ysluga/', views.Ysluga.as_view(), name='Ysluga'),
    path('admin/', admin.site.urls),
    path('blog/', views.BlogListView.as_view(), name='home'),
    path('item/<int:pk>/', views.BlogDetailView.as_view(), name='Item_detail'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
