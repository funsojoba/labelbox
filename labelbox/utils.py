import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

from django.conf import settings

# Configuration       
cloudinary.config( 
    cloud_name = settings.CLOUDINARY_CLOUD_NAME, 
    api_key = settings.CLOUDINARY_API_KEY, 
    api_secret = settings.CLOUDINARY_API_SECRET,
    secure=True
)

class CloudinaryManager:
    
    @classmethod
    def upload_image(cls, file, folder):
        valid_extension = ['jpg', 'png', 'jpeg', 'JPEG', 'SVG', 'webp']

        if file.name.split('.')[-1] not in valid_extension:
            return Response(errors=dict(file_format_error="Please input a proper image file"), status=status.HTTP_400_BAD_REQUEST)

        upload_image = cloudinary.uploader.upload(file=file, folder=folder, user_filename=True, overwrite=True)
        return upload_image.get('url')