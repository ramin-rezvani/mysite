from django.http import HttpResponse,JsonResponse
def http_test(request):
    return HttpResponse("<h1>thin is a test</h1>")


def json_test(request):
    return JsonResponse({"name":"ramin rezvani"})

