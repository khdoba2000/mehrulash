from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.

from .models import Post, Image, ImageAlbum
from .owner import OwnedListView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import CreateForm
from django.forms import modelformset_factory

class post_list(ListView):
    model=Post
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(post_list, self).get_context_data(**kwargs)
        context['region_list'] = posts.models.region_options
        context['section_list'] = posts.models.section_options
        context['searched'] = False
        return context
    
class post_filter_mixed_list(ListView):
    model=Post
    paginate_by = 10

    def get_queryset(self):
        filter_sec_val = self.request.GET.get('section', 'child_dress')
        filter_reg_val  = self.request.GET.get('region', 'Tashkent')

        order = self.request.GET.get('orderby', '-created_at')
        if filter_reg_val=="any":
            context_by_reg = Post.objects.all()
        else:
            context_by_reg = Post.objects.filter(region=filter_reg_val)
        if filter_sec_val=="any":
            new_context = context_by_reg.order_by(order)
        else:
            new_context = context_by_reg.filter(section=filter_sec_val).order_by(order)
        
        return new_context

    def get_context_data(self, **kwargs):
        context = super(post_filter_mixed_list, self).get_context_data(**kwargs)
        context['region'] = self.request.GET.get('region', 'default')
        context['section'] = self.request.GET.get('section', 'give-default-value')
        context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
        context['region_list'] = posts.models.region_options
        context['section_list'] = posts.models.section_options
        context['searched'] = True
        return context

class post_owned_list(OwnedListView):
    model=Post
    template_name="posts/post_owned_list.html"

class post_detail(DetailView):
    model=Post

class post_create(LoginRequiredMixin, View):
    success_url=reverse_lazy('posts:post_list') 

    def get(self, request, pk=None):
        ImageFormSet = modelformset_factory(Image, fields=('image', ), extra=4)
        form = CreateForm()
        formset = ImageFormSet(queryset=Image.objects.none())

        ctx = {'form': form,
              'formset': formset}
        return render(request, "posts/post_form.html", ctx)
        
        
    def post(self, request, pk=None):
        ImageFormSet = modelformset_factory(Image, fields=('image', ), extra=4)
        form = CreateForm(request.POST, request.FILES or None)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        if not form.is_valid() or not formset.is_valid():
            print(f"Form Valid:{form.is_valid()} Formset valid:{formset.is_valid()}")
            ctx = {'form': form,
                    'formset': formset}
            return render(request, "posts/post_form.html", ctx)
        post_obj=form.save(commit=False)
        post_obj.owner=self.request.user
        album = ImageAlbum()
        post_obj.album=album    

        print(f"Formset is {formset}")

        for f in formset:
            try:
                print(f"f is {f}")
                try:
                    photo = Image(image=f.cleaned_data['image'] , album=album)
                except Exception as e:
                    continue
                album.save()
                print("album saved")
                post_obj.save()
                photo.save()
                print("photo saved")
            
            except Exception as e:
                album.delete()
                ctx = {'form': form,
                    'formset': formset,
                    'message': "Xatolik, iltimos qaytadan urunib ko'ring!"}
                return render(request, "posts/post_form.html", ctx)
                
        return redirect(self.success_url)

       


class post_delete(OwnerDeleteView):
    model=Post
    success_url=reverse_lazy('posts:post_owned_list') 


class post_update(OwnerUpdateView):
    success_url=reverse_lazy('posts:post_list') 

    def get(self, request, pk):
        ImageFormSet = modelformset_factory(Image, fields=('image', ), extra=4)
        post=get_object_or_404(Post, id=pk, owner=self.request.user)
        formset = ImageFormSet(queryset=post.album.images.all())

        form=CreateForm(instance=post)
        ctx = {'form': form,
              'formset': formset} 
        return render(request, "posts/post_form.html", ctx)
        
        
    def post(self, request, pk=None):
        ImageFormSet = modelformset_factory(Image, fields=('image', ), extra=4)
        post=get_object_or_404(Post, id=pk, owner=self.request.user)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        form = CreateForm(request.POST, request.FILES  or None, instance=post)
        if not form.is_valid() or not formset.is_valid():
            ctx = {'form': form,
                   'formset': formset} 
            return render(request, "posts/post_form.html", ctx)
        post_obj=form.save(commit=False)
        album = ImageAlbum()
        post_obj.album=album
        for f in formset:
            try:
                print(f"f is {f}")
                try:
                    photo = Image(image=f.cleaned_data['image'] , album=album)
                except Exception as e:
                    continue
                album.save()
                print("album saved")
                post_obj.save()
                photo.save()
                print("photo saved")
            
            except Exception as e:
                album.delete()
                ctx = {'form': form,
                    'formset': formset,
                    'message': "Xatolik, iltimos qaytadan urunib ko'ring!"}
                return render(request, "posts/post_form.html", ctx)
                
        return redirect(self.success_url)



from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
import posts


def stream_file(request, pk):
    post = get_object_or_404(Post, id=pk)
    response = HttpResponse()
    response['Content-Type'] = post.content_type
    response['Content-Length'] = len(post.picture)
    response.write(post.picture)
    return response