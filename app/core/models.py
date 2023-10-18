"""Database models."""

from django.conf import settings
from django.db import models # noqa
from django.contrib.auth.models import ( AbstractBaseUser,BaseUserManager,PermissionsMixin)


class UserManager(BaseUserManager):
    "manager for users"

    def create_user(self, email, password=None, **extra_field):
        """Create, save and return new user."""

        if not email:
             raise ValueError("User must have an email address")
        
        user = self.model(email=self.normalize_email(email), **extra_field)

        #ser the harsh password
        user.set_password(password)

        try: 
            ##Try to save the user
            user.save(using=self._db)
        except IntegrityError:
            #checking for existing user in the database
            existing_user = self.get(email=email)
            return existing_user


        return user
    
    def create_superuser(self, email, password):
        """create and return a new superuser."""

        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user





class User(AbstractBaseUser,PermissionsMixin):

    """User in the system"""


    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'    

class Recipe(models.Model):
    """Receipe Object"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    """Tag for filtering recipes"""

    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

