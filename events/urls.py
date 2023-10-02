from django.urls import path

from events.apps import EventsConfig
from events.views import EventCreateView, EventUpdateView, EventDeleteView, EventListView, EventDetailView, \
    ParticipationAddView, ParticipationCancellView, EventsView, MainView

app_name = EventsConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('events/<int:pk>/', EventsView.as_view(), name='events'),
    path('event/create/', EventCreateView.as_view(), name='event_create'),
    path('event/update/<int:pk>/', EventUpdateView.as_view(), name='event_update'),
    path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),
    path('event/list/', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_view'),

    path('event/participation_add/<int:pk>/', ParticipationAddView.as_view(), name='participation_add'),
    path('event/participation_cancell/<int:pk>/', ParticipationCancellView.as_view(), name='participation_cancell'),
]
