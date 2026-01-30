from fastapi import FastAPI, Form
import pymysql

app = FastAPI()


def get_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="angel123",  
        database="purchaseapp",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.post("/submit")
def submit_form(
    category: str = Form(...),
    expense_head: str = Form(...),
    company: str = Form(...),
    division: str = Form(...),
    subdivision: str = Form(...),
    job_no: str = Form(None),
    description: str = Form(None),
    subject: str = Form(...),
    expected_date: str = Form(...),
    expected_time: str = Form(None),
    sales_order_no: str = Form(None),
    work_order_no: str = Form(None),
    preferred_supplier: str = Form(...),
    recommended_brand: str = Form(None),
    requested_by: str = Form(...)
):
    db = get_db()
    cursor = db.cursor()

    sql = """
    INSERT INTO purchase_requisition
    (category, expense_head, company, division, subdivision, job_no,
     description, subject, expected_date, expected_time, sales_order_no,
     work_order_no, preferred_supplier, recommended_brand, requested_by)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        category, expense_head, company, division, subdivision, job_no,
        description, subject, expected_date, expected_time,
        sales_order_no, work_order_no, preferred_supplier,
        recommended_brand, requested_by
    )

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()

    return {"message": "Purchase Requisition Saved Successfully"}
