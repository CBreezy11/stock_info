import boto3
def lambda_handler(event, context):
    table=boto3.resource('dynamodb').Table('InsiderTrading')
    item = table.get_item(Key = {'company_name':"NVDA"})
    return  item