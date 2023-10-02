from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer


class UserCreateView(CreateAPIView):
    """ Создание пользователя """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(APIView):
    """ Создание пользователя """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/register.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})

    def post(self, request):
        birth = None
        if request.POST['birth']:
            birth = request.POST['birth']

        if request.POST['password'] != request.POST['password2']:
            return redirect('users:register')

        user = User.objects.create(
            username=request.POST['login'],
            first_name=request.POST['name'],
            last_name=request.POST['last_name'],
            date_of_birth=birth
        )

        user.set_password(request.POST['password'])
        user.save()

        return redirect('events:home')
