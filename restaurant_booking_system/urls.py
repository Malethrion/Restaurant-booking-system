from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    path('', include('bookings.urls')),  # URLs from the bookings app
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login view
]
