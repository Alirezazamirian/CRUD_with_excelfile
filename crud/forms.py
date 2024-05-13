from django import forms

from crud.models import Passenger


class TakeExcelFile(forms.Form):
    excel = forms.FileField()


class UpdatePeopleForm(forms.ModelForm):
    class Meta:
        model = Passenger
        exclude = ['id']
        error_messages = {
            'age': {'max_value': 'سن نباید بیشتر 120 باشد!'},
            'sibsp': {'max_value': 'تعداد همسر و خواهر و برادر نباید بیشت ار 10 باشد',
                      'min_value': 'تعداد همسر و خواهر و برادر نباید کمتر از 0 باشد', 'required': 'این فیلد لازم است'},
            'parch': {'max_value': 'تعداد فرزندان و پدر و مادر نباید بیشتر از 10 باشد',
                      'min_value': 'تعداد فرزندان و پدر و مادر نباید کمتر از 0 باشد', 'required': 'این فیلد لازم است'},
            'fare': {'required': 'این فیلد لازم است'},
            'cabin': {'max_length': 'شماره کابین نباید بیشتر از 20 کارکتر باشد'},
            'name': {'required': 'این فیلد لازم است', 'max_length': 'نام نباید بیشتر از 100 کارکتر باشد'},
            'ticket': {'required': 'این فیلد لازم است', 'max_length': 'این فیلد نباید بیشتر از 20 کارکتر باشد'},
            'sex': {'required': 'ین فیلد لازم است'},
            'pclass': {'required': 'ین فیلد لازم است'},
            'embarked': {'required': 'ین فیلد لازم است'},
        }


class CreatePeopleForm(forms.ModelForm):
    class Meta:
        model = Passenger
        exclude = ['id']
        error_messages = {
            'age': {'max_value': 'سن نباید بیشتر 120 باشد!'},
            'sibsp': {'max_value': 'تعداد همسر و خواهر و برادر نباید بیشت ار 10 باشد',
                      'min_value': 'تعداد همسر و خواهر و برادر نباید کمتر از 0 باشد', 'required': 'این فیلد لازم است'},
            'parch': {'max_value': 'تعداد فرزندان و پدر و مادر نباید بیشتر از 10 باشد',
                      'min_value': 'تعداد فرزندان و پدر و مادر نباید کمتر از 0 باشد', 'required': 'این فیلد لازم است'},
            'fare': {'required': 'این فیلد لازم است'},
            'cabin': {'max_length': 'شماره کابین نباید بیشتر از 20 کارکتر باشد'},
            'name': {'required': 'این فیلد لازم است', 'max_length': 'نام نباید بیشتر از 100 کارکتر باشد'},
            'ticket': {'required': 'این فیلد لازم است', 'max_length': 'این فیلد نباید بیشتر از 20 کارکتر باشد'},
            'sex': {'required': 'ین فیلد لازم است'},
            'pclass': {'required': 'ین فیلد لازم است'},
            'embarked': {'required': 'ین فیلد لازم است'},
        }
