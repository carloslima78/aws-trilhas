
import json

def lambda_handler(event, context):
    
    # JSON de entrada
    json_input = {
        "cliente": {
            "id": "1",
            "nome": "Carlos Lima",
            "email": "carlos.lima@gmail.com"
        },
        "pedidos": [
            {
                "id": "101",
                "data": "2023-05-20",
                "valor_total": "100.00",
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
                "status": "Pendente"
            },
            {
                "id": "102",
                "data": "2023-05-21",
                "valor_total": "200.00",
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
                "status": "Aprovado"
            }
        ]
    }

    # Transformação dos dados
    cliente_id = json_input["cliente"]["id"]
    cliente_nome = json_input["cliente"]["nome"]
    cliente_email = json_input["cliente"]["email"]
    pedidos = []

    for pedido in json_input["pedidos"]:
        pedido_id = pedido["id"]
        pedido_data = pedido["data"]
        pedido_valor_total = pedido["valor_total"]
        produtos = pedido["produtos"]
        meio_pagamento = pedido["meio_pagamento"]
        status = pedido["status"]

        pedido_transformado = {
            "pedido_id": pedido_id,
            "pedido_data": pedido_data,
            "valor_total_pedido": pedido_valor_total,
            "produtos": produtos,
            "meio_pagamento": meio_pagamento,
            "status_pedido": status
        }

        pedidos.append(pedido_transformado)

    # Cria um novo objeto com os dados transformados
    json_output = {
        "id_cliente": cliente_id,
        "nome_cliente": cliente_nome,
        "email_cliente": cliente_email,
        "pedidos": pedidos
    }

    # Retorna o JSON transformado
    return {
        'statusCode': 200,
        'body': json.dumps(json_output)
    }
