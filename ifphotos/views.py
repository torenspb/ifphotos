from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Visitor
from django.template.loader import render_to_string
from .forms import UsernameForm
import requests


class IndexView(View):

    def get(self, request):
        form = UsernameForm()
        return render(request, 'base.html', {'form': form})

    def post(self, request):
        collect_visitor(
            ip=request.META['REMOTE_ADDR'],
            user_agent=request.META['HTTP_USER_AGENT'][0:100],
            search_value=request.POST['username']
        )
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            data = get_photos(username, request)
            return JsonResponse(data)
        else:
            return JsonResponse({'data': 'Form is not valid'})


class InfoView(View):

    def get(self, request):
        data = dict()
        data['data'] = render_to_string('info.html', request=request)
        return JsonResponse(data)


def collect_visitor(ip, user_agent, search_value=None, req_method=0):
    visitor = Visitor.objects.create(
        ip=ip,
        user_agent=user_agent,
        search_value=search_value,
        req_method=1
    )


def get_photos(username, request):
    data = dict()
    url = 'https://www.instagram.com/' + username + '/?__a=1'
    r = requests.get(url)

    try:
        resp = r.json()
    except ValueError:
        data['data'] = render_to_string('not_found.html', request=request)
        return data

    username = resp['user']['full_name']
    bio = resp['user']['biography']

    if not resp['user']['is_private']:
        nodes = resp['user']['media']['nodes']
        thumb = [i['thumbnail_resources'][0]['src'] for i in nodes]
        links = [i['display_src'] for i in nodes]
        photos = dict(zip(links, thumb))
        username = request.POST['username']
        context = {'username': username, 'bio': bio, 'photos': photos}
        data['data'] = render_to_string(
            'results.html',
            context,
            request=request
        )
        return data
    else:
        data['data'] = render_to_string(
            'private.html',
            context={'username': username, 'bio': bio},
            request=request
        )
        return data
