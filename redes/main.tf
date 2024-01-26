
# Configurando o provedor AWS
provider "aws" {
  # Defina a região desejada
  region = "us-east-1" 
}

# Criando uma VPC
resource "aws_vpc" "minha-vpc" {
  
  # Defina a faixa de IP desejada; nesta VPC, teremos 65.536 endereços IP disponíveis
  cidr_block = "10.0.0.0/16" 

  # Adicionando tags para identificação
  tags = {
    Name = "MinhaVPC"
  }
}

# Criando uma subnet pública
resource "aws_subnet" "minha-subnet-publica" {
  
  # Vinculando à VPC criada anteriormente
  vpc_id                  = aws_vpc.minha-vpc.id
  
  # Definindo a faixa de IP para a subnet pública
  cidr_block              = "10.0.1.0/24" 
  
  # Especificando a zona de disponibilidade desejada
  availability_zone       = "us-east-1a"   
  
  # Configuração para permitir que instâncias associadas recebam IPs públicos automaticamente 
  map_public_ip_on_launch = true

  # Adicionando tags para identificação
  tags = {
    Name = "SubnetPublica"
  }
}

# Criando uma subnet privada
resource "aws_subnet" "minha-subnet-privada" {
  
  # Vinculando à VPC criada anteriormente
  vpc_id                  = aws_vpc.minha-vpc.id
  
  # Definindo a faixa de IP para a subnet privada
  cidr_block              = "10.0.2.0/24" 

  # Especificando a zona de disponibilidade desejada
  availability_zone       = "us-east-1b"   

  # Adicionando tags para identificação
  tags = {
    Name = "SubnetPrivada"
  }
}
