# webapp/views.py

from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
from PIL import Image
import base64
import io
from django.conf import settings  
from django.shortcuts import render, redirect
from django.contrib import messages


def upload_image(request):
    original_image_url = None
    result_image_url = None
    heatmap_image_url = None
    
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image: InMemoryUploadedFile = request.FILES['image']
        
        # Save the uploaded image to the media folder
        original_image_path = os.path.join('media', uploaded_image.name)
        with open(original_image_path, 'wb+') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)

        # Get URLs for the result and heatmap images
        base_name = os.path.splitext(uploaded_image.name)[0]
        result_image_url = os.path.join(settings.MEDIA_URL, f"{base_name}_result.jpg")
        heatmap_image_url = os.path.join(settings.MEDIA_URL, f"{base_name}_anomaly.jpg")
        
        original_image_url = os.path.join(settings.MEDIA_URL, uploaded_image.name)

    return render(request, 'webapp/upload_image.html', {
        'original_image': original_image_url,
        'result_image': result_image_url,
        'heatmap_image': heatmap_image_url,
    })



# webapp/views.py


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Allow any username/password for demonstration
        if username and password:
            # Simulating a successful login
            return redirect('upload_image')  # Redirect to upload page on success
        else:
            messages.error(request, "Invalid username or password")  # Show error if invalid
    
    return render(request, 'login.html')  # Render the login page
