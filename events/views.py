from django.shortcuts import render
from .models import EventsModel
from django.views.generic import ListView,DetailView,TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "events/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = EventsModel.objects.all()
        filter_events = events.order_by("date")[:3]
        context["events"] = filter_events

        return context


class EventList(ListView):
    template_name = "events/explore.html"
    model = EventsModel
    context_object_name = "events"



class EventDetails(DetailView):
    model = EventsModel
    template_name = "events/event-detail.html"
    context_object_name = "event"

