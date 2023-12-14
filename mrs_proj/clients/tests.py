from django.test import TestCase
import os
from faker import Faker
from clients.models import Client
from datetime import date
from clients.forms import ClientForm
import secrets
import binascii

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

START_YEAR = 2023


class ClientFormTest(TestCase):
    """
        Класс для тестирования валидности формы ClientForm.

        Attributes:
            fake (Faker): Объект Faker для генерации случайных данных.

        Methods:
            setUp(self): Метод, вызываемый перед выполнением каждого тестового метода.
            test_valid_form(self): Метод тестирования валидности формы с корректными данными.
            test_invalid_form(self): Метод тестирования формы с некорректными данными.
            test_first_name_length: Метод тестирования корректности ввода по символам
    """

    def setUp(self):
        """Настройка объекта Faker перед каждым тестовым методом."""
        self.fake = Faker()

    def test_valid_form(self):
        """Тест валидности формы с корректными данными."""
        data = {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'age': self.fake.random_int(min=18, max=99),
            'admission_date': self.fake.date_between_dates(date(START_YEAR, 1, 1), date.today()),
            'gender': '1'
            # остальные поля модели
        }

        form = ClientForm(data)
        self.assertTrue(form.is_valid(), f'Form errors: {form.errors}')
        self.assertTrue(form.is_valid())

    def test_invalid_form_with_insufficient_data(self):
        """Тест формы с некорректными данными."""
        data = {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            # Недостаточно данных
        }

        form = ClientForm(data)
        self.assertFalse(form.is_valid())

    def test_first_name_length(self):
        """
        Тестирование корректности ввода длины имени в форме.

        Метод создает случайное имя, превышающее максимальную длину поля в форме,
        заполняет им форму ClientForm и проверяет, что форма считается невалидной.

        Asserts:
            assertFalse(bool): Подтверждает, что форма не прошла валидацию из-за превышения
            длины имени.
        """
        data = {
            'first_name': str('a' * 101),  # воод 101 символа
            'last_name': self.fake.last_name(),
            'age': self.fake.random_int(min=18, max=99),
            'admission_date': self.fake.date_between_dates(date(START_YEAR, 1, 1), date.today()),
            'gender': '1'
        }

        form = ClientForm(data)
        self.assertFalse(form.is_valid(), 'Form should be invalid due to first name length')

    def test_last_name_length(self):
        """
        Тестирование корректности ввода длины фамилии в форме.

        Метод создает случайную фамилию, превышающую максимальную длину поля в форме,
        заполняет ей форму ClientForm и проверяет, что форма считается невалидной.

        Asserts:
            assertFalse(bool): Подтверждает, что форма не прошла валидацию из-за превышения
            длины фамилии.
        """
        data = {
            'first_name': self.fake.first_name(),
            'last_name': str('a' * 101),  # ввод 101 символа
            'age': self.fake.random_int(min=18, max=99),
            'admission_date': self.fake.date_between_dates(date(START_YEAR, 1, 1), date.today()),
            'gender': '1'
        }

        form = ClientForm(data)
        self.assertFalse(form.is_valid(), 'Form should be invalid due to last name length')

    def test_age_negative(self):
        """
        Тестирование валидации возраста.

        Метод создает случайный возраст, отрицательный, заполняет им форму ClientForm
        и проверяет, что форма считается невалидной.

        Asserts:
            assertFalse(bool): Подтверждает, что форма не прошла валидацию из-за
            отрицательного возраста.
        """
        data = {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'age': -5,  # возраст отрицательный
            'spo2': 100,
            'admission_date': self.fake.date_this_decade(),
            'gender': '0'
        }

        form = ClientForm(data)
        self.assertFalse(form.is_valid(), 'Form should be invalid for negative age')

    def test_patronymic_valid(self):
        """
        Тестирование валидации отчества.

        Метод создает случайное отчество, соответствующее правилам валидации,
        заполняет им форму ClientForm и проверяет, что форма считается валидной.

        Asserts:
            assertTrue(bool): Подтверждает, что форма прошла валидацию.
        """
        data = {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'patronymic': "Ivanovich",
            'age': self.fake.random_int(min=18, max=99),
            'spo2': 100,
            'admission_date': self.fake.date_between_dates(date(START_YEAR, 1, 1), date.today()),
            'gender': '1'
        }

        form = ClientForm(data)
        self.assertTrue(form.is_valid(), 'Form should be valid for a valid patronymic')

    def test_body_mass_index_valid(self):
        """
        Тестирование валидации индекса массы тела.

        Метод создает случайные вес и рост, соответствующие правилам валидации,
        вычисляет индекс массы тела и заполняет им форму ClientForm.
        Проверяет, что форма считается валидной.

        Asserts:
            assertTrue(bool): Подтверждает, что форма прошла валидацию.
        """

        # Генерируем случайные байты и преобразуем их в число в диапазоне [0.0, 100.0)
        data = {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'age': self.fake.random_int(min=18, max=99),
            'admission_date': self.fake.date_between_dates(date(START_YEAR, 1, 1), date.today()),
            'gender': '1',
            'body_mass_index': float(self.fake.random_int(min=0, max=99)),
            # Добавьте остальные поля модели
        }

        print(data['body_mass_index'])

        form = ClientForm(data)
        self.assertTrue(form.is_valid(), 'Form should be valid for a valid body mass index')

    def test_spo2_fio_valid(self):
        """
        Тестирование валидации spo2_fio.

        Метод создает случайное значение spo2_fio, соответствующее правилам валидации,
        и заполняет им форму ClientForm. Проверяет, что форма считается валидной.

        Asserts:
            assertTrue(bool): Подтверждает, что форма прошла валидацию.
        """
        data = {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'spo2_fio': self.fake.random_int(min=0, max=600),  # случайное значение в пределах допустимого
            'age': self.fake.random_int(min=18, max=99),
            'admission_date': self.fake.date_between_dates(date(START_YEAR, 1, 1), date.today()),
            'gender': '0'
        }

        form = ClientForm(data)
        self.assertTrue(form.is_valid(), 'Form should be valid for a valid spo2_fio')

    def test_spo2_valid(self):
        """
        Тестирование валидации spo2.

        Метод создает случайное значение spo2, соответствующее правилам валидации,
        и заполняет им форму ClientForm. Проверяет, что форма считается валидной.

        Asserts:
            assertTrue(bool): Подтверждает, что форма прошла валидацию.
        """
        data = {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'spo2': self.fake.random_int(min=0, max=100),
            'age': self.fake.random_int(min=18, max=99),
            'admission_date': self.fake.date_between_dates(date(START_YEAR, 1, 1), date.today()),
            'gender': '1'
        }

        form = ClientForm(data)
        self.assertTrue(form.is_valid(), 'Form should be valid for a valid spo2')

class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls, num_objects=10):
        """
        Создает num_objects объектов Client с использованием случайных данных от Faker.
        """
        fake = Faker('ru_RU')

        # Создаем num_objects объектов Client с использованием случайных данных от Faker
        for _ in range(num_objects):
            Client.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                patronymic=fake.last_name(),
                age=fake.random_int(min=18, max=100),
                admission_date=fake.date_between(start_date='-30d', end_date='today'),
                id_token=fake.uuid4(),
                # другие поля модели
            )

    def test_none_values(self):
        """
        Тест проверяет, что поля в объекте Client не являются None.
        """
        clients = Client.objects.all()
        for client in clients:
            # Проверяем поле на NONE
            self.assertIsNotNone(client.first_name)
            self.assertIsNotNone(client.last_name)
            self.assertIsNotNone(client.patronymic)
            self.assertIsNotNone(client.age)
            self.assertIsNotNone(client.admission_date)
            self.assertIsNotNone(client.id_token)

        print(f'test_1_none_values: {len(clients)}')

    def test_str_method(self):
        """
        Тест использует метод __str__ для вывода строкового представления каждого объекта Client.
        """
        clients = Client.objects.all()

        # Используем метод __str__ и выводим строку для каждого объекта
        for client in clients:
            print(str(client))

    def test_token_uniqueness(self):
        """
        Тест для проверки уникальности токенов.
        """
        clients = Client.objects.all()
        tokens = set(client.id_token for client in clients)
        print(f'test_token_uniqueness: {len(tokens)}')
        self.assertEqual(len(clients), len(tokens))

    def test_get_gender_display(self):
        """
        Тест для проверки вывода пола(отображения).
        """
        client = Client.objects.first()
        self.assertEqual(client.get_gender_display(), 'Мужской' if client.gender else 'Женский')
