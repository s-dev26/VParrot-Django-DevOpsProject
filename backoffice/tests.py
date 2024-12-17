from django.test import TestCase
from .models import *

class ServiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Service.objects.create(name='Service de test', description='Description de test')

    def test_name_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_max_length(self):
        service = Service.objects.get(id=1)
        max_length = service._meta.get_field('description').max_length
        self.assertEquals(max_length, 300)

    def test_str_method(self):
        service = Service.objects.get(id=1)
        self.assertEquals(str(service), service.name)

class CarModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Car.objects.create(name='Voiture de test', slug='voiture-test', price=10000.00, speed=200.00, essence='Essence', year=2022)

    def test_name_label(self):
        car = Car.objects.get(id=1)
        field_label = car._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_price_max_digits(self):
        car = Car.objects.get(id=1)
        max_digits = car._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 10)

    def test_str_method(self):
        car = Car.objects.get(id=1)
        self.assertEquals(str(car), car.name)

    def test_get_absolute_url(self):
        car = Car.objects.get(id=1)
        self.assertEquals(car.get_absolute_url(), f"/vehicule/{car.slug}/")


class CoordinateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coordinate.objects.create(adress='Adresse de test', email='test@example.com', phone='1234567890', schedules='Horaires de test', status='Statut de test')

    def test_adress_label(self):
        coordinate = Coordinate.objects.get(id=1)
        field_label = coordinate._meta.get_field('adress').verbose_name
        self.assertEquals(field_label, 'adress')

    def test_str_method(self):
        coordinate = Coordinate.objects.get(id=1)
        self.assertEquals(str(coordinate), coordinate.adress)

class ContactFormModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ContactForm.objects.create(name='Test', lastname='Test', email='test@example.com', phone='1234567890', message='Message de test')

    def test_name_label(self):
        contact_form = ContactForm.objects.get(id=1)
        field_label = contact_form._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_str_method(self):
        contact_form = ContactForm.objects.get(id=1)
        self.assertEquals(str(contact_form), contact_form.name)


class CarFormModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CarForm.objects.create(name='Test', lastname='Test', title='Test', email='test@example.com', phone='1234567890', message='Message de test')

    def test_title_label(self):
        car_form = CarForm.objects.get(id=1)
        field_label = car_form._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_str_method(self):
        car_form = CarForm.objects.get(id=1)
        self.assertEquals(str(car_form), car_form.title)


class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Review.objects.create(author='Auteur de test', rating=5, content='Contenu de test', active=True)

    def test_author_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_str_method(self):
        review = Review.objects.get(id=1)
        self.assertEquals(str(review), review.author)

    def test_get_stars_method(self):
        review = Review.objects.get(id=1)
        self.assertEqual(list(review.get_stars()), [1, 2, 3, 4, 5])
