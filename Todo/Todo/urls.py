"""
URL configuration for Todo project.

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
from django.urls import path
from main.views import *
# here'*' means all modules in views.py can be accessed here

urlpatterns = [#this url path is directed to 'views.py' inorder to work the functions in that file
    path('admin/', admin.site.urls),
    path('',home,name='home'),#empty string coz we want to open the function in that path
    path('add_task',add_task,name='add_task'),#this url or route goes to views file then work the function 'add_task'
    path('mark_as_done/<int:task_id>/',mark_as_done,name='mark_as_done'),
    path('mark_as_undone/<int:task_id>/',mark_as_undone,name='mark_as_undone'),
    path('update/<int:update_id>/',update_task,name='update_task'),
    path('delete/<int:delete_id>/',delete_task,name='delete_task')
]
