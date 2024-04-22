#def lambda_handler(event,context):
#    message=event['Records'][0]['body']
#    print(message)
#    return event
import json
import boto3
import time
s3 = boto3.client('s3')

def check_s3_object(bucket_name, object_key):
    try:
        response = s3.get_object(
            Bucket=bucket_name,
            Key=object_key
        )
        stored_message = json.loads(response['Body'].read())
        print("JSON object content:", stored_message)
        return stored_message
    except s3.exceptions.NoSuchKey:
        print("The JSON object does not exist in the specified location.")
        return None
    except Exception as e:
        print("Error:", e)
        return None

def lambda_handler(event, context):
    # Extract the message from the event
    message = event['Records'][0]['body']
    print("Received message:", message)
    
    # Convert the message to JSON format
    message_json = json.dumps({"message": message})
    
    # Define the S3 bucket where you want to store the JSON
    bucket_name = 's3-bucket-terr'
    
    # Construct the object key based on the folder path and filename in S3
    timestamp = str(int(time.time()))
    object_key = timestamp + '.json'
    
    try:
        # Put the JSON object into the S3 bucket
        response = s3.put_object(
            Body=message_json,
            Bucket=bucket_name,
            Key=object_key
        )
        print("Uploaded message to S3:", response)
        
        # Check the S3 bucket for the existence and content of the JSON object
        stored_message = check_s3_object(bucket_name, object_key)
        
        # Compare the sent message with the stored message
        if stored_message is not None and 'message' in stored_message:
            stored_message_value = stored_message['message']
            if message == stored_message_value:
                print("Sent message is the same as the stored message in S3.")
            else:
                print("Sent message is different from the stored message in S3.")
        else:
            print("Failed to retrieve the stored message from S3 or stored message is invalid.")
            
    except Exception as e:
        print("Error:", e)
    
    return event

