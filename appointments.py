from tempfile import template
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")
appointments_data = [
    {"id": 1, "patient": "Aarav Sharma", "doctor": "Dr. Meena Nair", "date": "2025-08-15", "time": "10:00 AM"},
    {"id": 2, "patient": "Priya Verma", "doctor": "Dr. Rajesh Khanna", "date": "2025-08-16", "time": "11:30 AM"},
    {"id": 3, "patient": "Rohit Mehta", "doctor": "Dr. Kavita Sharma", "date": "2025-08-17", "time": "09:15 AM"},
    {"id": 4, "patient": "Sneha Kapoor", "doctor": "Dr. Suresh Menon", "date": "2025-08-18", "time": "02:00 PM"},
    {"id": 5, "patient": "Karan Gupta", "doctor": "Dr. Anita Reddy", "date": "2025-08-19", "time": "04:45 PM"},
    {"id": 6, "patient": "Ananya Singh", "doctor": "Dr. Meena Nair", "date": "2025-08-20", "time": "10:30 AM"},
    {"id": 7, "patient": "Vikram Malhotra", "doctor": "Dr. Rajesh Khanna", "date": "2025-08-21", "time": "12:00 PM"},
    {"id": 8, "patient": "Neha Agarwal", "doctor": "Dr. Suresh Menon", "date": "2025-08-22", "time": "03:30 PM"},
    {"id": 9, "patient": "Aditya Joshi", "doctor": "Dr. Anita Reddy", "date": "2025-08-23", "time": "09:45 AM"},
    {"id": 10, "patient": "Meera Nair", "doctor": "Dr. Kavita Sharma", "date": "2025-08-24", "time": "11:15 AM"},
    {"id": 11, "patient": "Siddharth Rao", "doctor": "Dr. Meena Nair", "date": "2025-08-25", "time": "01:00 PM"},
    {"id": 12, "patient": "Pooja Das", "doctor": "Dr. Rajesh Khanna", "date": "2025-08-26", "time": "10:15 AM"},
    {"id": 13, "patient": "Rahul Bansal", "doctor": "Dr. Suresh Menon", "date": "2025-08-27", "time": "02:45 PM"},
    {"id": 14, "patient": "Ishita Chawla", "doctor": "Dr. Anita Reddy", "date": "2025-08-28", "time": "09:30 AM"},
    {"id": 15, "patient": "Amit Yadav", "doctor": "Dr. Kavita Sharma", "date": "2025-08-29", "time": "03:15 PM"},
    {"id": 16, "patient": "Shreya Iyer", "doctor": "Dr. Meena Nair", "date": "2025-08-30", "time": "04:00 PM"},
    {"id": 17, "patient": "Harsh Patel", "doctor": "Dr. Rajesh Khanna", "date": "2025-09-01", "time": "10:20 AM"},
    {"id": 18, "patient": "Kavya Pillai", "doctor": "Dr. Anita Reddy", "date": "2025-09-02", "time": "11:50 AM"},
    {"id": 19, "patient": "Manish Kumar", "doctor": "Dr. Suresh Menon", "date": "2025-09-03", "time": "02:20 PM"},
    {"id": 20, "patient": "Divya Reddy", "doctor": "Dr. Meena Nair", "date": "2025-09-04", "time": "09:40 AM"},
    {"id": 21, "patient": "Arjun Sinha", "doctor": "Dr. Rajesh Khanna", "date": "2025-09-05", "time": "03:50 PM"},
    {"id": 22, "patient": "Ritika Roy", "doctor": "Dr. Kavita Sharma", "date": "2025-09-06", "time": "11:00 AM"},
    {"id": 23, "patient": "Nikhil Jain", "doctor": "Dr. Anita Reddy", "date": "2025-09-07", "time": "01:40 PM"},
    {"id": 24, "patient": "Tanya Paul", "doctor": "Dr. Meena Nair", "date": "2025-09-08", "time": "10:10 AM"},
    {"id": 25, "patient": "Saurabh Saxena", "doctor": "Dr. Suresh Menon", "date": "2025-09-09", "time": "04:20 PM"},
    {"id": 26, "patient": "Aishwarya Ghosh", "doctor": "Dr. Anita Reddy", "date": "2025-09-10", "time": "12:30 PM"},
    {"id": 27, "patient": "Vivek Nanda", "doctor": "Dr. Rajesh Khanna", "date": "2025-09-11", "time": "09:55 AM"},
    {"id": 28, "patient": "Renu Kaur", "doctor": "Dr. Meena Nair", "date": "2025-09-12", "time": "02:05 PM"},
    {"id": 29, "patient": "Anil Rathi", "doctor": "Dr. Kavita Sharma", "date": "2025-09-13", "time": "03:35 PM"},
    {"id": 30, "patient": "Sonal Kapoor", "doctor": "Dr. Anita Reddy", "date": "2025-09-14", "time": "10:25 AM"}
]

@router.get("/appointments", response_class=HTMLResponse)
async def get_appointments(request: Request):
    return templates.TemplateResponse(
        "appointments.html", 
        {"request": request, "appointments": appointments_data}
    )