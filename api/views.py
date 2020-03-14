from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from fuzzywuzzy import fuzz
from api import MODEL

logger = logging.getLogger("common_logger")


def pipeline(st, synonyms):
    return list(map(
        lambda pair: pair[0],
        map(
            lambda pair: (pair[0].replace('_', ' '), pair[1]),
            filter_similar(st, synonyms)
        )
    ))


def filter_similar(st, synonyms):
    res = []
    for pair in synonyms:
        ratio = fuzz.ratio(st, pair[0])
        if ratio < 75:
            res.append(pair)
    return res


@csrf_exempt
def most_similar(request, word):
    if request.method == "GET":
        word.lower()
        try:
            synonyms = pipeline(word, MODEL.most_similar(word))
            return JsonResponse({'similars': synonyms}, status=200)
        except KeyError:
            logger.info("Found no word " + word + " in dictionary")
    return HttpResponse(status=404)
