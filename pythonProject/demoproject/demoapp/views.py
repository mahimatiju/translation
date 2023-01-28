from django.shortcuts import render, redirect
from .models import folder


# Create your views here.
def demo(request):
    if request.method == 'POST':
        lang=request.POST.get('language',)
        upload=request.FILES['abc']
        fol=folder(language=lang,upload=upload)
        fol.save()
        return redirect('demo')

    return render(request, 'new.html')


