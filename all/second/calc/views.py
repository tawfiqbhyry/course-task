from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import PrimForm


def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes
    


def prime_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PrimForm(request.POST)
        if not form.is_valid():
            return render(request, "prime_template.html", {"form": PrimForm, "error": "Invalid Input"})

        num = form.cleaned_data["num1"]
        print(num)
        s = SieveOfEratosthenes(num)
        return render(request, "prime_template.html", {"form": PrimForm, "primes": s})
    return render(request, "prime_template.html", {"form": PrimForm})


def show_html(request):
    return render(request, "show.html")

