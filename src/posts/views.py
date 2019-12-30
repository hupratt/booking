from django.shortcuts import render
from django.views.generic import ListView
import datetime, pytz
from .models import Post, PostImage
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

class AboutView(ListView):
    model = Post
    template_name = "about.html"
    context_object_name = 'about_us_with_properties'

    def get_context_data(self, **kwargs):
        from django.utils.translation import get_language

        context = super().get_context_data(**kwargs)
        language = get_language()
        liste_events_en = Post.objects.all().filter(tag='property').order_by('timestamp')
        if language == 'en':
            context['properties'] = liste_events_en
        else:
            import sys
            sys.path.append("..")
            from booking.translate import translate
            context['properties'] = translate(liste_events_en, language)
        return context

def detail(request, slug):
    """
    Posts method: display the article's detail

    """
    post = get_object_or_404(Post, slug=slug)
    from django.utils.translation import get_language

    language = get_language()
    import sys

    sys.path.append("..")
    from booking.translate import translate

    img_list = PostImage.objects.filter(post=post)  

    if language == "en":
        context = {
            "post": post,
            "month_year": post.timestamp.strftime("%B, %Y"),
            "img_list": img_list,
        }
    else:
        context = {
            "post": translate(post, language),
            "month_year": post.timestamp.strftime("%B, %Y"),
            "img_list": img_list,
        }
    return render(request, "detail_location.html", context)  # queryset