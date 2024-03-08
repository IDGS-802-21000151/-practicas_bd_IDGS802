from flask import Flask, request, render_template, jsonify, make_response
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db
from models import Alumnos, Maestros, Ventas
from flask import flash
from datetime import datetime, date, timedelta
from sqlalchemy import extract

import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config["CACHE_TYPE"] = "null"

csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route("/", methods=["GET", "POST"])
def cargarIndex():
    formRegistro = forms.UserForm(request.form)
    
    if request.method == "POST" and formRegistro.validate():
        alumno = Alumnos(nombre = formRegistro.nombre.data,
                        primerApellido = formRegistro.primerApellido.data,
                        email = formRegistro.email.data)
        
        #Insert into alumnos values()
        db.session.add(alumno)
        db.session.commit()
    
    return render_template("index.html", formRegistro = formRegistro)

@app.route("/registrar-maestro", methods=["GET", "POST"])
def registrarMaestro():
    formRegistro = forms.MeastroForm(request.form)
    
    if request.method == "POST" and formRegistro.validate():
        maestro = Maestros(nombre = formRegistro.nombre.data,
                        primerApellido = formRegistro.primerApellido.data,
                        email = formRegistro.email.data,
                        materia = formRegistro.materia.data,
                        telefono = formRegistro.telefono.data)
        
        db.session.add(maestro)
        db.session.commit()
    
    return render_template("registrar-maestro.html", formRegistro = formRegistro)

@app.route("/alumnos", methods=["GET", "POST"])
def cargarAlumnos():
    alumnos = Alumnos.query.all()
    return render_template("ABC_Completo.html",alumnos = alumnos)

@app.route("/maestros", methods=["GET", "POST"])
def cargarMaestros():
    maestros = Maestros.query.all()
    return render_template("maestros.html", maestros = maestros)

@app.route("/alumnos/edit/<int:idAlumno>", methods=["GET"])
def editarAlumno(idAlumno):
    formRegistro = forms.UserForm(request.form)
    alumno = Alumnos.query.get(idAlumno)
        
    return render_template("editarAlumno.html", formRegistro = formRegistro, alumno = alumno)

@app.route("/alumnos", methods=["DELETE"])
def eliminarAlumno():
    alumnos = Alumnos.query.all()
        
    return render_template("ABC_Completo.html", alumnos = alumnos)

@app.route("/pedido-pizza", methods=["GET", "POST"])
def pedidoPizza():
    formPedido = forms.PizzasForm(request.form)
    
    today = date.today()

    fechaInicio = datetime.combine(today, datetime.min.time())
    fechaFinal = datetime.combine(today, datetime.max.time())

    ventas = Ventas.query.filter(Ventas.fecha_pedido.between(fechaInicio, fechaFinal)).all()
    
    if request.method == "POST":
        ventaJSON = request.json
        
        fechaPedido = datetime.strptime(ventaJSON.get("fechaPedido"), "%Y-%m-%d")
        
        print(ventaJSON.get("fechaPedido"))
        fechaActual = datetime.now()

        fechaCombinada = fechaPedido.replace(hour=fechaActual.hour, minute=fechaActual.minute, second=fechaActual.second)
        
        diaSemana = fechaCombinada.strftime('%a')
        
        venta = Ventas(
            nombre_cliente = ventaJSON.get("nombreCliente"),
            direccion_cliente = ventaJSON.get("direccionCliente"),
            telefono_cliente = ventaJSON.get("telefonoCliente"),
            total = ventaJSON.get("total"),
            fecha_pedido = fechaCombinada,
            dia_semana = diaSemana
        )
            
        db.session.add(venta)
        db.session.commit()
        
        return jsonify({"mensaje": "Datos recibidos correctamente"})
    
    return render_template("pedido-pizza.html", form = formPedido, ventas = ventas)

@app.route("/ventas", methods=["GET", "POST"])
def ventas():
    month = request.args.get('month')
    day = request.args.get('day')
    weekday = request.args.get('weekday')
    
    if month != None:
        diaFiltro = datetime.strptime(month, '%Y-%m').date()

        primerDiaSiguienteMes = (diaFiltro + timedelta(days=32)).replace(day=1)

        fechaInicio = datetime.combine(diaFiltro, datetime.min.time())
        fechaFinal = datetime.combine(primerDiaSiguienteMes, datetime.min.time())

        ventas = Ventas.query.filter(Ventas.fecha_pedido.between(fechaInicio, fechaFinal)).all()
        totalVentas = sum(venta.total for venta in ventas)
        
        return render_template("ventas.html", ventas = ventas, month = month, totalVentas = totalVentas)
    elif day != None:
        diaFiltro = datetime.strptime(day, '%Y-%m-%d').date()

        fechaInicio = datetime.combine(diaFiltro, datetime.min.time())
        fechaFinal = datetime.combine(diaFiltro, datetime.max.time())

        ventas = Ventas.query.filter(Ventas.fecha_pedido.between(fechaInicio, fechaFinal)).all()
        totalVentas = sum(venta.total for venta in ventas)
        
        return render_template("ventas.html", ventas = ventas, day = day, totalVentas = totalVentas)
    elif weekday != None:
        ventas = Ventas.query.filter(Ventas.dia_semana == weekday).all()
        totalVentas = sum(venta.total for venta in ventas)
        
        return render_template("ventas.html", ventas = ventas, weekday = weekday, totalVentas = totalVentas)
    else:
        ventas = Ventas.query.all()
        totalVentas = sum(venta.total for venta in ventas)
        
        return render_template("ventas.html", ventas = ventas, totalVentas = totalVentas)

# Método Main
if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.run()