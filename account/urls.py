from django.urls import path
from .views import loginpage, dashdoard, logoutpage, signuppage

urlpatterns = [
    path('signup', signuppage, name='signup'),
    path('login/', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),
    path('dashdoard', dashdoard , name='dashboard')
]