from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.

from .models import Post
from .owner import OwnedListView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import CreateForm

class post_list(ListView):
    model=Post

class post_owned_list(OwnedListView):
    model=Post
    template_name="posts/post_owned_list.html"

class post_detail(DetailView):
    model=Post

class post_create(LoginRequiredMixin, View):
    success_url=reverse_lazy('posts:post_list') 

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, "posts/post_form.html", ctx)
        
        
    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, "posts/post_form.html", ctx)
        object=form.save(commit=False)
        object.owner=self.request.user
        object.save()
        return redirect(self.success_url)


class post_delete(OwnerDeleteView):
    model=Post
    success_url=reverse_lazy('posts:post_list') 


class post_update(OwnerUpdateView):
    success_url=reverse_lazy('posts:post_list') 

    def get(self, request, pk):
        post=get_object_or_404(Post, id=pk, owner=self.request.user)
        form=CreateForm(instance=post)
        ctx = {'form': form}
        return render(request, "posts/post_form.html", ctx)
        
        
    def post(self, request, pk=None):
        post=get_object_or_404(Post, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES  or None, instance=post)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, "posts/post_form.html", ctx)
        object=form.save()
        object.save()
        return redirect(self.success_url)



from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError


def stream_file(request, pk):
    post = get_object_or_404(Post, id=pk)
    response = HttpResponse()
    response['Content-Type'] = post.content_type
    response['Content-Length'] = len(post.picture)
    response.write(post.picture)
    return response