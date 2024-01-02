
# Comando para instalar o stress.
sudo yum update -y
sudo amazon-linux-extras install epel -y
sudo yum install stress -y

# Comando para teste de carga na instância EC2, criando 4 threads para simular atividade de processamento intenso na CPU
sudo stress -c 4

# Remove a instalação
sudo yum remove stress stress-ng