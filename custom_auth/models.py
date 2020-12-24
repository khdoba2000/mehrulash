from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

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


class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, region, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')

        user = self.model(
            phone_number=phone_number,
            region=region,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, region, password=None):
        user = self.create_user(
            phone_number,
            password=password,
            region=region,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):

    phone_number = models.CharField(
                            max_length=9,
                            help_text="telefon raqamingiz 7 ta raqam bo'lishi kerak",
                            unique=True,
                            validators=[
                                RegexValidator(regex='^.{9}$', message='Length has to be 9')
                            ])
    password = models.CharField(
                            max_length=126,
                            validators=[
                                MinLengthValidator(6, "Parol kamida 6 xonali bo'lishi kerak! ")
                            ])
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    region = models.CharField(max_length=16,
                            choices=region_options)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    #age = models.IntegerChoices(0)
    USERNAME_FIELD = 'phone_number'
    #EMAIL_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['password', 'region']


    def __str__(self):
        return self.name
        
    def get_phone_number(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin