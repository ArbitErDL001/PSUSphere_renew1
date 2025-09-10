from django.urls import path
from . import views
from studentorg.views import HomePageView, OrganizationList

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Use the class-based view
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),  # Added trailing slash
]
