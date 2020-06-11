from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email_address = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email_address, ['hollygs96@live.co.uk'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            # send email code goes here
            return redirect('success')

    return render(request, 'contact/contact.html', {'form': form})

def successView(request):
    return render(request, 'contact/success.html')
