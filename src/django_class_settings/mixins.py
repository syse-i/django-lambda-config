__all__ = [
    'DisableSecurityMixin',
]


class DisableSecurityMixin:
    DEBUG = True

    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_PRELOAD = False
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_CONTENT_TYPE_NOSNIFF = False
    SECURE_BROWSER_XSS_FILTER = False
    SECURE_PROXY_SSL_HEADER = None

    SESSION_COOKIE_SECURE = False

    CSRF_COOKIE_SECURE = False

    X_FRAME_OPTIONS = 'DENY'
