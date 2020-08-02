import json
import boto3
import urllib3

def lambda_handler(event, context):
    
    # TODO implement
    url="http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Amazon_Instant_Video_5.json.gz"
    bucket = 'thanga-delete' #your s3 bucket
    key = 'testing/sales.zip' #your desired s3 path or filename

    s3=boto3.client('s3')
    http=urllib3.PoolManager()
    s3.upload_fileobj(http.request('GET', url,preload_content=False), bucket, key)
    return {
        'statusCode': 2000,
        'body': json.dumps('Hello from Lambda!')
    }
