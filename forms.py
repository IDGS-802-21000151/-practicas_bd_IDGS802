from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField, TelField, BooleanField, DateField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField("Ingresa el nombre", [
        validators.DataRequired(message="El campo nombre es requerido"),
        validators.length(min=4, max=10, message="Ingresa un nombre valido")
    ])
    primerApellido = StringField("Ingresa el primer apellido")
    email = EmailField("Ingresa tu email", {
        validators.Email(message="Ingresa un email valido")
    })
    
class MeastroForm(Form):
    id = IntegerField('id')
    nombre = StringField("Ingresa el nombre", [
        validators.DataRequired(message="El campo nombre es requerido"),
        validators.length(min=4, max=10, message="Ingresa un nombre valido")
    ])
    primerApellido = StringField("Ingresa el primer apellido", [
        validators.DataRequired(message="El campo primer apellido es requerido")
    ])
    email = EmailField("Ingresa tu email", {
        validators.Email(message="Ingresa un email valido")
    })
    materia = StringField("Ingresa la materia", [
        validators.DataRequired(message="El campo materia es requerido"),
        validators.length(min=4, max=10, message="Ingresa un nombre valido")
    ])
    telefono = TelField("Ingresa tu telefono", {
        validators.DataRequired(message="El campo télefono es requerido")
    })
    
class PizzasForm(Form):
    nombreCliente = StringField("Ingresa el nombre del cliente", [
        validators.DataRequired(message="El campo nombre es requerido")
    ])
    direccionCliente = StringField("Ingresa la dirección", [
        validators.DataRequired(message="El campo dirección es requerido")
    ])
    telefonoCliente = TelField("Ingresa tu telefono", {
        validators.DataRequired(message="El campo télefono es requerido")
    })
    tamanioPizza = RadioField("Tamaño Pizza", choices=[('chica', 'Chica $40'), ('mediana', 'Mediana $80'), ('grande', 'Grande $120')], validators=[validators.DataRequired()])
    
    jamon = BooleanField('Jamon $10')
    pinia = BooleanField('Piña $10')
    champiniones = BooleanField('Champiñones $10')
    
    numeroPizzas = IntegerField("Ingresa el número de pizzas", {
        validators.DataRequired(message="El campo número de pizzas es requerido")
    })
    fechaPedido = DateField("Ingresa la fecha del pedido")