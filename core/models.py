from django.db import models

# Create your models here.
from django.db import models

class Donation(models.Model):
    DONATION_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=DONATION_STATUS,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation ${self.amount} - {self.status}"


class Delivery(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    member = models.ForeignKey(
        'registration.Member',
        on_delete=models.CASCADE,
        related_name='deliveries'
    )
    volunteer = models.ForeignKey(
        'registration.Volunteer',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_deliveries'
    )
    partner = models.ForeignKey(
        'registration.Partner',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_deliveries'
    )

    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delivery for {self.member} - {self.status}"


class Meal(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    prep_instructions = models.TextField(blank=True)
    prep_time_minutes = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    date = models.DateField()
    meals = models.ManyToManyField(Meal, related_name='menus')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Menu for {self.date}"


class Ingredient(models.Model):
    STATUS_CHOICES = [
        ('good', 'Good'),
        ('warning', 'Warning'),
        ('critical', 'Critical'),
    ]

    name = models.CharField(max_length=150)
    quantity = models.CharField(max_length=50)
    expiry_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='good')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
