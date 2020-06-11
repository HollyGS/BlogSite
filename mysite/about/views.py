from django.shortcuts import render

# Create your views here.
def aboutView(request):
    template_name='about.html'
    return render(request, 'about/about.html')
