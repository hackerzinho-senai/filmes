from django.contrib import admin
from django.urls import path
from setup import settings
from django.conf.urls.static import static
from filmes.views import (FilmeCreateView, FilmeDeleteView, FilmeDetailView, FilmeForm, FilmeListView, 
                          FilmeUpdateView, PlaylistCreateView, PlaylistDeleteView, PlaylistDetailView, 
                          PlaylistForm, PlaylistListView, PlaylistUpdateView)  

urlpatterns = [
    path('', PlaylistListView.as_view(), name='playlist_list'),
    path('create/', PlaylistCreateView.as_view(), name='playlist_create'),
    path('<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'),
    path('<int:pk>/edit/', PlaylistUpdateView.as_view(), name='playlist_update'),
    path('<int:pk>/delete/', PlaylistDeleteView.as_view(), name='playlist_delete'),

    path('filmes/', FilmeListView.as_view(), name='filme_list'),
    path('filmes/<int:pk>/', FilmeDetailView.as_view(), name='filme_detail'),
    path('filmes/create/', FilmeCreateView.as_view(), name='filme_create'),
    path('filmes/<int:pk>/edit/', FilmeUpdateView.as_view(), name='filme_update'),
    path('filmes/<int:pk>/delete/', FilmeDeleteView.as_view(), name='filme_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
