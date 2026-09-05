from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomeView.as_view(), name="events"),
    path("explore/",views.EventList.as_view(),name="event-list"),
    path("explore/<slug:slug>",views.EventDetails.as_view(),name="event-detail" )
]