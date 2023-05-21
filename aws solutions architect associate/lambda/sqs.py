
import boto3
import json

def lambda_handler(event, context):
    nome = event['nome']
    idade = event['idade']

    # Cria uma instância do cliente do Amazon SQS
    sqs_client = boto3.client('sqs')

    # URL da fila do Amazon SQS
    queue_url = 'URL da fila SQS'

    # Cria a mensagem a ser enviada para a fila
    mensagem = {
        'nome': nome,
        'idade': idade
    }

    # Envio da mensagem para a fila do Amazon SQS
    sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(mensagem)
    )

    return {
        'statusCode': 200,
        'body': 'Dados enviados com sucesso para a fila SQS.'
    }
