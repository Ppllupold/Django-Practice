from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from practice_app.forms import TaskForm
from practice_app.models import Task, Tag


class HomePageView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "practice/home-page.html"
    queryset = Task.objects.all().order_by("is_done", "-created_at")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "practice/task_form.html"
    success_url = reverse_lazy("practice:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "practice/task_form.html"
    success_url = reverse_lazy("practice:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "practice/task_confirm_delete.html"
    success_url = reverse_lazy("practice:index")


class CompletionTaskView(generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("practice:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "practice/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    template_name = "practice/tag_form.html"
    success_url = reverse_lazy("practice:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "practice/tag_form.html"
    success_url = reverse_lazy("practice:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "practice/tag_confirm_delete.html"
    success_url = reverse_lazy("practice:tag-list")
