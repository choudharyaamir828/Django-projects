from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import ReservationForm


# Create your views here.

def hello_word(request):
    return HttpResponse("Hello Word")


class Helloindia(View):
    def get(self, request):
        return HttpResponse("Hello India")


def home(request):
    form = ReservationForm()

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation successful!")
    return render(request, "index.html", {'form': form})