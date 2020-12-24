from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
import this
# Create your models here.




section_options=(
    ('child_dress', 'bolalar kiyimlari'),
    ('man_dress', 'erkaklar kiyimlari'),
    ('woman_dress', 'ayollar kiyimlari'),
    ('home', 'uy jihozlari'),
    ('toys', "o'yinchoqlar"),
    ('books', 'kitoblar'),

)
region_options=(
    ('Tashkent_city', 'Toshkent shahar'),
    ('Tashkent', 'Toshkent viloyat'),
    ('Nukus', 'Nukus'),
    ('Urgench', 'Urganch'),
    ('Bukhara', 'Buxoro'),
    ('Navoiy', 'Navoiy'),
    ('Termiz', 'Termiz'),
    ('Qarshi', 'Qarshi'),
    ('Samarkand', 'Samarqand'),
    ('Guliston', 'Guliston'),
    ('Djizzakh', 'Jizzax'),
    ('Fergana', "Farg'ona"),
    ('Namangan', 'Namangan'),
    ('Andijon', 'Andijon')
)




class Post(models.Model):
    title = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    description = models.CharField(
        max_length=256,
        validators=[MinLengthValidator(2, "Description must be greater than 2 characters")]
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    
    section = models.CharField(max_length=32, choices=section_options)
    region = models.CharField(max_length=32, choices=region_options)

    # Picture
    picture = models.BinaryField(null=True, editable=True, blank=False)
    picture2 = models.ImageField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')

    phone_number = models.CharField(
        max_length=9,
        validators=[MinLengthValidator(9, "Phone number must be 9 characters")]
    )

    contact_info = models.CharField(
        default="https://t.me/",
        max_length=256,
        validators=[MinLengthValidator(2, "Contact info must be greater than 2 characters")]
    )


    is_available = models.BooleanField(default=True)
    
    def set_taken(self):
        self.is_available=False
        
    def set_available(self):
        self.is_available=True
    
   

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title
