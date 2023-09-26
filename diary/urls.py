from django.contrib import admin
from django.urls import path, include
from grades.views import index, contacts, notes, add_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('users/', include('users.urls'), name='users'),
    path('notes/', notes, name='notes'),
    path('add_note/', add_note, name='add_note'),
]
