from rest_framework import serializers

from users.models import User
from users.validators import FieldsValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'date_joined', 'date_of_birth']
        write_only_fields = ('password',)
        validators = [FieldsValidator()]

    def create(self, fields):
        if 'date_of_birth' not in fields:
            fields['date_of_birth'] = None

        user = User.objects.create(
            username=fields['username'],
            first_name=fields['first_name'],
            last_name=fields['last_name'],
            date_of_birth=fields['date_of_birth']
        )

        user.set_password(fields['password'])
        user.save()

        return user
