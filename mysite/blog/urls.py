from django.contrib import admin


from django.urls import path,include
from .views import *
urlpatterns = [
    path('users/',userlist),
    path('blog/',bloglist),
    path('post1/',post1list),

]