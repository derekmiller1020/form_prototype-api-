from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import FormPost, PostingForm, LoginForm, Login, RegisterForm
import requests
import json
from django.template import loader, Context, RequestContext
from Rabbit.rabbit import Rabbit
from the_variables import *

def register_post(request):

    #Set request_message to blank
    register_message = ""
    success_message = ""

    #Once we determine the request type, set the variables
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check post data
        if register.is_valid():

            #define variables to send to api
            url = REGISTER_URL
            the_data = {'username': username, 'password': password}

            #send data
            r = requests.post(url, data=the_data)
            status = r.status_code
            the_text = r.text

            #load data into dictionary
            the_data = json.loads(r.text)

            if 'success' in the_data:

                if the_data['success'] == 'True':
                    success_message = 'congrats, you have been signed up!'

                elif the_data['success'] == 'False':
                    register_message = the_data['message']

                else:
                    register_message = "There was an unknown error"

            else:
                register_message = "There was an unknown error"

    else:
        register = RegisterForm()

    return render(request, 'register.html', {
        'register': register,
        'register_message': register_message,
        'success_message': success_message,
    })

def login_post(request):

    username_message = ''
    password_message = ''

    if request.method == 'POST':
        login = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if login.is_valid():

            url = LOGIN_URL
            the_data = {'username': username, 'password': password}

            r = requests.post(url, data=the_data)
            status = r.status_code
            the_text = r.text

            the_data = json.loads(r.text)

            if the_data['success'] == 'True':
                request.session['user_id'] = the_data['user_id']
                request.session['has_conn'] = True
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

def form_post(request):

    response_message = ''

    if 'user_id' in request.session:
        if request.method == 'POST':
            form = PostingForm(request.POST)
            name = request.POST.get('name')
            food = request.POST.get('food')
            music = request.POST.get('music')
            movie = request.POST.get('movie')
            book = request.POST.get('book')
            poem = request.POST.get('poem')
            quote = request.POST.get('quote')

            if form.is_valid():

                url = FORM_URL
                the_data = {'unique_id': request.session['user_id'], 'name': name, 'food': food, 'music': music,
                            'movie': movie, 'book': book, 'poem': poem, 'quote': quote}

                r = requests.post(url, data=the_data)
                status = r.status_code
                the_text = r.text

                the_data = json.loads(r.text)

                if 'success' in the_data:
                    if the_data['success'] == 'True':
                        response_message = 'Your information has been added'
                    else:
                        response_message = 'Unknown error. Sorry'
                else:
                    response_message = 'blllaaaahhhh'

        else:
            form = PostingForm()

    else:
        return HttpResponseRedirect('/login/')

    return render(request, 'logic.html', {
        'form': form,
        'response_message': response_message
    })

def logout(request):

    login_message = ''
    logout_message = ''

    if request.session.get('has_conn', False):
        if request.session['has_conn'] == True:
            login_message = 'you are logged in'
        else:
            login_message = 'you are not logged in'

        del request.session['has_conn']
        del request.session['user_id']

        if request.session.get('has_conn', False):
            logout_message = 'Something went wrong'
        else:
            logout_message = 'You are officially logged out'

    else:
        login_message = 'you are not logged in'

    return render (request, 'logout.html', {
        'login_message': login_message,
        'logout_message': logout_message,
    })