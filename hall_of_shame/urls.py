from django.urls import path
from hall_of_shame.views import (
    show_hall_of_shame,
    get_hall_of_shame,
    add_corruptor,
    delete_corruptor,
    show_detail,
    add_corruptor_flutter,
)

app_name = 'hall_of_shame'

urlpatterns = [
    path('', show_hall_of_shame, name='show_hall_of_shame'),
    path('json/', get_hall_of_shame, name='get_hall_of_shame'),
    path('add/', add_corruptor, name='add_corruptor'),
    path('delete/<id>/', delete_corruptor, name='delete_corruptor'),
    path('detail/<id>/', show_detail, name='show_detail'),
    path('add-flutter', add_corruptor_flutter, name='add_corruptor_flutter')
]
