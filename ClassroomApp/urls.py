from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('students_list', views.students_list, name='students_list'),
    path('add_student', views.add_student, name='add_student'),
    path('update_student/<student_id>', views.update_student, name='update_student'),
    path('delete_student/<student_id>', views.delete_student, name='delete_student'),
    path('show_student/<student_id>', views.show_student, name='show_student'),

    path('groupes_list', views.groupes_list, name='groupes_list'),
    path('add_groupe', views.add_groupe, name='add_groupe'),
    path('update_groupe/<groupe_id>', views.update_groupe, name='update_groupe'),
    path('delete_groupe/<groupe_id>', views.delete_groupe, name='delete_groupe'),
    path('search_group', views.search_group, name='search_group'),

    path('search_student', views.search_student, name='search_student'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
