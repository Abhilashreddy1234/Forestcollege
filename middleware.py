from django.middleware.security import SecurityMiddleware

class CustomSecurityMiddleware(SecurityMiddleware):
    def process_response(self, request, response):
        response["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"
        return response
