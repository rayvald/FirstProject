from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request): #First View
    doc_externo = open("/Users/osvaldomurillo/Documents/djangoProjects/FirstProject/FirstProject/templates/mytemplate.html")

    tmp=Template(doc_externo.read())

    doc_externo.close

    ctx=Context()

    document=tmp.render(ctx)

    return HttpResponse(document)

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

def calculateAge(request, age, agno):
    periodo = agno - 2020
    futureAge = age + periodo

    future="""
    <html>
    <body>
    <h1>
    En el año: %s tendrás: %s años
    </h1>
    </body>
    </html>""" %(agno, futureAge)

    return HttpResponse(future)