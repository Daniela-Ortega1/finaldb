from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, List

class CustomerCreate(BaseModel):
    full_name: str = Field(..., description="Nombre completo del cliente")
    gender: str = Field(..., description="Género del cliente")
    age: int = Field(..., description="Edad del cliente")
    city: str = Field(..., description="Ciudad del cliente")

class Customer(CustomerCreate):
    customer_id: int

class PqrsCreate(BaseModel):
    type: str = Field(..., description="Tipo de PQRS (Reclamo, Queja, Solicitud)")
    customer_id: int = Field(..., description="ID del cliente relacionado")
    customer_fk: Optional[int] = Field(None, description="ID del cliente como clave foránea")
    case_date: date = Field(..., description="Fecha del caso")
    subject: str = Field(..., description="Asunto del PQRS")
    status: str = Field(..., description="Estado del PQRS")
    urgency: str = Field(..., description="Urgencia del PQRS")

class Pqrs(PqrsCreate):
    pqrs_id: int

class EmployeeCreate(BaseModel):
    full_name: str = Field(..., description="Nombre completo del empleado")
    position: str = Field(..., description="Cargo del empleado")
    hire_date: date = Field(..., description="Fecha de contratación del empleado")
    salary: float = Field(..., description="Salario del empleado")
    store_id: Optional[int] = Field(None, description="ID de la tienda relacionada")

class Employee(EmployeeCreate):
    employee_id: int

class StoreCreate(BaseModel):
    store_name: str = Field(..., description="Nombre de la tienda")
    address: str = Field(..., description="Dirección de la tienda")
    city: str = Field(..., description="Ciudad de la tienda")

class Store(StoreCreate):
    store_id: int

class OrderCreate(BaseModel):
    order_date: date = Field(..., description="Fecha del pedido")
    total_amount: float = Field(..., description="Monto total del pedido")
    payment_method: str = Field(..., description="Método de pago")
    customer_id: int = Field(..., description="ID del cliente que realiza el pedido")
    store_id: Optional[int] = Field(None, description="ID de la tienda donde se realiza el pedido")

class Order(OrderCreate):
    order_id: int

class ProductCreate(BaseModel):
    product_name: str = Field(..., description="Nombre del producto")
    price: float = Field(..., description="Precio del producto")

class Product(ProductCreate):
    product_id: int