from django import forms
from .models import Client
from django.utils import timezone
import re
from decimal import Decimal, ROUND_DOWN

FIO_RE_VALIDATION = "^[A-Za-zА-Яа-яЁёЇїІіЄєҐґ' -]+$"
FIO_MAX_LENGTH = 100


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

        fields = ['first_name', 'last_name', 'patronymic', 'gender', 'age', 'admission_date', 'spo2', 'body_mass_index',
                  'result', 'f_test_ex', 'f_test_in', 'comorb_ccc', 'comorb_bl', 'cd_ozhir', 'comorb_all', 'l_109',
                  'lf', 'rox', 'spo2_fio', 'ch_d']

        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'patronymic': 'Отчество',
            'gender': 'Пол',
            'age': 'Возраст',
            'admission_date': 'Дата поступления',
            'spo2': 'SPO2',
            'body_mass_index': 'ИМТ',
            'result': 'Исход',
            'ch_d': 'Частота дыхания',
            'cd_ozhir': 'Сахарный диабет или ожирение',
            'spo2_fio': 'Fraction of inspired oxygen',
            'rox': 'Rox-?',
            'lf': 'Lung function',
            'l_109': 'Level_109',
            'comorb_all': 'аллергии?',
            'comorb_ccc': 'comorb_ccc?',
            'f_test_in': 'внутренний',
            'f_test_ex': 'внешний',
            'comorb_bl': 'коморбидность',
            # Add labels for other fields
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'style': 'width: 80%;'}),
            'admission_date': forms.SelectDateWidget(),
            'comorb_ccc': forms.CheckboxInput(attrs={'class': 'checkbox-input'}),
            # Add widgets for other fields
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and len(first_name) > FIO_MAX_LENGTH:
            raise forms.ValidationError(f"Длина имени не должна превышать {FIO_MAX_LENGTH} символов.")

        # Проверка на наличие цифр, знаков, кроме апострофа и дефиса
        if first_name and not re.match(FIO_RE_VALIDATION, first_name):
            raise forms.ValidationError("Имя может содержать только буквы, апостроф, дефис и пробел.")

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        # Проверка на длину не более 100 символов
        if last_name and len(last_name) > FIO_MAX_LENGTH:
            raise forms.ValidationError(f"Длина фамилии не должна превышать {FIO_MAX_LENGTH} символов.")

        # Проверка на наличие цифр, знаков, кроме апострофа и дефиса
        if last_name and not re.match(FIO_RE_VALIDATION, last_name):
            raise forms.ValidationError("Фамилия может содержать только буквы, апостроф, дефис и пробел.")

        return last_name

    def clean_patronymic(self):
        patronymic = self.cleaned_data.get('patronymic')

        if patronymic and len(patronymic) > FIO_MAX_LENGTH:
            raise forms.ValidationError(f"Длина отчества не должна превышать {FIO_MAX_LENGTH} символов.")

        if patronymic and not re.match(FIO_RE_VALIDATION, patronymic):
            raise forms.ValidationError("Отчество может содержать только буквы, апостроф, дефис и пробел.")

        return patronymic

    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age is not None:
            if age < 0:
                raise forms.ValidationError("Возраст не может быть отрицательным числом.")
            elif age > 120:  # Установите желаемое верхнее значение, например, 150 лет
                raise forms.ValidationError("Возраст не может превышать 120 лет.")

        return age

    def clean_body_mass_index(self):
        body_mass_index = self.cleaned_data.get('body_mass_index')

        # Проверка на отрицательное значение BMI
        if body_mass_index is not None and body_mass_index < 0.0:
            raise forms.ValidationError("Индекс массы тела не может быть отрицательным.")

        # Проверка на значение BMI не более 100.0
        if body_mass_index is not None and body_mass_index > 100.0:
            raise forms.ValidationError("Индекс массы тела не может быть более 100.0.")

        # Проверка на количество знаков после запятой (не более 3)
        if body_mass_index is not None:
            decimal_part = Decimal(str(body_mass_index)).as_tuple().exponent
            if decimal_part < -3:
                raise forms.ValidationError("Индекс массы тела может иметь не более 3 знаков после запятой.")

        return body_mass_index

    def clean_spo2(self):
        spo2 = self.cleaned_data.get('spo2')

        if spo2 is not None and (spo2 < 0 or spo2 > 100):
            raise forms.ValidationError("SPO2 должен быть в пределах от 0 до 100.")

        return spo2

    def clean_lf(self):
        lf = self.cleaned_data.get('lf')

        if lf is not None and lf < 0:
            raise forms.ValidationError("lf не может быть отрицательным числом.")

        return lf

    def clean_admission_date(self):
        admission_date = self.cleaned_data.get('admission_date')

        if admission_date:
            # Проверка на дату, не больше сегодняшнего дня
            if admission_date > timezone.now().date():
                raise forms.ValidationError("Дата поступления не может быть в будущем.")

            # Проверка на дату, не раньше 2023 года
            if admission_date.year < 2023:
                raise forms.ValidationError("Дата поступления не может быть раньше 2023 года.")

        return admission_date

    def clean_ch_d(self):
        ch_d = self.cleaned_data.get('ch_d')

        # Проверка на отрицательное значение ch_d
        if ch_d is not None and ch_d < 0:
            raise forms.ValidationError("Частота дыхания не может быть отрицательной.")

        # Проверка на значение ch_d не более 150
        if ch_d is not None and ch_d > 150:
            raise forms.ValidationError("Частота дыхания не может превышать 150.")

        return ch_d

    def clean_f_test_ex(self):
        f_test_ex = self.cleaned_data.get('f_test_ex')

        # Проверка на отрицательное значение f_test_ex
        if f_test_ex is not None and f_test_ex < 0:
            raise forms.ValidationError("Значение f_test_ex не может быть отрицательным.")

        # Проверка на значение f_test_ex не более 200
        if f_test_ex is not None and f_test_ex > 200:
            raise forms.ValidationError("Значение f_test_ex не может превышать 200.")

        return f_test_ex

    def clean_f_test_in(self):
        f_test_in = self.cleaned_data.get('f_test_in')

        # Проверка на отрицательное значение f_test_in
        if f_test_in is not None and f_test_in < 0:
            raise forms.ValidationError("Значение f_test_in не может быть отрицательным.")

        # Проверка на значение f_test_in не более 200
        if f_test_in is not None and f_test_in > 200:
            raise forms.ValidationError("Значение f_test_in не может превышать 200.")

        return f_test_in

    def clean_l_109(self):
        l_109 = self.cleaned_data.get('l_109')

        # Проверка на отрицательное значение l_109
        if l_109 is not None and l_109 < 0:
            raise forms.ValidationError("Значение l_109 не может быть отрицательным.")

        # Проверка на значение l_109 не более 50
        if l_109 is not None and l_109 > 50:
            raise forms.ValidationError("Значение l_109 не может превышать 50.")

        return l_109

    def clean_lf(self):
        lf = self.cleaned_data.get('lf')

        # Проверка на отрицательное значение lf
        if lf is not None and lf < 0:
            raise forms.ValidationError("Значение lf не может быть отрицательным.")

        # Проверка на значение lf не более 50
        if lf is not None and lf > 50:
            raise forms.ValidationError("Значение lf не может превышать 50.")

        return lf

    def clean_rox(self):
        rox = self.cleaned_data.get('rox')

        # Проверка на отрицательное значение rox
        if rox is not None and rox < 0:
            raise forms.ValidationError("Значение rox не может быть отрицательным.")

        # Проверка на значение rox не более 50
        if rox is not None and rox > 50:
            raise forms.ValidationError("Значение rox не может превышать 50.")

        return rox

    def clean_spo2_fio(self):
        spo2_fio = self.cleaned_data.get('spo2_fio')

        # Проверка на отрицательное значение spo2_fio
        if spo2_fio is not None and spo2_fio < 0:
            raise forms.ValidationError("Значение spo2_fio не может быть отрицательным.")

        # Проверка на значение spo2_fio не более 600
        if spo2_fio is not None and spo2_fio > 600:
            raise forms.ValidationError("Значение spo2_fio не может превышать 600.")

        return spo2_fio
