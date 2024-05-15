
 
class Product:
    def __init__(self, productId, productName, description, price, quantityInStock, type):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

#Getters---------------------

    def getProductId(self):
       return self.productId

    def getProductName(self):
      return self.productName

    def getDescription(self):
      return self.description

    def getPrice(self):
      return self.price

    def getQuantityInStock(self):
      return self.quantityInStock

    def getType(self):
      return self.type

# Setters----------------------
    def setProductId(self, productId):
      self.productId = productId

    def setProductName(self, productName):
      self.productName = productName

    def setDescription(self, description):
      self.description = description

    def setPrice(self, price):
      self.price = price

    def setQuantityInStock(self, quantityInStock):
      self.quantityInStock = quantityInStock

    def setType(self, type):
      self.type = type

print("Getters,Setters,Constructors are implemented Successfully")
def __str__(self):
      return f"Product ID: {self.productId}, Name: {self.productName}, Description: {self.description}, Price: {self.price}, Quantity in Stock: {self.quantityInStock}, Type: {self.type}"

# Create a Product instance
product = Product(1, "Laptop", "High-performance laptop", 1200.0, 10, "Electronics")

# Access the productName attribute using the getter method
print(product.getProductName())  # This will print the product name "Laptop"

#---------------------------------------------------------------------------------------------------------

class Electronics(Product):
 def __init__(self, productId, productName, description, price, quantityInStock, type, brand, warrantyPeriod):
  super().__init__(productId, productName, description, price, quantityInStock, type)
  self.brand = brand
  self.warrantyPeriod = warrantyPeriod

 def get_brand(self):
  return self.brand
 
 def set_brand(self, brand):
  self.brand = brand

 def get_warranty_period(self):
  return self.warrantyPeriod
 
 def set_warranty_period(self, warrantyPeriod):
  self.warrantyPeriod = warrantyPeriod

electronics_product = Electronics(1, "Phone", "High-RAM phone", 2000.5, 5, 
"Electronics", "Oneplus", 1)
print(electronics_product.get_brand()) 
electronics_product.set_warranty_period(2)
print(electronics_product.get_warranty_period())


class Clothing(Product):
 def __init__(self, productId, productName, description, price, quantityInStock, type, size, color):
  super().__init__(productId, productName, description, price, quantityInStock, type)
  self.size = size
  self.color = color
 
 def get_size(self):
  return self.size
 
 def set_size(self, size):
  self.size = size

 def get_color(self):
  return self.color
 
 def set_color(self, color):
  self.color = color

clothing_product = Clothing(4, "T-shirt", "Cotton t-shirt", 500.5, 4, "Clothing", "M", "Blue")
print(clothing_product.get_size()) 
clothing_product.set_color("Red")
print(clothing_product.get_color())

class User:
  def __init__(self, userId, username, password, role):
   self.userId = userId
   self.username = username
   self.password = password
   self.role = role # Either "Admin" or "User"

#Getters

  def get_user_id(self):
   return self.userId
  
  def get_username(self):
   return self.username
  
  def get_password(self):
   return self.password
  
  def get_role(self):
   return self.role
  
#Setters
  
  def set_user_id(self, userId):
   self.userId = userId

  def set_username(self, username):
   self.username = username

  def set_password(self, password):
   self.password = password
  
  def set_role(self, role):
   self.role = role

user1 = User(1, "Shiva", "shiva@123", "Admin")
print(user1.get_username()) 
print(user1.get_role()) 
user2 = User(2, "Anika", "anika@123", "User")
print(user2.get_username()) 
print(user2.get_role()) 
#--------------------------------------------
from abc import ABC, abstractmethod
class IOrderManagementRepository(ABC):
 @abstractmethod
 def createOrder(self, user, products):
  pass
 @abstractmethod
 def cancelOrder(self, userId, orderId):
  pass
 @abstractmethod
 def createProduct(self, user, product):
  pass
 @abstractmethod
 def createUser(self, user):
  pass
 @abstractmethod
 def getAllProducts(self):
  pass
 @abstractmethod
 def getOrderByUser(self, user):
  pass
 
#-----------------------------------------------------
from abc import ABC, abstractmethod
class IOrderManagementRepository(ABC):
 @abstractmethod
 def createOrder(self, user, products):
  pass
 @abstractmethod
 def cancelOrder(self, userId, orderId):
  pass
 @abstractmethod
 def createProduct(self, user, product):
  pass
 @abstractmethod
 def createUser(self, user):
  pass
 @abstractmethod
 def getAllProducts(self):
  pass
 @abstractmethod
 def getOrderByUser(self, user):
  pass
 
class OrderProcessor(IOrderManagementRepository):
 def __init__(self):
  self.users = {}
  self.products = {}
  self.orders = {}
 def createOrder(self, user, products):
  if user.userId not in self.users:
   self.createUser(user)
   order_id = len(self.orders) + 1
   self.orders[order_id] = {'user': user, 'products': products}
  return order_id
 
 def cancelOrder(self, userId, orderId):
  if userId not in self.users:
   raise UserNotFound("User with ID {} not found.".format(userId))
  if orderId not in self.orders:
   raise OrderNotFound("Order with ID {} not found.".format(orderId))
  del self.orders[orderId]
 def createProduct(self, user, product):
  if user.role != "Admin":
   raise PermissionError("User does not have permission to create products.")
  self.products[product.productId] = product
 def createUser(self, user):
  self.users[user.userId] = user
 def getAllProducts(self):
  return list(self.products.values())
 def getOrderByUser(self, user):
  user_orders = []
  for order in self.orders.values():
   if order['user'] == user:
    user_orders.append(order)
  return user_orders
 
class UserNotFound(Exception):
 pass
class OrderNotFound(Exception):
 pass
#---------------------------------------------------------------------
import pyodbc

server_name = "DESKTOP-463S8KN\SQLEXPRESS"
database_name = "HexawareProductDB"
 
 
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
 
 
cursor.execute("Select 1")
print("Database connection is successful 🎊")
#----------------------------------------------------------------
class OrderManagement:
 @staticmethod
 def main():
  order_=OrderProcessor()
  print("Welcome to Order Management System")
  while True:
   print("\nMenu:")
   print("1. Create User")
   print("2. Create Product")
   print("3. Cancel Order")
   print("4. Get All Products")
   print("5. Get Orders by User")
   print("6. Exit")
   choice = input("Enter your choice: ")
   if choice == "1":
    OrderManagement.createUser(order_)
   elif choice == "2":
    OrderManagement.createProduct(order_)
   elif choice == "3":
    OrderManagement.cancelOrder(order_)
   elif choice == "4":
    OrderManagement.getAllProducts(order_)
   elif choice == "5":
    OrderManagement.getOrderByUser(order_)
   elif choice == "6":
    print("Exiting...")
    break
   else:
    print("Invalid choice. Please try again.")

 @staticmethod
 def createUser(order_):
  print("Creating a new user...")
  userId=int(input("Enter userID:"))
  userName=input("Enter UserName:")
  password=input("Enter Password:")
  role=input("Enter your role:")
  print("User created successfully.")
  user=User(userId,userName,password,role)
  order_.createUser(user)
  cursor.execute("Select * from Movies")
  

@staticmethod
def createProduct(order_):
  print("Creating a new product...")
  productId= int(input("Enter Product ID: "))
  productName = input("Enter Product Name: ")
  description = input("Enter Description: ")
  price = float(input("Enter Price: "))
  quantityInStock = int(input("Enter Quantity in Stock: "))
  type = input("Enter Type (Electronics/Clothing): ")
  product= Product(productId, productName, description, price, quantityInStock,type)
  order_.create_product (None, product) #Assuming None for adais user
  print("Product created successfully.")

@staticmethod
def cancelOrder(order_):
  print("Canceling an order...")
  userId = int(input("Enter User ID: "))
  orderId = int(input("Enter Order ID: "))
  order_.cancel_order (userId, orderId)

@staticmethod
def getAllProducts (order_):
 products = order_.get_all_products()
 print("All Products:")
 for product in products:
   print(product.getProductName())
 print("Retrieving all products...")

@staticmethod
def getOrderByUser(order_):
  print("Retrieving orders by user...")
  userId = int(input("Enter User ID: "))
  orders=order_.get_order_by_user (None) 
  print("Orders by User:")
  for order in orders:
   print("Order ID:", order.getId())
if __name__ == "__main__":
 order_management = OrderManagement()
 order_management.main()
