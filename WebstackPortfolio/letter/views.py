from django.shortcuts import render


def letterIndex(request):
    context = {
        
    }
    return render(request, 'letter/letterIndex.html', context)

def mail_letter(request):
    context = {
        
    }
    return render(request, 'letter/mail_letter.html', context)