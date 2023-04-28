from django.urls import path
from myapp.views import teacher_list

urlpatterns = [
    path('teachers/', teacher_list, name='teacher_list'),
]

