from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include default auth URLs
    path('', include('bookings.urls')),  # URLs from the bookings app
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Custom login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Custom logout to match /login/
]