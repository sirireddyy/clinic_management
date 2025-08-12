from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static folder for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 template loader
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
doctors_data = [
    {"id": 1, "name": "Dr. Asha Iyer", "specialization": "Cardiology", "experience": "18 years", "phone": "+91-9810011001", "email": "asha.iyer@clinic.com", "clinic": "Sunrise Clinic, Hyderabad"},
    {"id": 2, "name": "Dr. Rohit Sharma", "specialization": "Orthopedics", "experience": "12 years", "phone": "+91-9810011002", "email": "rohit.sharma@clinic.com", "clinic": "GreenHealth, Pune"},
    {"id": 3, "name": "Dr. Priya Nair", "specialization": "Pediatrics", "experience": "9 years", "phone": "+91-9810011003", "email": "priya.nair@clinic.com", "clinic": "LittleCare, Chennai"},
    {"id": 4, "name": "Dr. Arjun Mehta", "specialization": "Neurology", "experience": "14 years", "phone": "+91-9810011004", "email": "arjun.mehta@clinic.com", "clinic": "NeuroPlus, Delhi"},
    {"id": 5, "name": "Dr. Sneha Kapoor", "specialization": "Dermatology", "experience": "8 years", "phone": "+91-9810011005", "email": "sneha.kapoor@clinic.com", "clinic": "SkinCare Hub, Mumbai"},
    {"id": 6, "name": "Dr. Mohit Verma", "specialization": "ENT", "experience": "11 years", "phone": "+91-9810011006", "email": "mohit.verma@clinic.com", "clinic": "HealWell ENT, Jaipur"},
    {"id": 7, "name": "Dr. Kavita Desai", "specialization": "Gynecology", "experience": "13 years", "phone": "+91-9810011007", "email": "kavita.desai@clinic.com", "clinic": "MotherCare, Ahmedabad"},
    {"id": 8, "name": "Dr. Vinay Gupta", "specialization": "General Medicine", "experience": "22 years", "phone": "+91-9810011008", "email": "vinay.gupta@clinic.com", "clinic": "Vida Clinic, Kolkata"},
    {"id": 9, "name": "Dr. Alok Pandey", "specialization": "Psychiatry", "experience": "10 years", "phone": "+91-9810011009", "email": "alok.pandey@clinic.com", "clinic": "MindCare, Lucknow"},
    {"id": 10, "name": "Dr. Meera Nair", "specialization": "Ophthalmology", "experience": "16 years", "phone": "+91-9810011010", "email": "meera.nair@clinic.com", "clinic": "VisionPlus, Kochi"},
    {"id": 11, "name": "Dr. Rajesh Kumar", "specialization": "Cardiology", "experience": "20 years", "phone": "+91-9810011011", "email": "rajesh.kumar@clinic.com", "clinic": "HeartLine, Delhi"},
    {"id": 12, "name": "Dr. Ananya Rao", "specialization": "Pediatrics", "experience": "7 years", "phone": "+91-9810011012", "email": "ananya.rao@clinic.com", "clinic": "KidsCare, Bangalore"},
    {"id": 13, "name": "Dr. Sandeep Joshi", "specialization": "Orthopedics", "experience": "15 years", "phone": "+91-9810011013", "email": "sandeep.joshi@clinic.com", "clinic": "BoneFix, Pune"},
    {"id": 14, "name": "Dr. Kavya Menon", "specialization": "Dermatology", "experience": "6 years", "phone": "+91-9810011014", "email": "kavya.menon@clinic.com", "clinic": "DermaCare, Trivandrum"},
    {"id": 15, "name": "Dr. Rohan Singh", "specialization": "ENT", "experience": "9 years", "phone": "+91-9810011015", "email": "rohan.singh@clinic.com", "clinic": "Ear & Nose Clinic, Faridabad"},
    {"id": 16, "name": "Dr. Lata Bhat", "specialization": "Gynecology", "experience": "17 years", "phone": "+91-9810011016", "email": "lata.bhat@clinic.com", "clinic": "WomenCare, Surat"},
    {"id": 17, "name": "Dr. Manish Kapoor", "specialization": "General Medicine", "experience": "5 years", "phone": "+91-9810011017", "email": "manish.kapoor@clinic.com", "clinic": "Wellness Hub, Noida"},
    {"id": 18, "name": "Dr. Priyanka Dutta", "specialization": "Psychiatry", "experience": "12 years", "phone": "+91-9810011018", "email": "priyanka.dutta@clinic.com", "clinic": "PeaceMind, Kolkata"},
    {"id": 19, "name": "Dr. Karan Malhotra", "specialization": "Ophthalmology", "experience": "8 years", "phone": "+91-9810011019", "email": "karan.malhotra@clinic.com", "clinic": "EyeCare, Indore"},
    {"id": 20, "name": "Dr. Shreya Ghosh", "specialization": "Cardiology", "experience": "11 years", "phone": "+91-9810011020", "email": "shreya.ghosh@clinic.com", "clinic": "HeartCare, Ranchi"},
    {"id": 21, "name": "Dr. Saurabh Patel", "specialization": "Nephrology", "experience": "14 years", "phone": "+91-9810011021", "email": "saurabh.patel@clinic.com", "clinic": "KidneyCare, Vadodara"},
    {"id": 22, "name": "Dr. Nisha Sharma", "specialization": "Endocrinology", "experience": "9 years", "phone": "+91-9810011022", "email": "nisha.sharma@clinic.com", "clinic": "HormoneCare, Bhopal"},
    {"id": 23, "name": "Dr. Abhishek Rao", "specialization": "Pulmonology", "experience": "10 years", "phone": "+91-9810011023", "email": "abhishek.rao@clinic.com", "clinic": "LungHealth, Hyderabad"},
    {"id": 24, "name": "Dr. Jyoti Bhatt", "specialization": "Rheumatology", "experience": "13 years", "phone": "+91-9810011024", "email": "jyoti.bhatt@clinic.com", "clinic": "JointCare, Ahmedabad"},
    {"id": 25, "name": "Dr. Vikram Chawla", "specialization": "Gastroenterology", "experience": "18 years", "phone": "+91-9810011025", "email": "vikram.chawla@clinic.com", "clinic": "Digestive Health, Mumbai"},
    {"id": 26, "name": "Dr. Meera Bhatia", "specialization": "Oncology", "experience": "21 years", "phone": "+91-9810011026", "email": "meera.bhatia@clinic.com", "clinic": "CancerCare, Delhi"},
    {"id": 27, "name": "Dr. Sangeeta Reddy", "specialization": "Pediatrics", "experience": "10 years", "phone": "+91-9810011027", "email": "sangeeta.reddy@clinic.com", "clinic": "ChildCare, Hyderabad"},
    {"id": 28, "name": "Dr. Devansh Jain", "specialization": "Orthopedics", "experience": "7 years", "phone": "+91-9810011028", "email": "devansh.jain@clinic.com", "clinic": "BoneCare, Jodhpur"},
    {"id": 29, "name": "Dr. Anjali Menon", "specialization": "Dermatology", "experience": "6 years", "phone": "+91-9810011029", "email": "anjali.menon@clinic.com", "clinic": "SkinClinic, Kochi"},
    {"id": 30, "name": "Dr. Prakash Rao", "specialization": "ENT", "experience": "19 years", "phone": "+91-9810011030", "email": "prakash.rao@clinic.com", "clinic": "ENT Care, Visakhapatnam"},
    {"id": 31, "name": "Dr. Ritu Verma", "specialization": "Gynecology", "experience": "8 years", "phone": "+91-9810011031", "email": "ritu.verma@clinic.com", "clinic": "Women's Health, Lucknow"},
    {"id": 32, "name": "Dr. Ashok Gupta", "specialization": "General Medicine", "experience": "25 years", "phone": "+91-9810011032", "email": "ashok.gupta@clinic.com", "clinic": "CityMed, Surat"},
    {"id": 33, "name": "Dr. Nandini Kulkarni", "specialization": "Psychiatry", "experience": "11 years", "phone": "+91-9810011033", "email": "nandini.kulkarni@clinic.com", "clinic": "MindSpace, Pune"},
    {"id": 34, "name": "Dr. Harish Sharma", "specialization": "Ophthalmology", "experience": "13 years", "phone": "+91-9810011034", "email": "harish.sharma@clinic.com", "clinic": "EyeCare, Jaipur"},
    {"id": 35, "name": "Dr. Rekha Rao", "specialization": "Cardiology", "experience": "17 years", "phone": "+91-9810011035", "email": "rekha.rao@clinic.com", "clinic": "Heart Specialist, Bangalore"},
    {"id": 36, "name": "Dr. Kunal Mehra", "specialization": "Nephrology", "experience": "9 years", "phone": "+91-9810011036", "email": "kunal.mehra@clinic.com", "clinic": "Kidney Clinic, Chennai"},
    {"id": 37, "name": "Dr. Sheetal Desai", "specialization": "Endocrinology", "experience": "12 years", "phone": "+91-9810011037", "email": "sheetal.desai@clinic.com", "clinic": "HormoneCare, Vadodara"},
    {"id": 38, "name": "Dr. Amitabh Roy", "specialization": "Pulmonology", "experience": "15 years", "phone": "+91-9810011038", "email": "amitabh.roy@clinic.com", "clinic": "BreathWell, Kolkata"},
    {"id": 39, "name": "Dr. Pooja Jain", "specialization": "Rheumatology", "experience": "8 years", "phone": "+91-9810011039", "email": "pooja.jain@clinic.com", "clinic": "Joint Relief, Bhopal"},
    {"id": 40, "name": "Dr. Sanjay Nair", "specialization": "Gastroenterology", "experience": "14 years", "phone": "+91-9810011040", "email": "sanjay.nair@clinic.com", "clinic": "Digestive Care, Kochi"},
    {"id": 41, "name": "Dr. Kavinder Singh", "specialization": "Oncology", "experience": "20 years", "phone": "+91-9810011041", "email": "kavinder.singh@clinic.com", "clinic": "OncoCenter, Amritsar"},
    {"id": 42, "name": "Dr. Sima Khanna", "specialization": "Pediatrics", "experience": "11 years", "phone": "+91-9810011042", "email": "sima.khanna@clinic.com", "clinic": "Child Health, Chandigarh"},
    {"id": 43, "name": "Dr. Vikrant Bedi", "specialization": "Orthopedics", "experience": "16 years", "phone": "+91-9810011043", "email": "vikrant.bedi@clinic.com", "clinic": "OrthoPlus, Ludhiana"},
    {"id": 44, "name": "Dr. Radhika Menon", "specialization": "Dermatology", "experience": "9 years", "phone": "+91-9810011044", "email": "radhika.menon@clinic.com", "clinic": "Skin Solutions, Thrissur"},
    {"id": 45, "name": "Dr. Praveen Kaur", "specialization": "ENT", "experience": "10 years", "phone": "+91-9810011045", "email": "praveen.kaur@clinic.com", "clinic": "EarCare, Amritsar"},
    {"id": 46, "name": "Dr. Rakesh Tiwari", "specialization": "Gynecology", "experience": "12 years", "phone": "+91-9810011046", "email": "rakesh.tiwari@clinic.com", "clinic": "Mother & Child, Kanpur"},
    {"id": 47, "name": "Dr. Smita Rao", "specialization": "General Medicine", "experience": "7 years", "phone": "+91-9810011047", "email": "smita.rao@clinic.com", "clinic": "CarePoint, Nagpur"},
    {"id": 48, "name": "Dr. Anil Joshi", "specialization": "Psychiatry", "experience": "19 years", "phone": "+91-9810011048", "email": "anil.joshi@clinic.com", "clinic": "MindCare Center, Pune"},
    {"id": 49, "name": "Dr. Divya Kapoor", "specialization": "Ophthalmology", "experience": "6 years", "phone": "+91-9810011049", "email": "divya.kapoor@clinic.com", "clinic": "Vision Clinic, New Delhi"},
    {"id": 50, "name": "Dr. Sandeep Malhotra", "specialization": "Cardiology", "experience": "23 years", "phone": "+91-9810011050", "email": "sandeep.malhotra@clinic.com", "clinic": "HeartCare Center, Gurugram"},
]

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

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/appointments", response_class=HTMLResponse)
async def appointments(request: Request):
    return templates.TemplateResponse("appointments.html", {"request": request, "appointments": appointments_data})

@app.get("/patients", response_class=HTMLResponse)
async def patients(request: Request):
    return templates.TemplateResponse("patients.html", {"request": request, "patients": patients_data})

@app.get("/doctors", response_class=HTMLResponse)
async def doctors(request: Request):
    return templates.TemplateResponse("doctors.html", {"request": request, "doctors": doctors_data})