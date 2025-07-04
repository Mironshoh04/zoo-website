from django.shortcuts import render

def index(request):
    template_data = {}
    template_data['title'] = 'Zoo'
    template_data['show_hero'] = True  # Show hero section on home page
    return render(request, 'home/index.html', {
        'template_data': template_data,
        'show_hero': True  # Pass show_hero context
    })

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {
        "template_data": template_data,
        'show_hero': False  # Don't show hero section on about page
    })
