import boto3
import os

# table_name = os.environ['tableName']
resource = boto3.resource('dynamodb')
client   = boto3.client('dynamodb')
# table    = resource.Table(table_name)

# dynamoDb = {
#     "get": table.get_item,
#     "put": table.put_item,
#     "query": table.query,
#     "update": table.update_item,
#     "delete": table.delete_item
# }