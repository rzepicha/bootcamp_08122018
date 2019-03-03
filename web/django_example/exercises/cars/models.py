from django.db import models

# Create your models here.
BODY_TYPE_CHOICES=(
    ("sedan", "sedan"),
    ("combi", "combi"),
    ("hatchback", "hatchback"),
    ("cabriolet", "cabriolet"),
    ("van", "van"))

ENGINE_TYPE_CHOICES=(
    ("hybrid", "hybrid"),
    ("benz", "benz"),
    ("diesel", "diesel"),
    ("steam", "steam"),
)

class Engine(models.Model):
    type=models.CharField(max_length=20, choices=ENGINE_TYPE_CHOICES)
    power=models.IntegerField()
    description=models.TextField(null=True, blank=True)

    def __sts__(selfself):
        return f"{self.type}| {self.power}"

class Car(models.Model): #klasa dziedziczy po models
    brand=models.CharField(max_length=200)
    model=models.CharField(max_length=50)
    year=models.IntegerField()
    body_type=models.CharField(max_length=20, choices=BODY_TYPE_CHOICES, null=True, blank=True) #blank-puste w formularzu
    engine=models.ForeignKey(Engine,on_delete=models.SET_NULL, null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    is_ready=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model}"



