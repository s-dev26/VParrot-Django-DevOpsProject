from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from decimal import Decimal
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from backoffice.models import *


def index(request):
    services = Service.objects.all()
    cars = Car.objects.order_by("-created_on")[:3]
    coordinates = Coordinate.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact_data = ContactForm(name=name, lastname=lastname, email=email, phone=phone, message=message)
        contact_data.save()
    return render(request, 'website/index.html',
                context={"services": services, "cars": cars, "coordinates": coordinates})

def details_vehicule(request, slug):
    car = get_object_or_404(Car, slug=slug)
    coordinates = Coordinate.objects.all()
    if request.method == 'POST':
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            title = request.POST.get('title')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            contact_data = CarForm(name=name, lastname=lastname, title=title, email=email, phone=phone, message=message)
            contact_data.save()
    return render(request, 'website/details_vehicule.html', context={"car": car, "coordinates": coordinates})


def vehicules(request):
    cars = Car.objects.order_by("-created_on")[:3]
    coordinates = Coordinate.objects.all()
    return render(request, 'website/vehicules.html',
                    context={"cars": cars, "coordinates": coordinates})

def avis(request):
    coordinates = Coordinate.objects.all()
    reviews = Review.objects.filter(active=True).order_by("-created_on")
    new_review = None

    if request.method == 'POST':
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        content = request.POST.get('content')

        if author and rating and content:
            new_review = Review.objects.create(author=author, rating=rating, content=content)
            new_review.save()

    context = {
        'reviews': reviews,
        'new_review': new_review,
        'coordinates': coordinates
    }

    return render(request, 'website/avis.html', context)


def filter_cars(request):
    if request.method == 'POST':
        price_min = request.POST.get('price_min')
        price_max = request.POST.get('price_max')
        speed_min = request.POST.get('speed_min')
        speed_max = request.POST.get('speed_max')
        year_min = request.POST.get('year_min')
        year_max = request.POST.get('year_max')
        cars_filtered = Car.objects.all()
        if price_min:
            cars_filtered = cars_filtered.filter(price__gte=price_min)
        if price_max:
            cars_filtered = cars_filtered.filter(price__lte=price_max)
        if speed_min:
            cars_filtered = cars_filtered.filter(speed__gte=speed_min)
        if speed_max:
            cars_filtered = cars_filtered.filter(speed__lte=speed_max)
        if year_min:
            cars_filtered = cars_filtered.filter(year__gte=year_min)
        if year_max:
            cars_filtered = cars_filtered.filter(year__lte=year_max)

        cars_json = [{
            'thumbnail': car.thumbnail.url,
            'name': car.name,
            'speed': car.speed,
            'essence': car.essence,
            'price': car.price,
            'absolute_url': car.get_absolute_url()
        } for car in cars_filtered]

        return JsonResponse(cars_json, safe=False)
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


def mentions_legales(request):
    coordinates = Coordinate.objects.all()
    return render(request, 'website/mentions_legales.html',
                    context={"coordinates": coordinates})

def politique_confidentialite(request):
    coordinates = Coordinate.objects.all()
    return render(request, 'website/politique_confidentialite.html',
                    context={"coordinates": coordinates})

