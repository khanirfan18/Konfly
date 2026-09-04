from django.shortcuts import render
from .models import EventsModel
from django.views.generic.base import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "events/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = EventsModel.objects.all()
        filter_events = events.order_by("date")[:3]
        context["events"] = filter_events

        return context

   