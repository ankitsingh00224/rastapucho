from django.shortcuts import render
from django.http import HttpResponse
from .models import Card, TopCard

# Create your views here.

def HomePage(request):

    card_details = Card.objects.all()

    top_card = TopCard.objects.all()

    return render(request,'index.html', {'cards': card_details,'top_card':top_card});
