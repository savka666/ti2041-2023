from ninja import Schema
from typing import List

# Este es el esquema utilizado para la creación de posts exclusivamente
class MessageSchema(Schema):
    message: str

class ServiceInputSchema(Schema):
    nombres: str
    descripcion: str
    proveedores: int
    precios: int
    from_date: str
    thru_date: str

class ProviderOutputSchema(Schema):
    nombre_fantasia: str
    nombre_tax: str
    id_tax: str
    habilitacion: bool

class AddressOutputSchema(Schema):
    proveedores: int
    type: str
    direccion1: str
    direccion2: str
    zipcodigo: str
    ciudad: str
    region: str
    paises: str

class ContactOutputSchema(Schema):
    proveedores: int
    type: str
    primer_nombre: str
    segundo_nombre: str
    email: str
    telefono: str
    celular: str

class ServiceOutputSchema(Schema):
    nombres: str
    descripcion: str
    proveedores: ProviderOutputSchema
    precios: int
    from_date: str
    thru_date: str
    contacto: List[ContactOutputSchema]
    direccion: AddressOutputSchema






