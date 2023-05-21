
import pymysql

def lambda_handler(event, context):
    nome = event['nome']
    idade = event['idade']

    # Configurações de conexão com o banco de dados RDS
    db_endpoint = 'ENDPOINT_DO_BANCO_DE_DADOS'
    db_username = 'USUARIO'
    db_password = 'SENHA'
    db_name = 'NOME_DO_BANCO_DE_DADOS'

    # Cria uma conexão com o banco de dados RDS
    conn = pymysql.connect(
        host=db_endpoint,
        user=db_username,
        password=db_password,
        database=db_name
    )

    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Insere os dados na tabela do banco de dados
    sql = "INSERT INTO tabela (nome, idade) VALUES (%s, %s)"
    values = (nome, idade)
    cursor.execute(sql, values)

    # Confirma a transação
    conn.commit()

    # Fecha a conexão com o banco de dados
    conn.close()

    return {
        'statusCode': 200,
        'body': 'Dados inseridos com sucesso na tabela do RDS.'
    }
