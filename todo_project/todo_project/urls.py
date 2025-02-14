from django.contrib import admin
from django.urls import path, include
from todo_app.views import home  # Import the home view

urlpatterns = [
    path("", home, name="home"),  # Home route
    path("admin/", admin.site.urls),
    path("api/", include("todo_app.urls")),
]
