from django.http import JsonResponse
from .models import New
from .serializers import NewsSerializer


def news_list(request):

    #get all the news
    #serialize them 
    #return json
    news = New.objects.all()
    serializer = NewsSerializer(news, many=True)
    return JsonResponse({'News':serializer.data}, safe=False) 