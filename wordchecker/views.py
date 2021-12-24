from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
import os
from .analyzer import analyze


@api_view(("POST",))
def get_analysis(request: Request) -> Response:
    with open(
        os.path.join(settings.BASE_DIR, "wordchecker", "hangeul.txt"),
        mode="r",
        encoding="utf-8",
    ) as f:
        words = f.read().split("\n")
    exact, almost, unmatched = analyze(words, request.body.decode("utf-8"))
    return Response(
        {"exact": exact, "almost": almost, "unmatched": unmatched},
        status=status.HTTP_200_OK,
    )
