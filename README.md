# 🚗 Automatic Vehicle Number Plate Recognition System  

## 📌 **Project Overview**  
This project is a **Vehicle Number Plate Recognition System** that uses **OpenCV** and **Tesseract OCR** to detect and extract vehicle registration numbers from images or CCTV camera footage. The extracted data is stored in an **SQLite database** or **Excel sheet** for further analysis.

---

## 🔥 **Features**  
✅ Detects vehicle number plates using **Haar Cascade Classifier**  
✅ Extracts text from number plates using **Tesseract OCR**  
✅ Saves extracted vehicle numbers with **date and time** in an **SQLite database**  
✅ Option to export records to **Excel (CSV file)**  
✅ Supports **live feed from a CCTV camera or webcam**  
✅ Simple and efficient **Flask web interface** for viewing records  

---

## 🛠️ **Technologies Used**  
- **Python** (Main Programming Language)  
- **OpenCV** (Image Processing & Detection)  
- **Tesseract OCR** (Optical Character Recognition for Text Extraction)  
- **SQLite** (Database for Storing Records)  
- **Flask** (Web Interface for Viewing Records)  
- **Pandas** (Exporting Data to CSV)  

---

## 📂 **Project Structure**  
```
📂 Vehicle-Number-Plate-Recognition/
│── 📜 main.py                     # Main script for real-time detection
│── 📜 detect_plate.py              # Function for detecting number plates
│── 📜 extract_text.py              # OCR script for extracting text from plates
│── 📜 database.py                   # Database operations (SQLite)
│── 📜 export_data.py                # Script to export data to CSV
│── 📜 app.py                        # Flask web application
│── 📜 initialize_db.py              # Script to initialize the database
│── 📜 requirements.txt              # List of dependencies
│── 📜 README.md                     # Documentation
│── 📂 static/                        # Static files (CSS, JS, Images)
│── 📂 templates/                     # HTML files for Flask web app
│── 📂 dataset/                       # Sample images of number plates
│── 📜 haarcascade_russian_plate_number.xml  # Haar Cascade Model
│── 📜 database.db                    # SQLite Database
```

---

## 📦 **Installation & Setup**  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/prangowda/Vehicle-Number-Plate-Recognition.git
cd Vehicle-Number-Plate-Recognition
```

### **2️⃣ Install Dependencies**
Make sure you have **Python 3.x** installed. Then install the required packages:
```bash
pip install -r requirements.txt
```

### **3️⃣ Download & Install Tesseract OCR**
Tesseract OCR is required for text extraction from number plates.  
🔗 **[Download Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)**  
After installing, add Tesseract to your system PATH.

### **4️⃣ Initialize the Database**
```bash
python initialize_db.py
```
This will create `database.db` and a table for storing vehicle number records.

### **5️⃣ Run the Main Script**
To start real-time vehicle number plate detection, run:
```bash
python main.py
```
It will open the webcam or connect to a CCTV feed and start detecting number plates.

### **6️⃣ Run the Flask Web App (Optional)**
To view stored vehicle records in a web interface:
```bash
python app.py
```
Open **http://127.0.0.1:5000/** in your browser.

---

## 📌 **How It Works**  
1️⃣ The script captures **real-time video frames** from the webcam/CCTV camera.  
2️⃣ It uses **Haar Cascade Classifier** to detect **vehicle number plates**.  
3️⃣ The detected plate is passed through **Tesseract OCR** to extract text.  
4️⃣ The extracted text is **stored in an SQLite database** with **date & time**.  
5️⃣ The Flask web app allows **viewing and exporting** stored records.  

---

## 📸 **Example Output**  
**Input Image:**  
🚗 _A vehicle with a visible number plate_  

**Detected Plate:**  
📸 _A cropped image of the number plate_  

**Extracted Text:**  
📝 `KA 05 AB 1234`  

**Stored in Database:**  
| ID  | Plate Number | Date & Time          |
|-----|-------------|----------------------|
| 1   | KA 05 AB 1234  | 2025-02-12 14:30:00 |

---

## 🛡️ **Security & Enhancements**  
- 🚀 Improve detection accuracy using **Deep Learning models (YOLO, SSD, Faster R-CNN)**  
- 🔒 Encrypt the database for **secure storage of vehicle data**  
- 🌐 Deploy the system on **cloud servers** for remote monitoring  
- 📱 Create a **mobile app** for real-time notifications  

