from django.http import HttpResponse

def home(request):
    html = "<html><head><title>Things</title></head></html>"
    return HttpResponse(html)

