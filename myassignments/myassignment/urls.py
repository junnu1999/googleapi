from django.contrib import admin
# from django.urls import path
# add include to your imports from django.urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # add this line below
    path('', include('main_app.urls')),
]