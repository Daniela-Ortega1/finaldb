from fastapi import APIRouter, HTTPException
from app.models import CustomerCreate, Customer, PqrsCreate, Pqrs, EmployeeCreate, Employee, StoreCreate, Store, OrderCreate, Order, ProductCreate, Product
from app.database import get_db_connection
from typing import List

router = APIRouter()

# Customer endpoints
@router.post("/customers/", response_model=Customer, tags=["Customers"])
def create_customer(customer: CustomerCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO customers (full_name, gender, age, city)
        VALUES (%s, %s, %s, %s)
        """
        values = (customer.full_name, customer.gender, customer.age, customer.city)
        
        cursor.execute(query, values)
        conn.commit()
        
        customer_id = cursor.lastrowid
        return Customer(customer_id=customer_id, **customer.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/customers/", response_model=List[Customer], tags=["Customers"])
def list_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM customers"
        cursor.execute(query)
        customers = cursor.fetchall()
        return [Customer(**customer) for customer in customers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/customers/bulk/", response_model=List[Customer], tags=["Customers"])
def create_customers_bulk(customers: List[CustomerCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO customers (full_name, gender, age, city)
        VALUES (%s, %s, %s, %s)
        """
        values = [(c.full_name, c.gender, c.age, c.city) for c in customers]
        
        cursor.executemany(query, values)
        conn.commit()
        
        # Fetch the last inserted id
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        # Calculate the ids of all inserted customers
        customer_ids = range(last_id - len(customers) + 1, last_id + 1)
        
        return [Customer(customer_id=cid, **c.dict()) for cid, c in zip(customer_ids, customers)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Store endpoints
@router.post("/stores/", response_model=Store, tags=["Stores"])
def create_store(store: StoreCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO stores (store_name, address, city)
        VALUES (%s, %s, %s)
        """
        values = (store.store_name, store.address, store.city)
        
        cursor.execute(query, values)
        conn.commit()
        
        store_id = cursor.lastrowid
        return Store(store_id=store_id, **store.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/stores/", response_model=List[Store], tags=["Stores"])
def list_stores():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM stores"
        cursor.execute(query)
        stores = cursor.fetchall()
        return [Store(**store) for store in stores]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/stores/bulk/", response_model=List[Store], tags=["Stores"])
def create_stores_bulk(stores: List[StoreCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO stores (store_name, address, city)
        VALUES (%s, %s, %s)
        """
        values = [(s.store_name, s.address, s.city) for s in stores]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        store_ids = range(last_id - len(stores) + 1, last_id + 1)
        
        return [Store(store_id=stid, **s.dict()) for stid, s in zip(store_ids, stores)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Product endpoints
@router.post("/products/", response_model=Product, tags=["Products"])
def create_product(product: ProductCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO products (product_name, price)
        VALUES (%s, %s)
        """
        values = (product.product_name, product.price)
        
        cursor.execute(query, values)
        conn.commit()
        
        product_id = cursor.lastrowid
        return Product(product_id=product_id, **product.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/products/", response_model=List[Product], tags=["Products"])
def list_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()
        return [Product(**product) for product in products]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/products/bulk/", response_model=List[Product], tags=["Products"])
def create_products_bulk(products: List[ProductCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO products (product_name, price)
        VALUES (%s, %s)
        """
        values = [(p.product_name, p.price) for p in products]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        product_ids = range(last_id - len(products) + 1, last_id + 1)
        
        return [Product(product_id=pid, **p.dict()) for pid, p in zip(product_ids, products)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Employee endpoints
@router.post("/employees/", response_model=Employee, tags=["Employees"])
def create_employee(employee: EmployeeCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO employees (full_name, position, hire_date, salary)
        VALUES (%s, %s, %s, %s)
        """
        values = (employee.full_name, employee.position, employee.hire_date, employee.salary)
        
        cursor.execute(query, values)
        conn.commit()
        
        employee_id = cursor.lastrowid
        return Employee(employee_id=employee_id, **employee.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/employees/", response_model=List[Employee], tags=["Employees"])
def list_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        return [Employee(**employee) for employee in employees]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/employees/bulk/", response_model=List[Employee], tags=["Employees"])
def create_employees_bulk(employees: List[EmployeeCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO employees (full_name, position, hire_date, salary)
        VALUES (%s, %s, %s, %s)
        """
        values = [(e.full_name, e.position, e.hire_date, e.salary) for e in employees]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        employee_ids = range(last_id - len(employees) + 1, last_id + 1)
        
        return [Employee(employee_id=eid, **e.dict()) for eid, e in zip(employee_ids, employees)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Order endpoints
@router.post("/orders/", response_model=Order, tags=["Orders"])
def create_order(order: OrderCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO orders (order_date, total_amount, payment_method, customer_id, store_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (order.order_date, order.total_amount, order.payment_method, order.customer_id, order.store_id)
        
        cursor.execute(query, values)
        conn.commit()
        
        order_id = cursor.lastrowid
        return Order(order_id=order_id, **order.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/orders/", response_model=List[Order], tags=["Orders"])
def list_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM orders"  # Solo selecciona registros con store_id
        cursor.execute(query)
        orders = cursor.fetchall()
        return [Order(**order) for order in orders]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/orders/bulk/", response_model=List[Order], tags=["Orders"])
def create_orders_bulk(orders: List[OrderCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO orders (order_date, total_amount, payment_method, customer_id)  # Cambia customer_fk por customer_id
        VALUES (%s, %s, %s, %s)
        """
        values = [(o.order_date, o.total_amount, o.payment_method, o.customer_id) for o in orders]  # Cambia customer_fk por customer_id
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        order_ids = range(last_id - len(orders) + 1, last_id + 1)
        
        return [Order(order_id=oid, **o.dict()) for oid, o in zip(order_ids, orders)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# PQRS endpoints
@router.post("/pqrs/", response_model=Pqrs, tags=["PQRS"])
def create_pqrs(pqrs: PqrsCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO pqrs (type, customer_id, case_date, subject, status, urgency)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Cambia pqrs.customer_fk por pqrs.customer_id
        values = (pqrs.type, pqrs.customer_id, pqrs.case_date, pqrs.subject, pqrs.status, pqrs.urgency)
        
        cursor.execute(query, values)
        conn.commit()
        
        pqrs_id = cursor.lastrowid
        return Pqrs(pqrs_id=pqrs_id, **pqrs.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/pqrs/", response_model=List[Pqrs], tags=["PQRS"])
def list_pqrs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM pqrs"
        cursor.execute(query)
        pqrs_list = cursor.fetchall()
        return [Pqrs(**pqrs) for pqrs in pqrs_list]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/pqrs/bulk/", response_model=List[Pqrs], tags=["PQRS"])
def create_pqrs_bulk(pqrs_list: List[PqrsCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO pqrs (type, customer_id, case_date, subject, status, urgency)  # Cambia customer_fk por customer_id
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = [(p.type, p.customer_id, p.case_date, p.subject, p.status, p.urgency) for p in pqrs_list]  # Cambia customer_fk por customer_id
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        pqrs_ids = range(last_id - len(pqrs_list) + 1, last_id + 1)
        
        return [Pqrs(pqrs_id=pid, **p.dict()) for pid, p in zip(pqrs_ids, pqrs_list)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()