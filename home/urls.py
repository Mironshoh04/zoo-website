from django.urls import path
from .views import index, about#, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('', index, name='home.index'),
    path('about/', about, name='home.about'),
    # path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    # path('movie/new/', MovieCreateView.as_view(), name='movie_create'),
    # path('movie/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    # path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
]