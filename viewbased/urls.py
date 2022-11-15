"""viewbased URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display',views.display),
    path('add_books', views.add_books),
    path('show', views.show),
    path('show_books', views.show_books, name='show_books'),
    path('delete_book/<int:id>', views.delete_book, name='delete'),
    path('create_books', views.create_data, name='create_books'),
    path('edit-book/<int:id>', views.edit_book, name='edit'),
]
