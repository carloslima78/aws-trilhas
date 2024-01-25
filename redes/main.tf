
# Definindo o provedor AWS
provider "aws" {
  
  # Substitua pela região desejada
  region = "us-east-1" 
}

# Criando uma VPC
resource "aws_vpc" "minha-vpc" {
  
  # Substitua pela sua faixa de IP desejada
  cidr_block = "10.0.0.0/16" 

  tags = {
    Name = "MinhaVPC"
  }
}