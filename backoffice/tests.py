from django.test import TestCase
from .models import Service, Car, Coordinate, ContactForm, CarForm, Review

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

class CoordinateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coordinate.objects.create(adress='Adresse de test', email='test@example.com', phone='1234567890', schedules='Horaires de test', status='Statut de test')

    def test_adress_label(self):
        coordinate = Coordinate.objects.get(id=1)
        field_label = coordinate._meta.get_field('adress').verbose_name
        self.assertEquals(field_label, 'adress')

class ContactFormModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ContactForm.objects.create(name='Test', lastname='Test', email='test@example.com', phone='1234567890', message='Message de test')

    def test_name_label(self):
        contact_form = ContactForm.objects.get(id=1)
        field_label = contact_form._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

class CarFormModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CarForm.objects.create(name='Test', lastname='Test', title='Test', email='test@example.com', phone='1234567890', message='Message de test')

    def test_title_label(self):
        car_form = CarForm.objects.get(id=1)
        field_label = car_form._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Review.objects.create(author='Auteur de test', rating=5, content='Contenu de test', active=True)

    def test_author_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')
