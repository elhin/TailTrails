from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator

class PetPost(models.Model):
    PET_TYPE_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    pet_name = models.CharField(max_length=100, blank=True)
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES)
    breed = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=20, blank=True)
    last_seen_location = models.CharField(max_length=200)
    last_seen_date = models.DateField()
    contact_phone = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(10),
            RegexValidator(regex=r'^\+?\d{10,15}$', message="Enter a valid phone number.")
        ]
    )
    contact_email = models.EmailField()
    description = models.TextField()
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.get_status_display()} - {self.pet_type.capitalize()}" + \
               (f" ({self.pet_name})" if self.pet_name else "")

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Pet Post"
        verbose_name_plural = "Pet Posts"
