from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">看我</h1>'
    line2 = '<h1 style="text-align: center"><img src="https://i.postimg.cc/Kz02yNBd/IMG20210516193807.jpg" width=400></h1>'
    return HttpResponse(line1 + line2)
