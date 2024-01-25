# Conceitos de Redes na AWS

Na AWS, redes referem-se à infraestrutura de comunicação que permite a conectividade e o isolamentoentre os diversos serviços e recursos hospedados na nuvem.

A AWS oferece uma variedade de serviços e ferramentas para configurar redes, como o Amazon VPC (Virtual Private Cloud), que permite criar redes isoladas e personalizadas na nuvem.

Através de recursos como subnets e security groups (grupos de segurança), é possível projetar arquiteturas de rede flexíveis e escaláveis para atender às necessidades específicas das aplicações.

Além disso, a presença global da AWS é suportada por regiões, como US East, e cada região é composta por múltiplas Zonas de Disponibilidade (AZs), proporcionando redundância e resiliência. 

Ao utilizar as regiões e AZs estrategicamente, os usuários podem projetar arquiteturas de rede robustas que garantem desempenho e alta disponibilidade para suas aplicações na nuvem.

A rede na AWS desempenha um papel crucial na garantia de desempenho, segurança e alta disponibilidade para as aplicações e dados hospedados na plataforma.


## Regions (Regiões)

Na AWS, uma region refere-se a uma localização geográfica específica que abriga data centers. Cada região é composta por múltiplas Zonas de Disponibilidade, oferecendo redundância e permitindo a distribuição global de recursos em uma plataforma de nuvem.


## Availability Zones (Zonas de Disponiblidade)

Tratam-se data centers fisicamente separados, mas interconectados, dentro de uma região, sendo que cada possui energia, rede e conectividade redundantes. 

Estratégicamente localizadas a uma distância significativa, até 100 km, essas zonas são separadas estrategicamente para garantir backups seguros e oferecer resiliência contra desastres, aproveitando a separação física para assegurar redundância e aumentar a confiabilidade da infraestrutura na nuvem.


## VPC - Virtual Privte Cloud

- Uma VPC está sempre vinculada a uma region.
- Uma region suporta até 5 VPCs.


## Subnet

Toda subnet é vinculada a uma VPC


### Subnet Pública


### Subnet Privada

Não possui acesso externo
Cluster ECS, bancos de dados


## Seurity Group


## Analogia (Cidade)


## Criando os recursos na AWS

Após concluir o código acima, executar os comandos Terraform abaixo para iniciar, planejar e aplicar os recursos declarados:

**Observação:** Execute os comandos via terminal dentro da pasta onde o arquivo Terraform *main.tf* se encontra.

![Diagrama](diagramas/comando-terraform-terminal.png)

```hcl
# Inicia o Terraform e instala os componentes de acordo com os recursos declarados que serão criados
terraform init 
```

```hcl
# Apresenta o plano dos recursos que serão criados de acordo com a receita Terraform
terraform plan
```

```hcl
# Aplica a criação dos recursos conforme o planejamento acima, porém, sem solicitar confirmação
terraform apply -auto-approve
```

Após a execução com sucesso dos comandos acima, espera-se que os recursos definidos nessa trilha tenham sido provisionados
