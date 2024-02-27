from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField, TelField
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