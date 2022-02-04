from django.conf.urls import url
from django.urls import path
from . import views 
#from .views import CategoryView
from .views import HomeViews, CategoryWisePostView, PostDetailView




urlpatterns = [
    path('', HomeViews, name="home"),
    path('CategoryWisePostView/<int:cat_id>/', CategoryWisePostView, name="CategoryWisePostView"),
    path('aricle/<int:pk>', PostDetailView.as_view(), name="article-detail"),
    #path('archive/', detail_post_view, name="archive"),

]    