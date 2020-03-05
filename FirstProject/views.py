from django.http import HttpResponse
import datetime

saludoMessage="""
<html>
<body>
<h1>Hello World It's Siraj</h1>
</body>
</html>"""
def saludo(request): #First View

    return HttpResponse(saludoMessage)

def goodbye(request):

    return HttpResponse("Goodbye My brotha")

def getDate(request):
    fecha_actual=datetime.datetime.now()

    timeDate="""
    <html>
    <body>
    <h1>
    Fecha y hora actual: %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(timeDate)