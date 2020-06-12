from django.shortcuts import render


def aboutView(request):
    template_name='about.html'
    return render(request, 'about/about.html')
