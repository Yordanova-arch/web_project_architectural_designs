from django.shortcuts import render


# Create your views here.
def main_page(request):
    context = {
        'current_page': 'home'
    }
    return render(request, 'index.html', context)
