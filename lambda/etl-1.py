
import json

def lambda_handler(event, context):
   
    # JSON de entrada
    json_input = {
        "idpedido": "11",
        "idcliente": "1",
        "nome": "Carlos Lima",
        "email": "carlos.lima@gmail.com",
        "telefone": "+55 11 99999-9999",
        "total": "10.000.00",
        "produtos": [
            {
                "idproduto": "12",
                "nome": "TV",
                "valor": "5000.00"
            },
            {
                "idproduto": "13",
                "nome": "Game",
                "valor": "5000.00"
            }
        ]
    }

    # Transformação dos dados
    json_output = {
        "pedido": json_input["idpedido"],
        "cliente": json_input["nome"],
        "total": json_input["total"],
        "quantidadeprodutos": str(len(json_input["produtos"]))
    }

    # Retorna o JSON transformado
    return {
        'statusCode': 200,
        'body': json.dumps(json_output)
    }
