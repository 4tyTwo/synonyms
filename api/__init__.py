# from gensim.models import KeyedVectors
#
from django.conf import settings

MODEL = getattr(settings, "MODEL")
