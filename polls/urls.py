from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rooms/", views.rooms, name="rooms"),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
    path('blogs/', views.blogs, name='blogs'),
    path('restart_poll/', views.restart_poll, name='restart_poll'),
    path('blogs/<int:id>/', views.blog_detail, name='blog_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)