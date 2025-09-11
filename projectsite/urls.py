"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from studentorg.views import (
    OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView,
)

urlpatterns = [
    path("organization_list", OrganizationList.as_view(), name="organization-list"),
    path("organization_list/add", OrganizationCreateView.as_view(), name="organization-add"),
    path("organization_list/<pk>", OrganizationUpdateView.as_view(), name="organization-update"),
    path("organization_list/<pk>/delete", OrganizationDeleteView.as_view(), name="organization-delete"),

    path("students", StudentList.as_view(), name="student-list"),
    path("students/add", StudentCreateView.as_view(), name="student-add"),
    path("students/<pk>", StudentUpdateView.as_view(), name="student-update"),
    path("students/<pk>/delete", StudentDeleteView.as_view(), name="student-delete"),
]
