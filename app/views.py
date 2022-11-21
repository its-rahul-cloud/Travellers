from django.contrib.auth import forms
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import  ProfileRegistrationForm,ProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
import sys
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import *
from django.contrib.auth import login
from translate import Translator
def is_users(post_user, logged_user):
    return post_user == logged_user


class  HomeListView(ListView):
    
    model=House
    template_name='app/index.html'
    context_object_name='home'
    paginate_by=5

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        home = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(home, self.paginate_by)
        try:
            home = paginator.page(page)
        except PageNotAnInteger:
            home = paginator.page(1)
        except EmptyPage:
            home = paginator.page(paginator.num_pages)
        context['home'] = home
        return context

class TravellerListView(ListView):
    model=Traveller
    template_name='app/travellerlist.html'
    context_object_name='travellers'

class HomeDetailView(LoginRequiredMixin,DetailView):
    model = House
    template_name = 'app/housedetail.html'
    context_object_name = 'house_d'


class ProfileRegistrationView(View):
    def get(self, request):
        form = ProfileRegistrationForm()
        return render(request, "app/profileregistration.html", {"form": form})

    def post(self, request):
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registration Completed !")
            user=form.save()
            login(request,user)
        return redirect('home')

class ProfileDetailView(LoginRequiredMixin,View):

    def get(self,request,pk):
        us =User.objects.get(id=pk)
        profile = Traveller.objects.get(user =us)
        if profile :
            context = {"profile":profile}
            return render(request ,'app/profile.html',context)
        else:
            return redirect('profile_update')



class ProfileUpdateView(LoginRequiredMixin,View):
 
    def get(self,request,pk):
        obj = Traveller.objects.get(pk=pk)
        form = ProfileForm(instance=obj)
        obj = Traveller.objects.get(pk=pk)
        return render(request,'app/profileupdate.html', {"form": form, "acitve": "btn-primary","obj":obj}) 

    def post(self, request,pk):
        obj = Traveller.objects.get(pk=pk)
        form =ProfileForm(request.POST,request.FILES,instance=obj)

        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            contanct_no = form.cleaned_data["contanct_no"]
            image=form.cleaned_data["image"]
            verification=form.cleaned_data["verification"]

            reg = Traveller(
                id=pk,
                user=user,
                name=name,
                contanct_no=contanct_no,
                image=image,
                verification=verification
            )
            reg.save()
            messages.success(request, "Congratulation !! Profile Updated Successfully")
            context = {"form": form, "active": "btn-primary"}
            return redirect("home")
   
class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Review
    template_name = "app/commentdelete.html"
    success_url = "/"
    
    def test_func(self):
        return is_users(self.get_object().author, self.request.user)


        
class HomeDetailView(LoginRequiredMixin,DetailView):
    model = House
    template_name = 'app/housedetail.html'
    context_object_name = 'house'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Review.objects.filter(house=self.get_object()).order_by('-date_posted')

        data['comments'] = comments_connected
    
        data['form'] = CommentForm(instance=Traveller.objects.get(user=self.request.user))
        return data

    def post(self, request, *args, **kwargs):
        form =CommentForm(request.POST)
        if form.is_valid():
          new_comment = Review(comment=request.POST.get('comment'),
                              author=Traveller.objects.get(user=self.request.user),
                              house=self.get_object())
          new_comment.save()

        return self.get(self, request, *args, **kwargs)



class PostListView(ListView):

    model = Post
    template_name = 'app/post.html'
    context_object_name = 'post'
    paginate_by = 5
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        post = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(post, self.paginate_by)
        try:
            post = paginator.page(page)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)
        context['post'] = post
        return context


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'app/postdetail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(post=self.get_object()).order_by('-date_posted')

        data['comments'] = comments_connected
    
        data['form'] = CommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        form =CommentForm(request.POST)
        if form.is_valid():
          new_comment = Comment(comment=request.POST.get('comment'),
                              author=Traveller.object.get(user=self.request.user),
                              house=self.get_object())
          new_comment.save()

        return self.get(self, request, *args, **kwargs)


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "app/chat.html", context)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "app/postdelete.html"
    success_url = "/"
    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

class PostMakeView(LoginRequiredMixin,View):

    def get(self,request):
        form=PostForm()
        return render(request,'app/postcreate.html', {"form": form, "acitve": "btn-primary"})


    def post(self, request):
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            traveller=Traveller.objects.get(user=user)
            title = form.cleaned_data["title"]
            subtitle =  form.cleaned_data["subtitle"]
            content = form.cleaned_data["content"]
            image = form.cleaned_data["image"]

            reg = Post(
                author=traveller,
           
                title=title,
                content = content,
                subtitle =subtitle,
                image=image,
               

            )
            reg.save()
            messages.success(request, "Congratulation !! Post Created Successfully")
            context = {"form": form, "active": "btn-primary"}
            return redirect('home')





def add_to_cart(request):
    return render(request,"app/cart.html")
