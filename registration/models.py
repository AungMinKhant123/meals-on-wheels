from django.db import models

# Create your models here.

class Volunteer(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    SERVICE_CHOICES = [
        ("delivery", "Meal Delivery"),
        ("preparation", "Meal Preparation"),
        ("packaging", "Packaging"),
        ("transportation", "Driving / Transportation"),
        ("admin", "Administrative Support"),
        ("fundraising", "Fundraising Events"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)

    interests = models.JSONField()  
    availability = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Partner(models.Model):
    SERVICE_CHOICES = [
        ("delivery", "Meal Delivery"),
        ("preparation", "Meal Preparation"),
        ("packaging", "Packaging"),
        ("kitchen", "Kitchen Space"),
        ("storage", "Cold Storage"),
        ("ingredients", "Ingredient Supply"),
    ]

    org_name = models.CharField(max_length=150)
    contact_person = models.CharField(max_length=100)

    org_email = models.EmailField(unique=True)
    org_phone = models.CharField(max_length=20)

    org_address = models.TextField()
    org_postal = models.CharField(max_length=10)

    services = models.JSONField()  # multiple checkbox values
    additional_info = models.TextField(blank=True, null=True)

    is_approved = models.BooleanField(default=False)  # admin approval flag
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name
    

class Member(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    national_id = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    address = models.TextField()
    postal_code = models.CharField(max_length=10)

    health_conditions = models.TextField()
    dietary_restrictions = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=False)  # approved by admin
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Caregiver(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    member = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,
        related_name="caregiver"
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    national_id = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()

    relationship = models.CharField(max_length=50)

    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} ({self.relationship})"