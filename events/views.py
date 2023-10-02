from django.shortcuts import redirect
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event
from events.permissions import IsOwner
from events.serializers import EventSerializer
from users.models import User


class MainView(APIView):
    """ Главная страница """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'events/main.html'

    def get(self, request):
        return Response()


class EventsView(APIView):
    """ События """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'events/events.html'

    def get(self, request, pk=0):
        events = Event.objects.all()

        if pk == 0:
            pk = events[0].id
        event = Event.objects.filter(id=pk)
        event = event[0]

        if 'participation' in request.GET:
            if request.GET['participation'] == 'cancell':
                # Берет всех участников данного события
                users = User.objects.filter(user_event__pk=event.id)
                print(users)

                # Если участник есть в событии, удаляет
                if self.request.user in users:
                    event.participants.remove(self.request.user)

                event.save()

            if request.GET['participation'] == 'add':
                # Берет всех участников данного события
                users = User.objects.filter(user_event__pk=event.id)

                # Если участника нет в событии, записывает
                if self.request.user not in users:
                    event.participants.add(self.request.user)

                event.save()

        participants = User.objects.filter(user_event__pk=event.id)

        user_events = Event.objects.filter(owner=request.user.id)

        return Response({
            'events': events,
            'user_events': user_events,
            'event': event,
            'participants': participants
        })


class EventDetailView(RetrieveAPIView):
    """ Просмотр одного события """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventListView(ListAPIView):
    """ Просмотр всех событий """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventCreateView(CreateAPIView):
    """ Создание события """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Сохранение авторизованного пользователя во владельца события и подписка того же пользователя на событие """
        event = serializer.save()
        event.owner = self.request.user
        event.participants.add(self.request.user)
        event.save()


class EventDeleteView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class EventUpdateView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ParticipationAddView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """ Добавляет участника к событию """
        event = serializer.save()
        # Берет всех участников данного события
        users = User.objects.filter(user_event__pk=event.id)

        # Если участника нет в событии, записывает
        if self.request.user not in users:
            event.participants.add(self.request.user)

        event.save()


class ParticipationCancellView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """ Удаляет участника из события """
        event = serializer.save()
        # Берет всех участников данного события
        users = User.objects.filter(user_event__pk=event.id)

        # Если участник есть в событии, удаляет
        if self.request.user in users:
            event.participants.remove(self.request.user)

        event.save()
