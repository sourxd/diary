from django.contrib import admin
from django.urls import path, include
from grades.views import index, contacts, notes, add_note, remove_note
from users.views import login, logout, registration, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('notes/', notes, name='notes'),
    path('add_note/', add_note, name='add_note'),
    path('remove_note/<int:note_id>', remove_note, name='remove_note'),
    path('login/', login, name='login'),
    path('reg/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
