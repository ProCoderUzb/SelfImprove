from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home_page, name="home"),
    path("office/", view=views.office_page, name="office"),
    path("activities/", views.activites_page, name="acitivities")
]
