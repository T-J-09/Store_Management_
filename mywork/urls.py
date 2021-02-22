"""mywork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from stockmgmt import views

urlpatterns = [
    #path('stockmgmt/',include('stockmgmt.urls')),
    path('dp/',views.dt),
    path('home/',views.home,name='home'),
    path('list_item/',views.list_item,name='list_item'),
    path('add_item/',views.add_item,name='add_item'),
    path('update_item/<str:pk>/', views.update_item, name='update_item'),
    path('delete_item/<str:pk>/', views.delete_item, name="delete_item"),
    path('store_detail/<str:pk>/', views.store_detail, name="store_detail"),
    path('issue_item/<str:pk>/', views.issue_item, name="issue_item"),
    path('receive_item/<str:pk>/', views.receive_item, name="receive_item"),
    path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
    path('list_history/', views.list_history, name='list_history'),
    path('admin/',admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
]
