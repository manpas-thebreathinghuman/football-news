from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406411830',
        'name': 'Haru Urara (no fake) (Jk it\'s M. Fadhlurrohman)',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.
