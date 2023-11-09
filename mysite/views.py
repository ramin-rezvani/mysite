from django.http import HttpResponse
def http_test(request):
    return HttpResponse("<h1>thin is a test</h1>")
