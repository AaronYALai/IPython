from django.shortcuts import render
from django.http import HttpResponse
import random 
from random_sentences.models import sentence


def home(request):
    S = random.choice(sentence.objects.all())
    return render(request, "index.html", {'sentence': S.content})




