from django.contrib import admin
from posts.models import Image, ImageAlbum, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(ImageAlbum)