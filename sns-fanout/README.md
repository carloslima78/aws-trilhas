# Padrão Fanout: Distribuição e Filtro de Mensagens com SNS, SQS e Infra Terraform na AWS

O padrão **Fanout** é uma estratégia eficaz quando se trata de distribuir mensagens para vários consumidores sem a necessidade de modificar a lógica de produção de mensagens. 

Nesse contexto, a **Amazon Simple Notification Service (SNS)** se destaca como uma ferramenta robusta para a implementação desse padrão, especialmente quando combinada com as Filas de Mensagens do **Amazon Simple Queue Service (SQS)**.

Com o **Terraform**, tem o relevate papel de automatizar o provisionamento de toda a infraestrutura necessária para implementar o padrão Fanout, incluindo tópicos do SNS, filas do SQS e filtros de mensagens.

Isso facilita o gerenciamento da infraestrutura e garante que ela esteja sempre atualizada e consistente.


![Diagrama](diagramas/fanout.png)

## Distribuição Eficiente de Mensagens

O padrão Fanout é frequentemente utilizado em arquiteturas de microsserviços e sistemas distribuídos para alcançar a escalabilidade e a flexibilidade na distribuição de mensagens. 

Permite que uma mensagem seja replicada para vários destinos, atendendo a diferentes requisitos de consumo sem afetar a fonte original da mensagem.

## Amazon SNS: Facilitando a Distribuição de Mensagens

O Amazon SNS é um serviço de mensagens totalmente gerenciado de notificações que simplifica a construção e a escalabilidade de sistemas distribuídos. 

No contexto do padrão Fanout, o SNS atua como o ponto de entrada central para as mensagens, permitindo a criação de tópicos, nos quais os assinantes se inscrevem para receber mensagens relevantes.

## Filtro de Mensagens do SNS: Direcionando Mensagens com Precisão

Uma característica poderosa do SNS é o filtro de mensagens, que oferece a capacidade de direcionar mensagens específicas para assinantes interessados por mensagens específicas. 

Esse recurso é aderente ao implementar o padrão Fanout, embora seja opcional, permite que mensagens sejam enviadas apenas para os consumidores específicos, evitando uma sobrecarga desnecessária. 

As mensagens são filtradas com base em atributos pré definidos, proporcionando uma granularidade refinada na distribuição.

## Publishers/Subscribers: Características Cruciais

Os publicadores são responsáveis por enviar mensagens para o um tópico SNS, têm a flexibilidade de incluir atributos que são usados no processo de filtragem. 

Esses atributos ajudam a direcionar as mensagens aos assinantes corretos, garantindo que apenas as partes interessadas recebam informações relevantes.

Os assinantes, por sua vez, se conectam aos tópicos relevantes e recebem as mensagens que atendem aos critérios de filtragem estabelecidos. Isso permite uma distribuição personalizada, adaptada às necessidades específicas de cada consumidor.

## Amazon SQS: Filas de Mensagens Escalonáveis

O Amazon SQS, por sua vez, é um serviço de fila totalmente gerenciado que oferece uma maneira confiável e escalável de armazenar mensagens enquanto aguardam processamento. 

Ao conectar o SNS a filas SQS, é possível garantir que as mensagens sejam eficientemente encaminhadas para os consumidores finais, mantendo a ordem e a consistência.

## SNS vs SQS


### SNS - Serviço de Notificação Proativo 

O Amazon SNS é um serviço de mensageria ativo, projetado para notificar e distribuir mensagens para um ou mais consumidores, como endpoints de aplicativos, filas SQS, e-mails, SMS, Push, etc. 

Age como um "empurrador" ativo, enviando mensagens diretamente aos consumidores interessados, eliminando a necessidade de eles buscarem proativamente as informações.

### SQS - Serviço de Filas Reativo

O Amazon SQS, por outro lado, é um serviço de fila de mensagens que opera no modelo "puxe", armazenando as mensagens em filas e aguardando que os consumidores as solicitem. 

Fornece uma camada de desacoplamento entre produtores e consumidores, garantindo que as mensagens sejam processadas na ordem correta e evitando perda de dados.

### Combinação Eficiente para Garantir a Entrega: SNS + SQS

Ao combinar o SNS com o SQS, estabelecemos uma estratégia poderosa para garantir a entrega confiável de mensagens. 

O SNS serve como o iniciador ativo, transmitindo mensagens diretamente aos SQS, enquanto o SQS atua como um buffer resiliente, armazenando as mensagens até que os consumidores estejam prontos para processá-las. Essa abordagem oferece flexibilidade, escalabilidade e robustez na entrega de mensagens em ambientes distribuídos.

## Implementação do Padrão Fanout: SNS e SQS em Harmonia

Ao implementar o padrão Fanout com o SNS e SQS, é possível configurar tópicos no SNS para categorias específicas de mensagens. 

Utilizando filtros, as mensagens são direcionadas com precisão para aos assinantes apropriados, evitando distribuições desnecessárias. 

As filas SQS, por sua vez, agem como assinantes desses tópicos, recebendo e processando as mensagens de acordo com as necessidades específicas de cada consumidor.


## Terraform (IaaC)

O Terraform incorpora o conceito de Infraestrutura como Código (IaaC). Sua função é definir e provisionar recursos em núvem (Neste caso na AWS), como tópicos SNS, filas SQS e permissões, utilizando código declarativo. 

Ao adotar a abordagem IaaC, a infraestrutura torna-se facilmente gerenciável e escalável, permitindo uma implementação consistente e eficiente da arquitetura de mensageria na AWS. 

Essa prática não apenas agiliza o ciclo de vida dos recursos, mas também proporciona flexibilidade e facilita futuras atualizações na infraestrutura de forma padronizada.

## Caso de Uso: Arquitetura de Mensageria Financeira na Nuvem - PIX, Boleto e Contábil

Imaginemos um ambiente financeiro na nuvem, onde as mensagens de pagamento desempenham um papel vital. Vamos explorar um cenário onde um tópico SNS representa eventos de pagamentos efetuados e três filas SQS consumidoras desempenham funções distintas.

![Diagrama](diagramas/caso-de-uso.png)

### Notificação de Pagamento Efetuado - Tópico SNS:

No centro desse ambiente está o Tópico SNS denominado "Pagamento Efetuado". Este tópico funciona como o canal central que anuncia a ocorrência de pagamentos, sendo o ponto focal para distribuição de mensagens.

### Três Destinos Estratégicos - Filas SQS:

1. Fila PIX - Filtrando Transações Instantâneas:

- A Fila PIX é configurada para receber exclusivamente mensagens relacionadas aos pagamentos via o meio de pagamento PIX. Utiliza-se um filtro para direcionar apenas mensagens PIX para essa fila, otimizando o processamento específico dessas transações instantâneas.

2. Fila Boleto - Foco em Pagamentos Tradicionais:

- A Fila Boleto é designada para mensagens vinculadas a pagamentos realizados por boletos bancários. Semelhante à Fila PIX, ela emprega um filtro para concentrar-se exclusivamente em mensagens associadas a pagamentos via boleto.

3. Fila Contábil - Recebendo Todas as Mensagens:

- Contrariamente às filas anteriores, a Fila Contábil não utiliza filtros. Ela serve como um destino inclusivo, recebendo todas as mensagens de pagamentos efetuados, independentemente do método (PIX, boleto, entre outros). Este destino é estratégico para processos contábeis gerais.

### Eficiência e Especificidade:

Cada fila SQS estabelece uma assinatura com o tópico SNS, delineando suas preferências de filtro conforme o meio de pagamento ou ausência dela. Essas assinaturas são cruciais para direcionar eficientemente as mensagens para os destinos desejados.

Nesse contexto, a arquitetura proposta permite uma distribuição eficiente de mensagens financeiras, atendendo às necessidades específicas de cada componente. PIX, boletos e processos contábeis coexistem harmoniosamente, proporcionando uma abordagem estruturada e eficaz na manipulação de dados financeiros na nuvem.

## Definindo a infraestrutura IaaC

O código Terraform apresentado logo abaixo, representa a implementação do padrão Fanout com filtro de mensagens, utilizando o Amazon Simple Notification Service (SNS) como Publisher e o Simple Queue Service (SQS) como Subscribler. 

Partindo do princípio de que todo o código apresentado está sendo escrito em um arquivo **main.tf**:

### Definindo o Provedor AWS

O trecho inicial abaixo estabelece a região do provedor a ser utilizado, responsável por coordenar a criação e gerenciamento dos recursos na nuvem.

```hcl
# Definindo o provedor AWS
provider "aws" {
  region = "us-east-1" # Substitua pela sua região desejada
}
```

### Criando Tópico SNS e Filas SQS para Meios de Pagamento

O código abaixo define um tópico SNS denominado "pagamento-efetuado" e três filas SQS associadas a diferentes meios de pagamento: pix, boleto e contábil. 

Aqui, vale destacar que a fila "pagamento-contabil" não possui filtro, o que significa que receberá todas as mensagens, independentemente do tipo de pagamento.

```hcl
# Criando um tópico SNS
resource "aws_sns_topic" "pagamento_efetuado" {
  name = "pagamento-efetuado"
}

# Criando a fila SQS para pagamento pix
resource "aws_sqs_queue" "pagamento_pix" {
  name = "pagamento-pix"
}

# Criando a fila SQS para pagamento boleto
resource "aws_sqs_queue" "pagamento_boleto" {
  name = "pagamento-boleto"
}

# Criando a fila SQS para pagamento contábil
resource "aws_sqs_queue" "pagamento_contabil" {
  name = "pagamento-contabil"
}
```

### Adicionando Permissões para o Tópico SNS escrever nas Filas SQS

A permissão para que o tópico SNS escreva nas filas SQS é estabelecida utilizando os recursos aws_sqs_queue_policy. 

```hcl
# Adicionando permissões para o tópico SNS escrever na fila para o meio de pagamento pix
resource "aws_sqs_queue_policy" "permissao_pagamento_pix" {
  queue_url = aws_sqs_queue.pagamento_pix.id
  policy    = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Action": [
        "sqs:SendMessage"
      ],
      "Resource": [
        "${aws_sqs_queue.pagamento_pix.arn}"
      ],
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_sns_topic.pagamento_efetuado.arn}"
        }
      }
    }
  ]
}
EOF
}

# Adicionando permissões para o tópico SNS escrever na fila para o meio de pagamento boleto
resource "aws_sqs_queue_policy" "permissao_pagamento_boleto" {
  queue_url = aws_sqs_queue.pagamento_boleto.id
  policy    = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Action": [
        "sqs:SendMessage"
      ],
      "Resource": [
        "${aws_sqs_queue.pagamento_boleto.arn}"
      ],
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_sns_topic.pagamento_efetuado.arn}"
        }
      }
    }
  ]
}
EOF
}

# Adicionando permissões para o tópico SNS escrever na fila para o fluxo contábil
resource "aws_sqs_queue_policy" "permissao_pagamento_contabil" {
  queue_url = aws_sqs_queue.pagamento_contabil.id
  policy    = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Action": [
        "sqs:SendMessage"
      ],
      "Resource": [
        "${aws_sqs_queue.pagamento_contabil.arn}"
      ],
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_sns_topic.pagamento_efetuado.arn}"
        }
      }
    }
  ]
}
EOF
}
```

## Criando Assinaturas entre o Tópico SNS e Filas SQS com Filtros

A criação de assinaturas entre o tópico SNS e as filas SQS é realizada através dos recursos aws_sns_topic_subscription. 

Além disso, os filtros são aplicados nessa etapa para direcionar mensagens específicas para cada fila.

```hcl
# Criando a assinatura da fila "pagamento-pix" no tópico "pagamento-efetuado" com filtro
resource "aws_sns_topic_subscription" "assinatura_pix" {
  topic_arn = aws_sns_topic.pagamento_efetuado.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.pagamento_pix.arn

# Adicionando o filtro com o atributo tipo e valor pix
  filter_policy = <<EOF
{
  "tipo": ["pix"]
}
EOF
}

# Criando a assinatura da fila "pagamento-boleto" no tópico "pagamento-efetuado" com filtro
resource "aws_sns_topic_subscription" "assinatura_boleto" {
  topic_arn = aws_sns_topic.pagamento_efetuado.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.pagamento_boleto.arn

# Adicionando o filtro com o atributo tipo e valor boleto
  filter_policy = <<EOF
{
  "tipo": ["boleto"]
}
EOF
}

# Criando a assinatura da fila "pagamento-contabil" no tópico "pagamento-efetuado" sem filtro
resource "aws_sns_topic_subscription" "assinatura_contabil" {
  topic_arn = aws_sns_topic.pagamento_efetuado.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.pagamento_contabil.arn
}
```

### Outputs para Informações Adicionais

Por fim, são definidos outputs para imprimir informações sobre os principais recursos provisionados na AWS após a execução do Terraform, como o nome do tópico e o nome das filas.

```hcl
# Output para imprimir o nome do tópico
output "topic_name" {
  value = aws_sns_topic.pagamento_efetuado.name
}

# Output para imprimir o nome da fila pagamento pix
output "queue_name_pix" {
  value = aws_sqs_queue.pagamento_pix.name
}

# Output para imprimir o nome da fila pagamento boleto
output "queue_name_boleto" {
  value = aws_sqs_queue.pagamento_boleto.name
}

# Output para imprimir o nome da fila pagamento contabil
output "queue_name_contabil" {
  value = aws_sqs_queue.pagamento_contabil.name
}
```

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

Após a execução com sucesso dos comandos acima, espera-se que os recursos definidos nessa trilha tenham sido provisionados conforme imagens abaixo:

- Tópico SNS - Representa o evento para Pagamento Efetuado


![Diagrama](diagramas/sns-pagamento-efetuado.png)


- Filas SQS - Representam os assinantes do tópico **pagamento-efetuado** que receberão as mensagens correspondentes aos meios de pagamento pix e boleto, além do fluxo contábil que receberá todas as mensagens.


![Diagrama](diagramas/sqs-filas.png)


- Assinatauras das filas SQS com o tópico SNS **pagamento-efetuado**.


![Diagrama](diagramas/assinaturas.png)


- Filtro incluído na assinatura da fila SQS **pagamento-pix** para recepção das mensagens específicas de pagamentos realizados com este meio de pagamento


![Diagrama](diagramas/filtro-pix.png)


- Filtro incluído na assinatura da fila SQS **pagamento-boleto** para recepção das mensagens específicas de pagamentos realizados com este meio de pagamento


![Diagrama](diagramas/filtro-boleto.png)



## Testando a arquitetura criada na AWS

Após o provisionamento dos recursos com sucesso na AWS, vamos testar a arquietura.


- Produzindo uma mensagem de pagamento efetuado via pix utilizando o filtro com o atributo "tipo" e valor "pix".


![Diagrama](diagramas/sns-evento-pagamento-efetuado-pix.png)


- Produzindo uma mensagem de pagamento efetuado via boleto utilizando o filtro com o atributo "tipo" e valor "boleto".


![Diagrama](diagramas/sns-evento-pagamento-efetuado-boleto.png)


- Consumindo a mensagem de pagamento efetuado via pix a fila SQS pagamento-via-pix. Note que existe apenas a mensagem específica a este meio de pagamento de acordo com o filtro.


![Diagrama](diagramas/sqs-pagamento-efetuado-pix.png)

![Diagrama](diagramas/sqs-pagamento-efetuado-pix.mensagem.png)


- Consumindo a mensagem de pagamento efetuado via boleto a fila SQS pagamento-via-boleto. Note que existe apenas a mensagem específica a este meio de pagamento de acordo com o filtro.


![Diagrama](diagramas/sqs-pagamento-efetuado-boleto.png)


![Diagrama](diagramas/sqs-pagamento-efetuado-boleto.mensagem.png)


- Consumindo todas as mensagens na fila SQS pagamento-contabil. Note que existem as duas mensagens tanto pix quanto boleto, pois neste caso não houve filtro.


![Diagrama](diagramas/sqs-pagamento-efetuado-todos.png)


O comando abaixo, removerá todos os recursos criados na AWS.

```hcl
# Destrói todos os recursos criados
terraform destroy -auto-approve 
```

## Conclusão

O padrão Fanout, quando implementado com Amazon SNS e SQS, oferece uma solução escalável e eficiente para a distribuição de mensagens em sistemas distribuídos. 

O uso do filtro de mensagens do SNS garante que as mensagens relevantes sejam entregues a cada consumidor específico, minimizando a sobrecarga e maximizando a eficiência operacional. 

Essa abordagem não apenas simplifica a arquitetura, mas também contribui para um melhor desempenho e gerenciamento de recursos em ambientes complexos e dinâmicos.

O código Terraform apresentado, proporciona uma base para a criação e configuração automatizada de recursos SNS e SQS na AWS, facilitando a implementação de padrões como Fanout para distribuição eficiente de mensagens em sistemas distribuídos.




