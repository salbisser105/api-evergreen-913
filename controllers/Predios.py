from flask import jsonify, request
from db.db import cnx

class TipoSensor():
    global cur
    cur = cnx.cursor()
    
    def list():
        lista= []
        cur.execute("SELECT * FROM predios")
        rows= cur.fetchall()
        columnas= [i[0] for i in cur.description]
        for row in rows:
            registro=zip(columnas, row)
            json= dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close

    def create (body):
        data= (body['codigo'],body['latitud'],body['longitud'],body['producto'],body['area'],body['imagen'])
        sql = "INSERT INTO predios(codigo,latitud,longitud,producto,area,imagen) VALUES(%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': "Insertado"}, 200