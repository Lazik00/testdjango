from .views import homePage,signin,signup
from django.urls import path,include

urlpatterns=[
    path('',homePage.as_view(),name='home'),
    path('signin/',signin.as_view(),name='signin'),
    path('signup/',signup.as_view(),name='signup')
]
