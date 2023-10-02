from rest_framework.serializers import ValidationError


class FieldsValidator:
    """ Проверка поля на введенные данные(ссылки запрещены, кроме youtube) """
    def __call__(self, fields):
        fields = dict(fields)
        if 'first_name' not in fields or fields['first_name'] == '':
            raise ValidationError('Не указано имя!')

        if 'last_name' not in fields or fields['last_name'] == '':
            raise ValidationError('Не указана фамилия!')
