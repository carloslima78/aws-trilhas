
import boto3
import json

def lambda_handler(event, context):
    nome = event['nome']
    idade = event['idade']

    # Cria uma instância do cliente do Amazon SNS
    sns_client = boto3.client('sns')

    # ARN do tópico do Amazon SNS
    topic_arn = 'ARN do tópico SNS'

    # Publica a mensagem no tópico do Amazon SNS
    sns_client.publish(
        TopicArn=topic_arn,
        Message=json.dumps(mensagem)
    )

    return {
        'statusCode': 200,
        'body': 'Dados publicados com sucesso no tópico SNS.'
    }
