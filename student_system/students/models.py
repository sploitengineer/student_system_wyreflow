from django.db import models

class Students(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name

    # Compatibility with Django auth expectations so DRF and SimpleJWT work
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        # If you want to support deactivating a student, add a BooleanField
        # like `active = models.BooleanField(default=True)` and use that here.
        return True

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name.split()[0] if self.full_name else ''
