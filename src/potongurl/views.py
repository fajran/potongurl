from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, \
                             redirect
from django.contrib.auth.models import AnonymousUser

from potongurl import utils
from potongurl.models import Link

def go(request, hash):
    link = get_object_or_404(Link, hash=hash, active=True)
    return redirect(link.url, permanent=True)

def index(request):
    if request.method == 'POST':
        url = utils.clean_url(request.POST['url'])
        if url is None:
            return redirect(reverse(index))

        user = request.user
        if isinstance(user, AnonymousUser):
            user = None

        link = Link(url=url, user=user)
        link.save()

        human = request.GET.get('human', None)
        if human is not None:
            return redirect('%s?show=%s' % (reverse(index), link.hash))
        else:
            return render_to_response('new.json', {'link': link},
                                      mimetype='text/plain')
    else:
        show = request.GET.get('show', None)
        if show is not None:
            try:
                link = Link.objects.get(hash=show)
                return render_to_response('show.html', {'link': link})
            except Link.DoesNotExist:
                return redirect(reverse(index))
        return render_to_response('index.html')

