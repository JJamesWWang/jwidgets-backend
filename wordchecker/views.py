from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
import os
from .analyzer import analyze


@api_view(("POST",))
def get_analysis(request: Request) -> Response:
    """Analyzes an essay on how many words match our Korean class's vocabulary.

    Param:
        request (Request): A request with a body containing Korean text.

    Returns:
        Response:
            Status: 200
            A JSON object with three keys:
                exact (string[]): Exact matches
                almost (string[]): Almost exact matches
                unmatched (string[]): Remaining unmatched words
    """
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
