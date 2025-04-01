from django.views import generic

from practice_app.models import Task


class HomePageView(generic.ListView):
    model = Task
    template_name = "practice/home-page.html"
