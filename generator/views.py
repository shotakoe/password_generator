from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()_+~{}/?.,'))

    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(chars)
    return render(request, 'generator/password.html', {'password':thepassword})

def credits(request):
    return render(request, 'generator/credits.html')