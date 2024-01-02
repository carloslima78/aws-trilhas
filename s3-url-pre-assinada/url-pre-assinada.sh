
# Comando para gerar a URL pré assinada
aws s3 presign s3://meubucket/meuobjeto --region minharegiao

# Comando para gerar uma URL pré assinada com tempo de expiração em segundos
aws s3 presign s3://meubucket/meuobjeto --expires-in 300 --region minharegiao

