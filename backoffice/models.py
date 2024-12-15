from django.db import models
from django.urls import reverse


"""
Services
- Name 
- Description
"""

"""
Cars
- Name
- Slug
- Price
- Speed
- Essence
- Year
- Description
- Thumbnail
- Created_on
"""

"""
Reviews
- Author
- Rating
- Content
- Active
- Created_on
"""

"""
Coordinate
- Adress
- Email
- Phone
- Schedules
- Status
"""

"""
ContactForm
- Name
- Lastname
- Email
- Phone 
- Message
"""

"""
CarForm
- Name
- Lastname
- Title
- Email
- Phone
- Message
"""


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    speed = models.DecimalField(max_digits=10,decimal_places=2)
    essence = models.CharField(max_length=128)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="cars", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vehicule", kwargs={"slug": self.slug})


class Coordinate(models.Model):
    adress = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    schedules = models.TextField(blank=True)
    status = models.TextField(blank=True)


class ContactForm(models.Model):
    name = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CarForm(models.Model):
    name = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)  
    content = models.TextField()
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)    
    def get_stars(self):
        return range(1, self.rating + 1)
    def __str__(self):
        return self.author
    def __str__(self):
        return 'Review {} by {}'.format(self.content, self.author)
