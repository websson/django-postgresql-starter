"""Who may show this app inside a frame.

Django's XFrameOptionsMiddleware sends X-Frame-Options: DENY, and that header can
only say DENY or SAMEORIGIN, so an editor or builder on another address can never
show a live preview of the app. Content-Security-Policy frame-ancestors can name
who may frame it instead; every other site is still refused, as with DENY.

FRAME_ANCESTORS (environment) replaces the default list, e.g. "'none'" to refuse
every frame again.
"""
import os

DEFAULT = "'self' https://*.uppcoder.com"


class FrameAncestorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.policy = "frame-ancestors " + (os.environ.get("FRAME_ANCESTORS") or DEFAULT)

    def __call__(self, request):
        response = self.get_response(request)
        # an app that sets its own Content-Security-Policy keeps it
        response.headers.setdefault("Content-Security-Policy", self.policy)
        return response
