#!/bin/bash
# Comandos para instalar um servidor httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Bem vindo a Instância EC2 $(hostname -f)</h1>" > /var/www/html/index.html