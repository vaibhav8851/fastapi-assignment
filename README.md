
---





### **README.md**:

---

# FastAPI Assignment

This repository contains the FastAPI application built as part of the assignment for Vodex.ai. The application performs CRUD operations for **Items** and **User Clock-In Records** using MongoDB as the database.

## **Table of Contents**:
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [How to Run the Project Locally](#how-to-run-the-project-locally)
4. [API Endpoints](#api-endpoints)
5. [Deployed Application](#deployed-application)
6. [Accessing the APIs](#accessing-the-apis)

## **Project Overview**:

- The project is a FastAPI application that supports CRUD operations for two entities:
    - **Items**: Includes item details such as name, email, quantity, and expiry date.
    - **User Clock-In Records**: Logs user clock-in data, such as email and location.
  
## **Technologies Used**:
- Python 3.x
- FastAPI
- MongoDB (via MongoDB Atlas)
- Koyeb for hosting
- GitHub for version control

## **How to Run the Project Locally**:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/vaibhav8851/fastapi-assignment.git
    cd fastapi-assignment
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up MongoDB**:
   - Create a MongoDB instance on MongoDB Atlas or run it locally.
   - Update the MongoDB connection string in the `main.py` file.
   
5. **Run the Application**:
    ```bash
    uvicorn main:app --reload
    ```

6. **Access the Swagger UI**:
    Open your browser and go to `http://127.0.0.1:8000/docs` to see the Swagger documentation and test the APIs.

## **API Endpoints**:

The application supports the following APIs:

### **Items APIs**:
- **POST** `/items`: Create a new item.
- **GET** `/items/{id}`: Retrieve an item by ID.
- **GET** `/items/filter`: Filter items by various criteria (Email, Expiry Date, Insert Date, Quantity).
- **GET** `/items/aggregate`: Aggregate items by email.
- **PUT** `/items/{id}`: Update an item by ID.
- **DELETE** `/items/{id}`: Delete an item by ID.

### **Clock-In APIs**:
- **POST** `/clock-in`: Create a new clock-in entry.
- **GET** `/clock-in/{id}`: Retrieve a clock-in entry by ID.
- **GET** `/clock-in/filter`: Filter clock-ins by email, location, or date.
- **PUT** `/clock-in/{id}`: Update a clock-in entry by ID.
- **DELETE** `/clock-in/{id}`: Delete a clock-in entry by ID.

## **Deployed Application**:

- The FastAPI application is hosted on Koyeb. You can access it here:
  - **Hosted Application**: [Koyeb Hosted Link](https://app.koyeb.com/services/bfed6fde-6696-403d-a467-3865190d94cd?deploymentId=ce2c646d-dee7-446a-a323-8f0ca74cfde6)
  
## **Accessing the APIs**:

- You can access and test the APIs using the **Swagger UI**:
  - **Swagger Documentation**: [Swagger UI Link](https://your-app-name.koyeb.app/docs)

---

