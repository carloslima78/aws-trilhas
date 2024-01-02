
import boto3
import json

def lambda_handler(event, context):
    nome = event['nome']
    idade = event['idade']

    # Cria o conteúdo do arquivo JSON
    dados = {
        'nome': nome,
        'idade': idade
    }
    json_data = json.dumps(dados)

    # Nome do arquivo a ser criado no bucket
    nome_arquivo = 'cliente.json'

    # Nome do bucket do Amazon S3
    bucket_name = 'Nome do Bucket S3'

    # Cria uma instância do cliente do Amazon S3
    s3_client = boto3.client('s3')

    # Armazena o arquivo JSON no bucket do Amazon S3
    s3_client.put_object(
        Body=json_data,
        Bucket=bucket_name,
        Key=nome_arquivo
    )

    return {
        'statusCode': 200,
        'body': 'Arquivo JSON gerado e armazenado no bucket do S3.'
    }
