
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post

class OwnedListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerCreateView(LoginRequiredMixin, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['owner'] = 1#user
        return ctx 
    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    
    def get_queryset(self):
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    
    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)
