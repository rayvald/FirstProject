from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import datetime

class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name


def saludo(request): #First View
    
    p1=Person("Ragnar", "Lothbrok")
    #first_name="Ragnar"
    #last_name="Lothbrok"

    topics_list=["Templates", "Models", "Forms", "Views", "Deploy"]
    now=datetime.datetime.now()

    #For Windows
    #doc_externo=open("C:/Users/rayni/Desktop/djangoProjects/FirstProject/FirstProject/templates/mytemplate.html")

    #For Linux and Mac
    #doc_externo = open("/Users/osvaldomurillo/Documents/djangoProjects/FirstProject/FirstProject/templates/mytemplate.html")

    #tmp=Template(doc_externo.read())

    #doc_externo.close

    #ctx=Context({"first_name":p1.first_name, "last_name":p1.last_name, "time":now, "topics":topics_list})

    doc_externo=get_template('mytemplate.html')
    document=doc_externo.render({"first_name":p1.first_name, "last_name":p1.last_name, "time":now, "topics":topics_list})

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