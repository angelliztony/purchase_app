Purchase Requisition Form

This project is a simple end-to-end Purchase Requisition system built using FastAPI, MySQL, and HTML. It allows users to submit purchase requisition details through a web-based form, which are then stored in a MySQL database.

Project Overview

The application consists of:
A frontend HTML form for data entry
A FastAPI backend to handle form submissions
A MySQL database to persist purchase requisition data
This project is intended for learning and demonstration purposes and runs locally on the system.

Tech Stack

Backend: FastAPI (Python)
Frontend: HTML
Database: MySQL
Server: Uvicorn
Version Control: Git and GitHub

Project Structure
purchase_form/
│
├── backend/
│   ├── main.py
│   └── __pycache__/
│
├── frontend/
│   └── index.html
│
├── README.md

Database Details

Database Name: purchaseapp
Table Name: purchase_requisition

The table stores the following fields:

category
expense_head
company
division
subdivision
job_no
description
subject
expected_date
expected_time
sales_order_no
work_order_no
preferred_supplier
recommended_brand
requested_by

How to Run the Project Locally

1. Install Dependencies
Make sure Python 3.10 or above is installed.
Install required Python packages:
pip install fastapi uvicorn pymysql

2. Configure Database
Install and start MySQL
Create a database named purchaseapp
Create the purchase_requisition table
Update database credentials in backend/main.py

3. Start the Backend Server
Navigate to the backend folder:
cd backend
Run the FastAPI application:
uvicorn main:app --reload
The backend will be available at:
http://127.0.0.1:8000

4. Run the Frontend
Open the frontend file directly in a browser:
frontend/index.html
Submit the form to store data in the database.
API Endpoint
Method: POST
Endpoint: /submit
This endpoint accepts form data and saves it into the MySQL database.

Notes

This application runs locally.
Frontend and backend communicate over HTTP.
No authentication or validation is implemented.
CORS is not configured for production use.



Author
Angel
