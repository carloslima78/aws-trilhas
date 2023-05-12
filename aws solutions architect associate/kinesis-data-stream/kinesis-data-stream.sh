#!/bin/bash

# Verifica a versão do CLI
aws --version

# Acesso a conta AWS ---------------------------------------------------------------------------

aws configure

    AWS Access Key ID [****************]: sua access key id
    AWS Secret Access Key [****************]: sus access key
    Default region name [us-east-1]: 
    Default output format [json]: 


# Producer ------------------------------------------------------------------------------------

# CLI v2
# Produz dados no Stream utilizando a API "put-record"
aws kinesis put-record --stream-name meu-stream --partition-key minha-particao --data "testando a entrada de dados" --cli-binary-format raw-in-base64-out

# CLI v1
# Produz dados no Stream utilizando a API "put-record"
aws kinesis put-record --stream-name meu-stream --partition-key minha-particao --data "testando a entrada de dados"


# Consumer -------------------------------------------------------------------------------------

# Descreve o Stream usando a API "kinesis describe-stream"
aws kinesis describe-stream --stream-name meu-stream

# Retorna a chave "ShardIterator" usando a API "get-shard-iterator" 
aws kinesis get-shard-iterator --stream-name meu-stream --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON

# Consome os dados do Stream com base no ShardIterator retornado na chamada a API "get-shard-iterator"
# Use o "https://www.base64decode.org/" para decodificar o dado do Stream no campo "Data" que estará criptografado
aws kinesis get-records --shard-iterator chave-shard-iterator