from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal, Review
from django.contrib.auth.decorators import login_required

def index(request):
    search_term = request.GET.get('search')
    if search_term:
        animals = Animal.objects.filter(name__icontains=search_term)
    else:
        animals = Animal.objects.all()
    template_data = {
        'title': 'Animals',
        'animals': animals
    }
    return render(request, 'animals/index.html', {
        'template_data': template_data,
        'show_hero': False  # Don't show hero section on animals page
    })

def show(request, id):
    animal = get_object_or_404(Animal, id=id)
    reviews = Review.objects.filter(animal=animal).order_by('-date')

    template_data = {
        'title': animal.name,
        'animal': animal,
        'reviews': reviews
    }
    return render(request, 'animals/show.html', {
        'template_data': template_data,
        'show_hero': False  # Don't show hero section on animal detail page
    })

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'].strip():
        animal = get_object_or_404(Animal, id=id)
        review = Review(
            comment=request.POST['comment'],
            animal=animal,
            user=request.user
        )
        review.save()
        return redirect('animals.show', id=id)
    return redirect('animals.show', id=id)

@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('animals.show', id=id)

    if request.method == 'GET':
        template_data = {
            'title': 'Edit Review',
            'review': review
        }
        return render(request, 'animals/edit_review.html', {
            'template_data': template_data
        })
    elif request.method == 'POST' and request.POST['comment'].strip():
        review.comment = request.POST['comment']
        review.save()
        return redirect('animals.show', id=id)
    return redirect('animals.show', id=id)
