import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'messages':[
                {
                    'type':'unstructured',
                    'unstructured':
                        {
                        'text': 'Application under development. Search functionality will be implemented in Assignment 2'
                        }
                }
                ]
        }