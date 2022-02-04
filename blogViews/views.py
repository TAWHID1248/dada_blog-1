from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .models import Category, Post
from django.views.generic import DetailView
#from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.shortcuts import render, get_object_or_404


def HomeViews(request):
    cat_lists = Category.objects.all()
    #feature_posts = Post.objects.all()
    feature_posts = Post.objects.filter(featured=True).order_by('-post_date')[0:1]
    latest_posts_date = Post.objects.order_by('-post_date')[:2]
    post_lists = Post.objects.all().order_by('-post_date')
    
    #postobj= get_object_or_404(Post, id=id)
    ##archive = Post.objects.filter(post_date__month=month)

    stuff_items = Post.objects.all()
    archive = Post.objects.all()

    p = Paginator(stuff_items, 5)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)

    except EmptyPage:
        page = p.page(1)    
    
    




    context = {
        'cat_lists' : cat_lists,
        'feature_posts': feature_posts,
        'latest_posts_date' : latest_posts_date,
        #'posts' : posts,
        'items' : page,
       'post_lists': post_lists,
       #'postobj': postobj,
       'archive' : archive
    }

    return render(request, 'home.html', context)

'''def detail_post_view(request, id=None):
        postobj= get_object_or_404(Post, id=id)

        context={
            'postobj': postobj
            }

        

        return render (request, 'archive.html', context)'''



def CategoryWisePostView(request, cat_id) :
    obj = Post.objects.filter(category=cat_id)

    #show_post = Post.objects.filter(category=cats.replace('-', ' '))
    cat_list = Category.objects.all()
    cat_lists = Category.objects.all()
    #feature_posts = Post.objects.all()
    feature_posts = Post.objects.filter(featured=True).order_by('-featured')[0:1]

    context = {

        'cat_lists' : cat_lists,
        'feature_posts': feature_posts,
        'obj': obj,
       #'show_post' : show_post,
        'cat_list' : cat_list 


    }

    return render(request, 'CategoryWisePostViews.html', context)
    







class PostDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'



    def get_context_data(self, *args, **kwargs) :
        feature_posts = Post.objects.filter(featured=True).order_by('-featured')[0:1]
        context = super().get_context_data(*args, **kwargs)
        context["feature_posts"] = feature_posts
        
        cat_lists = Category.objects.all()
        context["cat_lists"] = cat_lists
  
        return context

    
        
       

'''class PostDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


    def get_context_data(self, *args, **kwargs) :
        category_posts =  Post.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["category_posts"] = category_posts
        return context'''
