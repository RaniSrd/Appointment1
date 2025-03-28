from django.contrib import admin # type: ignore
from django.urls import path # type: ignore

from views import appointment # type: ignore


urlpatterns = [
    path('admin/', admin.site.urls),

 
    path('appointment/',appointment,name="appointment")
]
