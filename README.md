# 📚 Smart Assignment Submission System (GCP-Based)

A beginner-friendly cloud-based system to help students upload assignments and automatically extract and store metadata using **Google Cloud Platform (GCP)** services.

---

## 🚀 Features

- 📤 Upload assignments (PDFs/images) via Cloud Storage
- ⚙️ Auto-triggered Cloud Function on file upload
- 🔎 Validates file type, size (can later include plagiarism check)
- 🧠 Extracts or simulates student info: name, roll number, marks
- 📊 Stores metadata in BigQuery
- 🔔 Uses Pub/Sub to decouple processing logic
---

## 🔧 GCP Services Used

| GCP Service        | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| ☁️ Cloud Storage    | Store uploaded assignment PDFs/images manually                              |
| ⚙️ Cloud Functions  | Validate file & simulate OCR → publish/consume from Pub/Sub                 |
| 🔔 Pub/Sub          | Decouples file validation from metadata processing                          |
| 📊 BigQuery         | Store structured data: filename, student name, roll number, marks, timestamp |

---

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/shreyavekhande/smart-assignment-system.git
cd smart-assignment-system

# Install dependencies (if running locally for tests)
pip install -r requirements.txt

# Deploy validate_assignment function
gcloud functions deploy validate_assignment \
  --runtime python310 \
  --trigger-resource assignment-upload-bucket \
  --trigger-event google.storage.object.finalize \
  --entry-point validate_assignment \
  --region us-central1

# Deploy process_assignment function
gcloud functions deploy process_assignment \
  --runtime python310 \
  --trigger-topic assignment-upload-topic \
  --entry-point process_assignment \
  --region us-central1
---

## 📂 Project Structure


smart-assignment-system/
├── validate_assignment/
│   ├── main.py              # Validates file and publishes to Pub/Sub
│   └── requirements.txt
├── process_assignment/
│   ├── main.py              # Simulates OCR and inserts into BigQuery
│   └── requirements.txt
├── screenshots/             # Optional: logs and output proof
└── README.md                # Project overview and setup instructions


---

## 🙋‍♀️ Made by

*Shreya Vekhande*  
🎓 Electronics & Computer Science Graduate  
📬 [shreyavekhande7496@gmail.com](mailto:shreyavekhande7496@gmail.com)

---
