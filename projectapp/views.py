from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from projectapp.decorators import project_ownership_required
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse_lazy('projectapp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25
