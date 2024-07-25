from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render


monthly_challenges = {
    "january": "Meditate for 5 minutes",
    "february": "Create a new playlist",
    "march": "Pick or buy yourself flowers",
    "april": "Do one thing you're afraid of",
    "may": "Avoid social media for 24 hours",
    "june": "Read 50 pages of something",
    "july": "Go for a long walk",
    "august": "Create a mood board",
    "september": "Find an interesting podcast to listen to",
    "october": "Schedule your month",
    "november": "Try something you've always wanted to try",
    "december": "Do a 30-minute workout"
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!<h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
