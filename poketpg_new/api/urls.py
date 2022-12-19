from django.urls import path ,include
from rest_framework import routers
#from . import UserViewSet
from . import views
 #router=routers.DefaultRouter()
#router.register('api/users',LeadViewSet)
urlpatterns = [
    path("get-hostler-list/",views.get_hostler_list, name="get-hostler-list"),
    path("get-owner-details/",views.get_owner_details,name="get-owner-details"),
    path("signup-owner/",views.signup_owner.as_view(),name="signup-owner"),
    path("signup-hostler/",views.signup_hostler.as_view(),name="signup-hostler"),
    path("get-owner-by-num/<str:pk>/",views.get_owner_by_num,name="get-owner-by-num"),
    path("get-hostler-by-num/<str:pk>/",views.get_hostler_by_num,name="get-hostler-by-num"),
    
    # path("form/",views.form,name="form"),
]
