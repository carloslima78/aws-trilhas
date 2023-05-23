
import boto3
import json

def lambda_handler(event, context):
    # Nome do bucket do Amazon S3
    bucket_name = 'nome-do-bucket-s3'

    # Nome do arquivo JSON a ser lido
    nome_arquivo = 'dados.json'

    # Configuração do cliente do Amazon S3
    s3_client = boto3.client('s3')

    # Recupera o arquivo JSON do bucket do Amazon S3
    response = s3_client.get_object(
        Bucket=bucket_name,
        Key=nome_arquivo
    )

    # Extrai os dados do conteúdo do arquivo
    json_data = response['Body'].read().decode('utf-8')
    dados = json.loads(json_data)

    # Obtém os valores de nome e idade
    nome = dados['nome']
    idade = dados['idade']

    # Imprime os dados lidos
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

    return {
        'statusCode': 200,
        'body': 'Dados lidos com sucesso do arquivo JSON.'
    }
