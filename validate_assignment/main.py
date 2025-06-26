import json
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("stalwart-method-462107-m8", "assignment-upload-topic")

def validate_assignment(event, context):
    file = event
    file_name = file['name']
    if not file_name.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg')):
        print(f"Ignored unsupported file: {file_name}")
        return

    size = int(file['size'])
    if size > 10 * 1024 * 1024:
        print("File too large")
        return

    payload = {
        "file_name": file_name,
        "bucket": file['bucket'],
        "size": size
    }

    publisher.publish(topic_path, json.dumps(payload).encode('utf-8'))
    print(f"Published metadata for {file_name}")
