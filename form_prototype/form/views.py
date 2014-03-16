from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import FormPost, PostingForm, LoginForm, Login
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

            the_data = {'username': username, 'password': password}
            RabbitMq(the_data)

            number = Login.objects.filter(username=username).count()
            if number != 1:
                username_message = 'Your username was not found'
            else:
                username_message = ''

            pass_find_it = Login.objects.filter(username=username, password=password).count()

            if pass_find_it == 1:
                the_pass = Login.objects.get(username=username, password=password)
                if password != the_pass.password:
                    password_message = 'your password does not match'
                else:
                    request.session['unique_id'] = the_pass.unique_id
                    return HttpResponseRedirect('/form/')
            else:
                password_message = 'Password is incorrect'
        else:
            login =LoginForm()
    else:
        login = LoginForm()

    return render(request, 'login.html', {
        'login': login,
        'username_message': username_message,
        'password_message': password_message,
    })
