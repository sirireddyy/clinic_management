from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")
patients_data = [
    {"id": 1, "name": "Aarav Sharma", "age": 34, "gender": "Male", "contact": "9876543210"},
    {"id": 2, "name": "Priya Verma", "age": 28, "gender": "Female", "contact": "9123456780"},
    {"id": 3, "name": "Ravi Kumar", "age": 45, "gender": "Male", "contact": "9988776655"},
    {"id": 4, "name": "Neha Gupta", "age": 31, "gender": "Female", "contact": "9876501234"},
    {"id": 5, "name": "Anil Yadav", "age": 39, "gender": "Male", "contact": "9012345678"},
    {"id": 6, "name": "Kiran Patel", "age": 29, "gender": "Female", "contact": "9823456789"},
    {"id": 7, "name": "Vikram Singh", "age": 40, "gender": "Male", "contact": "9776543210"},
    {"id": 8, "name": "Sonia Kapoor", "age": 36, "gender": "Female", "contact": "9654321789"},
    {"id": 9, "name": "Manoj Mehta", "age": 50, "gender": "Male", "contact": "9898989898"},
    {"id": 10, "name": "Pooja Nair", "age": 33, "gender": "Female", "contact": "9123451234"},
    {"id": 11, "name": "Ramesh Chauhan", "age": 55, "gender": "Male", "contact": "9345678901"},
    {"id": 12, "name": "Anita Joshi", "age": 47, "gender": "Female", "contact": "9543216789"},
    {"id": 13, "name": "Suresh Iyer", "age": 37, "gender": "Male", "contact": "9789123456"},
    {"id": 14, "name": "Ritika Malhotra", "age": 26, "gender": "Female", "contact": "9897654321"},
    {"id": 15, "name": "Kunal Desai", "age": 32, "gender": "Male", "contact": "9765432198"},
    {"id": 16, "name": "Deepa Menon", "age": 41, "gender": "Female", "contact": "9432156789"},
    {"id": 17, "name": "Arjun Reddy", "age": 35, "gender": "Male", "contact": "9555123456"},
    {"id": 18, "name": "Meera Krishnan", "age": 30, "gender": "Female", "contact": "9786453210"},
    {"id": 19, "name": "Rajesh Pillai", "age": 44, "gender": "Male", "contact": "9874563210"},
    {"id": 20, "name": "Shreya Choudhary", "age": 29, "gender": "Female", "contact": "9632587410"},
    {"id": 21, "name": "Amit Sharma", "age": 52, "gender": "Male", "contact": "9988771122"},
    {"id": 22, "name": "Lakshmi Nair", "age": 38, "gender": "Female", "contact": "9877123456"},
    {"id": 23, "name": "Gaurav Bhatia", "age": 33, "gender": "Male", "contact": "9456789012"},
    {"id": 24, "name": "Sneha Kapoor", "age": 27, "gender": "Female", "contact": "9123987654"},
    {"id": 25, "name": "Rahul Khanna", "age": 42, "gender": "Male", "contact": "9876001234"},
    {"id": 26, "name": "Divya Sethi", "age": 31, "gender": "Female", "contact": "9546783210"},
    {"id": 27, "name": "Sameer Joshi", "age": 46, "gender": "Male", "contact": "9745632109"},
    {"id": 28, "name": "Ananya Roy", "age": 28, "gender": "Female", "contact": "9876123450"},
    {"id": 29, "name": "Harish Kumar", "age": 39, "gender": "Male", "contact": "9345678123"},
    {"id": 30, "name": "Tanya Mehta", "age": 34, "gender": "Female", "contact": "9765123456"},
    {"id": 31, "name": "Sanjay Verma", "age": 53, "gender": "Male", "contact": "9988012345"},
    {"id": 32, "name": "Nidhi Rani", "age": 25, "gender": "Female", "contact": "9823456123"},
    {"id": 33, "name": "Vivek Anand", "age": 36, "gender": "Male", "contact": "9632109876"},
    {"id": 34, "name": "Komal Yadav", "age": 32, "gender": "Female", "contact": "9543210987"},
    {"id": 35, "name": "Ashok Patil", "age": 40, "gender": "Male", "contact": "9765432109"},
    {"id": 36, "name": "Pallavi Dixit", "age": 29, "gender": "Female", "contact": "9876098765"},
    {"id": 37, "name": "Mohan Lal", "age": 48, "gender": "Male", "contact": "9988776654"},
    {"id": 38, "name": "Chhavi Agarwal", "age": 30, "gender": "Female", "contact": "9123456789"},
    {"id": 39, "name": "Ajay Tiwari", "age": 37, "gender": "Male", "contact": "9765012345"},
    {"id": 40, "name": "Renu Bajaj", "age": 41, "gender": "Female", "contact": "9654321098"},
    {"id": 41, "name": "Vishal Kumar", "age": 34, "gender": "Male", "contact": "9543109876"},
    {"id": 42, "name": "Smita Shah", "age": 28, "gender": "Female", "contact": "9876543120"},
    {"id": 43, "name": "Siddharth Sinha", "age": 46, "gender": "Male", "contact": "9988123456"},
    {"id": 44, "name": "Preeti Kaur", "age": 33, "gender": "Female", "contact": "9654321870"},
    {"id": 45, "name": "Lokesh Bansal", "age": 39, "gender": "Male", "contact": "9432109876"},
    {"id": 46, "name": "Shruti Deshpande", "age": 27, "gender": "Female", "contact": "9876123098"},
    {"id": 47, "name": "Aditya Malhotra", "age": 38, "gender": "Male", "contact": "9543012789"},
    {"id": 48, "name": "Bhavna Jain", "age": 31, "gender": "Female", "contact": "9786012345"},
    {"id": 49, "name": "Rohit Kapoor", "age": 35, "gender": "Male", "contact": "9765432876"},
    {"id": 50, "name": "Shalini Reddy", "age": 29, "gender": "Female", "contact": "9876012789"},
]
@router.get("/patients", response_class=HTMLResponse)
async def get_patients(request: Request):
    return templates.TemplateResponse(
        "patients.html", 
        {"request": request, "patients": patients_data}
    )