# Pizza API Challenge

A simple RESTful API for managing restaurants, pizzas, and their relationships. Built with Flask, SQLAlchemy, and Alembic, this project demonstrates best practices for building, validating, and documenting a backend API. You can use this API to manage restaurants, pizzas, and the prices at which each restaurant offers each pizza.

---

## Table of Contents

1. [Introduction](#pizza-api-challenge)
2. [Setup Instructions](#setup-instructions)
3. [Database Migration & Seeding](#database-migration--seeding)
4. [Route Summary](#route-summary)
5. [Example Requests & Responses](#example-requests--responses)
6. [Validation Rules](#validation-rules)
7. [Postman Usage](#postman-usage)

---

## Setup Instructions

1. **Clone the repository and navigate to the project directory:**

   ```bash
   git clone <your-repo-url>
   cd pizza-api-challenge
   ```

2. **Install dependencies using pipenv:**

   ```bash
   pipenv install
   pipenv shell
   ```

3. **Set up the database:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
   flask db init should be used only if migration does not exist

4. **Seed the database:**

   ```bash
   python -m server.seed
   ```

5. **Run the Flask server:**
   ```bash
   flask run
   # or
   python -m server.app
   ```

---

## Database Migration & Seeding

- Migrations are managed with Flask-Migrate (Alembic).
- Use `flask db migrate` and `flask db upgrade` to manage schema changes.
- Seed the database with sample data using `python -m server.seed`.

---

## Route Summary

### Restaurants

- `GET /restaurants` — List all restaurants
- `GET /restaurants/<int:id>` — Get a restaurant and its pizzas
- `DELETE /restaurants/<int:id>` — Delete a restaurant and its related RestaurantPizzas

### Pizzas

- `GET /pizzas` — List all pizzas

### Restaurant Pizzas

- `POST /restaurant_pizzas` — Create a new RestaurantPizza

---

## Example Requests & Responses

### GET /restaurants

**Request:**

```http
GET /restaurants
```

**Response:**

```json
[
  { "id": 1, "name": "Pizza Place", "address": "Tom Mboya St" },
  { "id": 2, "name": "Pasta Place", "address": "Kenyatta Ave" }
]
```

### GET /restaurants/<int:id>

**Request:**

```http
GET /restaurants/1
```

**Response:**

```json
{
  "id": 1,
  "name": "Pizza Place",
  "address": "Tom Mboya St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato, Mozzarella, Basil",
      "price": 10
    }
  ]
}
```

**If not found:**

```json
{ "error": "Restaurant not found" }
```

### DELETE /restaurants/<int:id>

**Request:**

```http
DELETE /restaurants/1
```

**Response:**

- Status: 204 No Content
  **If not found:**

```json
{ "error": "Restaurant not found" }
```

### GET /pizzas

**Request:**

```http
GET /pizzas
```

**Response:**

```json
[
  { "id": 1, "name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil" },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Tomato, Mozzarella, Pepperoni"
  }
]
```

**If none:**

```json
{ "error": "No pizzas found" }
```

### POST /restaurant_pizzas

**Request:**

```http
POST /restaurant_pizzas
Content-Type: application/json

{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

**Success Response:**

```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  },
  "restaurant": { "id": 3, "name": "Salad Place", "address": "Westalands" }
}
```

**Validation Error:**

```json
{ "errors": ["Price must be between 1 and 30"] }
```

---

## Validation Rules

- `price` for RestaurantPizza must be between 1 and 30 (inclusive).
- All fields (`price`, `pizza_id`, `restaurant_id`) are required for POST /restaurant_pizzas.
- `pizza_id` and `restaurant_id` must reference existing Pizza and Restaurant records.

---

## Postman Usage

- Import the provided `challenge-1-pizzas.postman_collection.json` into Postman.
- Use the collection to test all endpoints with example requests and responses.

---

For any issues, please open an issue or contact the maintainer.
