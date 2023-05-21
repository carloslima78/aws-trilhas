
import boto3

def lambda_handler(event, context):
    nome = event['nome']
    idade = event['idade']

    # Cria uma instância do cliente do Amazon DynamoDB
    dynamodb_client = boto3.client('dynamodb')

    # Nome da tabela do Amazon DynamoDB
    table_name = 'Nome da tabela DynamoDB'

    # Insere os dados na tabela do Amazon DynamoDB
    dynamodb_client.put_item(
        TableName=table_name,
        Item={
            'Nome': {'S': nome},
            'Idade': {'N': str(idade)}
        }
    )

    return {
        'statusCode': 200,
        'body': 'Dados inseridos com sucesso na tabela DynamoDB.'
    }
