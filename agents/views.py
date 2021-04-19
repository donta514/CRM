import random
from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrgAndLoginRequiredMixin

class AgentListView(OrgAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        org = self.request.user.userprofile
        return Agent.objects.filter(org=org)

class AgentCreateView(OrgAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_org = False
        user.set_password(f"{random.randint(0, 1000)}")
        user.save()
        Agent.objects.create(
            user=user,
            org=self.request.user.userprofile
        )
        send_mail(
            subject="You are invited to become an agent.",
            message="You were added as an agent on Dontá CRM. Please come login to start working.",
            from_email="admin@test.com",
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form) 
        # agent.org = self.request.user.userprofile
        # agent.save()

class AgentDetailView(OrgAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        org = self.request.user.userprofile
        return Agent.objects.filter(org=org)

class AgentUpdateView(OrgAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def get_queryset(self):
        return Agent.objects.all()

class AgentDeleteView(OrgAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        org = self.request.user.userprofile
        return Agent.objects.filter(org=org)

    def get_success_url(self):
        return reverse("agents:agent-list")

