import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def article_home_view(request):
    pass

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    print("id:", id)
    print(args, kwargs)
    name = "Julius" # hard coded
    random_id = random.randint(1, 4)
    
    # from the database
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    
    # HTML_STRING = """
    # <h1>{title} (id: {id})</h1>
    # <p>{content}<p>
    # """.format(**context)
    
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)