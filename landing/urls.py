from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("user/", views.user_list, name="user_list"),
    path("create_user/", views.create_profile, name="create_profile"),
]
