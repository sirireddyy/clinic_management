from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

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
@router.get("/doctors", response_class=HTMLResponse)
async def get_doctors(request: Request):
    return templates.TemplateResponse(
        "doctors.html", 
        {"request": request, "doctors": doctors_data}
    )