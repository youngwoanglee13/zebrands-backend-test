# Product Catalog - ZeBrands Project
This project implements a basic catalog system to manage products. It allows administrators to create, update, and delete products, as well as manage other administrators. Additionally, anonymous users can retrieve information about products without the ability to make changes.

## Key Features
- Product management with SKU, name, price, and brand.
- Two types of users: administrators and anonymous users.
- Notifications to administrators when changes are made to products.
- Tracking the number of product queries made by anonymous users.

## Technologies
- Python
- Flask
- SQLAlchemy
- Flask-JWT-Extended
- Flask-Mail (Gmail)
- MySQL
- Docker

## Project Structure
The current architecture is a monolithic design, structured as a single unit with MVC pattern implementation. This allows for the implementation of some functionalities in the future, but if multiple functionalities are desired, it is recommended to use a microservices-based architecture.

- `app/`: Contains the application source code.
  - `controllers/`: Business logic controllers.
  - `database/`: Database configuration.
  - `models/`: Data model definitions.
  - `routes/`: Application routes.
  - `schemas/`: Data schemas for serialization.

## API Documentation
The API has the following endpoints:

- `/login` (POST): Allows users to authenticate and obtain a JWT token.
    Request:    {
                    "email": "user@example.com",
                    "password": "password"
                }
    Response:   {
                    "access_token": "<JWT_TOKEN>"
                }
- `/products` (POST - Requires JWT Token): Creates a new product.
    Request:    {
                    "name": "Product 1",
                    "price": 100,
                    "brand": "Brand A",
                    "sku": "SKU123"
                }
      
- `/products/<int:id>` (PUT - Requires JWT Token): Updates an existing
    Request:    {
                    "name": "NEW NAME",
                    ...
                }
- `/products` (GET): Gets all products.
- `/products/<int:id>` (DELETE - Requires JWT Token): Deletes an existing.
- `/products/<int:id>` (GET): Gets detailed information about a product with the provided ID. If there is no JWT token in the headers and the product exists, a view is recorded.
- `/product_views` (GET - Requires JWT Token): Gets the list of all product views, including detailed information for each view.
- `/users` (GET - Requires JWT Token): Gets the list of all users.
- `/users/<int:id>` (DELETE - Requires JWT Token): Deletes an existing user.
- `/users` (POST - Requires JWT Token): Creates a new user.
    Request:    {
                    "username": "new_user",
                    "password": "password",
                    "role": "user",
                    "email": "user@example.com"
                }
- `/users/<int:id>` (PUT - Requires JWT Token): Updates an existing user.
    Request:    {
                    "username": "other",
                }
       
## Configuración
Make sure to configure the following environment variables in your .env file:
- `DATABASE_URI`:  URI of the MySQL database.
- `JWT_SECRET_KEY`: Secret key for JWT token generation.
- `MAIL_USERNAME`: Email username for notifications.
- `MAIL_PASSWORD`: Email app password.

## Installation
1. Clone the repository to your local machine.
2. Open a terminal window and navigate to the project directory.
3. Run `docker-compose up` to start a Docker container running an instance of Flask.
4. Once the container is up and running, you can access the application by `http://localhost:5000.




