from django.shortcuts import render

def home_page(request):
    return render(request, "home_page.html")

def office_page(request):
    return render(request, "office_page.html")

def activites_page(request):
    return render(request, "activities.html")