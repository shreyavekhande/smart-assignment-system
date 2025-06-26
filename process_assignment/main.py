import base64
import json
from google.cloud import bigquery
from datetime import datetime

def process_assignment(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    data = json.loads(pubsub_message)

    file_name = data['file_name']

    # Dummy OCR values (replace later)
    student_name = "Sample Student"
    roll_no = "VIT2023CS001"
    marks = 85

    client = bigquery.Client()
    table_id = "stalwart-method-462107-m8.assignment_data.submissions"

    rows = [{
        "file_name": file_name,
        "student_name": student_name,
        "roll_no": roll_no,
        "marks": marks,
        "upload_time": datetime.utcnow().isoformat()
    }]

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        print(f"BigQuery insert failed: {errors}")
    else:
        print(f"Inserted into BigQuery: {rows}")
