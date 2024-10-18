# myimageapp/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from webapp.views import upload_image, login_view

urlpatterns = [
    path('', login_view, name='login'),  # Set the login view as the home page
    path('login/', login_view, name='login'),  # Optional, keep this for direct access
    path('upload/', upload_image, name='upload_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
