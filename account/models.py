from uuid import uuid4

from django.db import models
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .services import (
    get_custom_user_img_path,
    get_default_user_img_path,
    validate_size_image,
    delete_old_file
)
from .managers import AccountManager


class Account(AbstractBaseUser):
    """
    Model to describe an user account
    """
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False, verbose_name=_('ID'))
    nickname = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    name = models.CharField(max_length=60, blank=True, null=True)
    surname = models.CharField(max_length=60, blank=True, null=True)

    img = models.ImageField(
        upload_to=get_custom_user_img_path,
        default=get_default_user_img_path,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), validate_size_image]
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self) -> str:
        return f'{self.nickname}'


@receiver(models.signals.post_delete, sender=Account)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Delete user photo file on delete model"""
    if instance.img:
        img_file_path = instance.img.path
        if "default" not in img_file_path:
            delete_old_file(instance.img.path)
