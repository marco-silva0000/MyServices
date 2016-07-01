from random import shuffle

from django.shortcuts import render


# Create your views here.


def mapstringview(request):
    string = list('ABCDEFGHIJKLMNOPQR')
    shuffle(string)
    string = ''.join(string)
    print string
    # template = loader.get_template('polls/index.html')
    return render(request, 'mapstring.html', {'string': string})
