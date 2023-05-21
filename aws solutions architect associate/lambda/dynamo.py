import json
import boto3

# Importante: Criar um IAM Role (Função) anexando um IAM Policy (Política) que permite interação com o DynamoDB a Lambda

def lambda_handler(event, context):
    
    # JSON de entrada
    json_input = {
        "id_cliente": "1",
        "nome_cliente": "Carlos Lima",
        "email_cliente": "carlos.lima@example.com",s
        "pedidos": [
            {
                "pedido_id": "101",
                "pedido_data": "2023-05-20",
                "valor_total_pedido": "100.00",
                "produtos": [
                    {
                        "id": "12",
                        "nome": "TV",
                        "preco": "5000.00"
                    },
                    {
                        "id": "13",
                        "nome": "Game",
                        "preco": "5000.00"
                    }
                ],
                "meio_pagamento": {
                    "id": "1",
                    "nome": "Cartão de Crédito"
                },
                "status_pedido": "Pendente"
            },
            {
                "pedido_id": "102",
                "pedido_data": "2023-05-21",
                "valor_total_pedido": "200.00",
                "produtos": [
                    {
                        "id": "14",
                        "nome": "Livro",
                        "preco": "50.00"
                    },
                    {
                        "id": "15",
                        "nome": "Câmera",
                        "preco": "150.00"
                    }
                ],
                "meio_pagamento": {
                    "id": "2",
                    "nome": "Boleto Bancário"
                },
                "status_pedido": "Aprovado"
            }
        ]
    }

    # Converte o JSON de resultado em uma string
    json_output = json.dumps(json_input)

    # Configuração do cliente do Amazon DynamoDB
    dynamodb_client = boto3.client('dynamodb')

    # Inserção do JSON de resultado na tabela do DynamoDB
    response = dynamodb_client.put_item(
        TableName = 'pedidos',
        Item = {

            # O id_cliente é a chave de particão da tabela
            'id_cliente': {'S': json_input['id_cliente']},
            'resultado': {'S': json_output}
        }
    )

    # Retorna a resposta da inserção
    return {
        'statusCode': 200,
        'body': 'JSON de resultado inserido na tabela DynamoDB com sucesso.'
    }

