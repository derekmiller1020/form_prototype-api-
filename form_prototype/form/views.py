from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import FormPost, PostingForm
from django.template import loader, Context, RequestContext

def form_post(request):

    if request.method == 'POST':
        form = PostingForm(request.post)
        if form.is_valid():
            form.save()
    else:
        form = PostingForm()

    return render(request, 'logic.html', {
        'form': form,
    })