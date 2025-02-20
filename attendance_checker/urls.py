
from django.contrib import admin
from django.urls import path,include
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', include('core.urls')),
]
