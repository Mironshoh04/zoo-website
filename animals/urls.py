from .views import index, show, create_review, edit_review
from django.urls import path

urlpatterns = [
    path('', index, name='animals.index'),
    path('<int:id>/', show, name='animals.show'),
    path('<int:id>/review/create/', create_review, name='animals.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', edit_review, name='animals.edit_review'),
]
