
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
    Name = "minha-vpc"
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
    Name = "minha-subnet-publica"
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
    Name = "minha-subnet-privada"
  }
}

# Criando um Security Group para a EC2 pública, vista que estará na subnet pública
resource "aws_security_group" "minha-ec2-public-sg" {
  name        = "minha-ec2-public-sg"
  description = "Security Group para as EC2s"
  
  # Vinculando à VPC criada anteriormente
  vpc_id                  = aws_vpc.minha-vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Criando um Security Group para a EC2 privada, vista que estará na subnet privada
resource "aws_security_group" "minha-ec2-private-sg" {
  name        = "minha-ec2-private-sg"
  description = "Security Group para as EC2s"
  
  # Vinculando à VPC criada anteriormente
  vpc_id                  = aws_vpc.minha-vpc.id
  
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Criando uma instância EC2 pública
resource "aws_instance" "minha-ec2-publica" {
  # Ubuntu 20.04 LTS 
  ami           = "ami-0c7217cdde317cfec"  

  # Tipo de instância da camada gratuita
  instance_type = "t2.micro"  

  associate_public_ip_address = true

  # Vinculando à subnet pública
  subnet_id     = aws_subnet.minha-subnet-publica.id

  # Configurando o Security Group para permitir tráfego de entrada de qualquer lugar
  vpc_security_group_ids = ["${aws_security_group.minha-ec2-public-sg.id}"]

  # Atribuindo um par de chaves existente
  key_name      = "nome do par de chaves"

  tags = {
    Name = "minha-ec2-publica"
  }
}

# Criando uma instância EC2 privada
resource "aws_instance" "minha-ec2-privada" {
  # Ubuntu 20.04 LTS 
  ami           = "ami-0c7217cdde317cfec"  
  
  # Tipo de instância da camada gratuita
  instance_type = "t2.micro"   

  associate_public_ip_address = true             
  
  # Vinculando à subnet privada
  subnet_id     = aws_subnet.minha-subnet-privada.id

  # Configurando o Security Group para permitir tráfego de entrada de qualquer lugar
  vpc_security_group_ids = ["${aws_security_group.minha-ec2-private-sg.id}"]

  # Atribuindo um par de chaves existente
  key_name      = "nome do par de chaves"

  tags = {
    Name = "minha-ec2-privada"
  }
}
