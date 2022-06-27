from django.shortcuts import render
import webbrowser

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def insta(request):
    webbrowser.open_new_tab("www.instagram.com/j1t9n")
    return render(request,'contact.html')

def github(request):
    webbrowser.open_new_tab("www.github.com/Know167")
    return render(request,'contact.html')

def linkedin(request):
    webbrowser.open_new_tab("www.linkedin.com/in/jatinpateldeveloper")
    return render(request,'contact.html')