from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    primerApellido = db.Column(db.String(50))
    email = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    
class Maestros(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    primerApellido = db.Column(db.String(50))
    email = db.Column(db.String(50))
    materia = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    
class Ventas(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre_cliente = db.Column(db.String(50))
    direccion_cliente = db.Column(db.String(50))
    telefono_cliente = db.Column(db.String(50))
    total = db.Column(db.Integer)
    fecha_pedido = db.Column(db.DateTime, default=datetime.datetime.now)
    dia_semana = db.Column(db.String(20), default=datetime.datetime.now().strftime('%a'))