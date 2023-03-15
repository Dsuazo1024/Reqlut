import urllib.request, json
import json


Datos = {}
def get_one(RUT):
    url = "http://ws.udd.net/Pregrado/PregradoAcademico/WSPreAcad.svc/JsonAlumno/GetInformacionByRut/"+ RUT
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    for a in data:
        Datos = {
            "Identificacion :" + a['Rut']
            ,"Email :" + a['eMail']
            ,"Name :" + a['Nombre']
            ,"LastName :" + a['Apellido_Paterno'] +" "+ a['Apellido_Materno']
            ,"Phone :" + '-'
            ,"Cellphone :" + '-'
            ,"Careers :" + a['Carrera']
            ,"Type :" + a['Sistema']
            ,"id :" + a['codCarrera']
            ,"State :" + a['Sistema']
        }
        aux = a['eMail'].replace('@',' ').split()
        url2 = "http://ws.udd.net/Pregrado/PregradoAcademico/WSPreAcad.svc/JsonAlumno/Informacion/Datos/"+ aux[0]
        response2 = urllib.request.urlopen(url2)
        data2 = json.loads(response2.read())
        for b in data2:
            Datos.update(
            {"Codigo_Alumno :" + str(b['Codigo_Alumno'])}
            ,{"InitialYear :" + str(b['Periodo_Actual'])}
            ,{"Endyear :" + str(b['Promocion'])}
            ,{"CentreId :" + str(b['Codigo_Tipo'])}
            ,{"ProgramName :" + str(b['Descripcion_Tipo'])}
            ,{"FacultyId :" + str(b['Campus'])}
            )
    for F in Datos:
        return str(Datos)


