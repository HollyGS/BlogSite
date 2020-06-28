from django.shortcuts import render

def contactView(request):
    template_name='contact.html'
    return render(request, 'contact/contact.html')
