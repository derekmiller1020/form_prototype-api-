from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import FormPost, PostingForm, LoginForm, Login
import requests
import json
from Rabbit.rabbit import RabbitMq
from django.template import loader, Context, RequestContext

def form_post(request):

    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostingForm()

    return render(request, 'logic.html', {
        'form': form,
    })

def login_post(request):

    username_message = ''
    password_message = ''

    if request.method == 'POST':
        login = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if login.is_valid():

            url = "http://127.0.0.1:5000/login/"
            the_data = {'username': str(username), 'password': str(password)}

            r = requests.post(url, data=the_data)
            status = r.status_code
            the_text = r.text

            username_message = str(r.text)

            the_data = json.loads(r.text)

            if the_data['success'] == 'True':
                request.session['user_id'] = the_data['user_id']
                return HttpResponseRedirect('/form/')

            elif the_data['success'] == 'False':
                if 'username_message' in the_data:
                    username_message = the_data['username_message']
                else:
                    password_message = the_data['password_message']

            else:
                username_message = 'There was an error'


    else:
        login = LoginForm()

    return render(request, 'login.html', {
        'login': login,
        'username_message': username_message,
        'password_message': password_message,
    })
