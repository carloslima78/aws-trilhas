# AWS - Solutions Architect Associate

Esta trilha tem o propósito de fornecer pílulas de conhecimento para direcionamento para gatilhos de estudos mais aprofundados referente a certificação **Solutions Architect Associate**.

A certificação **Solutions Architect Associate** está posicionada entre a certificação **AWS Practitioner** e a **Solutions Architect Professional**.

## Conceitos de Cloud Computing

### Histórico

Antigamente as empresas contratavam salas com servidores físicos conectados via rede com switches, roteadores e firewalls. Cada servidor tinha um objetivo específico como AD, FTP, aplicação, banco de dados etc.

#### Pontos negativos dessa estrutura:

- Alto custo.
- Tempo de preapração.
- Atualizações de softwares.
- Extração de backups.

### AWS

Embora a AWS não tenha criado o conceito de Cloud, podemos dizer que foi responsável por dar um grande impulso. 

A Amazon pussuia uma excelente estrutura computacional para atender as suas próprias operações, com uma quantidade de recursos e processamento extremamente grande, mas que porém, não utilizava essa gama totalmente. 

Foi então que a Amazon criou uma outra empresa chamada Amazon Web Services (AWS) para fornecer comercialmente os recursos computacionais que não utilizava.

Atualmente a AWS assim como outros provedores de serviços em Cloud (Microsoft Azure, Google Cloud, etc), permitem que o cliente contrate e utilize recursos computacionais e pague por **segundo** de uso.

#### Benefícios da Cloud Computing

- Velocidade de implementação e disponibilidade de soluções em segundos.
- Atualizações de softwares automáticas e sem interrupção de serviços.
- Otimização de custo ao poder prever e provisionar a utilização de recursos (3 anos = 75% de desconto).
- Segurança de dados (Sistema de backup integrado).
- Escalabilidade **automática** ou **manual em segundos e com poucos cliques** de recursos conforme demanda.

### Tipos de Cloud

#### IaaS - Infrastructure as a Service (Hospedagem)

- Oferta de recursos de infraestrutura em ambiente Cloud.
- Paga-se pela utilização da **infraestrutura** de um provedor como serviço.
- Máquinas virtuais, rede, armazenamento, etc.

#### PaaS - Platform as a Service (Construção)

- Oferta de ambientes em Cloud para desenvolvimento e fornecimento de aplicações.
- Paga-se pela utilização da **plataforma** de um provedor como serviço.
- Banco de dados, CI/CD, orquestração de containers, etc.

#### SaaS - Software as a Service (Consumo)

- Oferta de software e aplicações que podem ser consumidos pela internet.
- Paga-se pela utilização do **software** de um provedor como serviço.
- Marketplaces, ERP, CRM, editores, etc.

<br>

| On Site | IaaS | PaaS | SaaS | 
| ---- | ----- | ---- | ----- |
| Applications | Applications | Applications | **Applications** |
| Data | Data | Data | **Data** |
| Runtime | Runtime | **Runtime** | **Runtime** |
| Middleware | Middleware | **Middleware** | **Middleware** |
| O/S | O/S | **O/S** | **O/S** |
| Virtualization | **Virtualization** | **Virtualization** | **Virtualization** |
| Servers | **Servers** | **Servers** | **Servers** |
| Storage | **Storage** | **Storage** | **Storage** |
| Networking | **Networking** | **Networking** | **Networking** |


### Tipos de Rede

#### Public Cloud

- Trata-se de um ambiente Cloud compartilhado e disponível ao público.
- A infraestrutura de uma Cloud pública é gerenciada pelo provedor do serviço.
- **Importante**: Public Cloud não significa que os recursos utilizados em ambiente Cloud são públicos, significa que os provedores ofertam os recursos Cloud ao público.

#### Private Cloud

- Trata-se de um ambiente Cloud dedicado exclusivamente a uma determinada organização (Cliente).
- A infraestrutura de uma Cloud privada pode ser gerenciada pela própria organização.
- A Cloud privada oferece maior controle, privacidade e segurança em relação as outras opções.

#### Hybrid Cloud

- Trata-se da combinação entre Public Cloud e Private Cloud.
- Permite que uma organização mantenha algumas cargas de trabalho em sua nuvem privada e outras em nuvem pública.
- Útil para organizações que desejam aproveitar os benefícios de ambas as nuvens e, ao mesmo tempo, manter o controle sobre dados sensíveis.
- **Caso de Uso**: Uma organização deseja manter as páginas Web em cloud pública e o banco de dados em cloud privada.


## Shared Responsability Model (Modelo de Responsabilidade Compartilhada)

Determina quais são as responsabilidades da AWS e quais são do Cliente referente a uma infraestrutura de recursos.

Trata-se de um termo que o cliente aceita no momento da criação de uma conta, onde é demonstrado que AWS que não garante toda a segurança de um ambiente, pois existem etapas que dependem do cliente. 

**Documentação Oficial:** (https://aws.amazon.com/pt/compliance/shared-responsibility-model/)

### Responsabilidades da AWS

- Garantir a segurança **DA** Cloud e o que o cliente não tem acesso nem autonomia.
- Software (Computação, armazenamento, banco de dados, rede, etc.).
- Hardware (Regiões, zonas de disponibilidade, edge locations, etc.).

### Responsabilidades do Cliente

- Garantir a segurança **NA** Cloud e o que o cliente tem acesso e autonomia.
- Plataformas, aplicações, identidade, gerenciamento de acesso, etc.
- Configurações de sistemas operacionais, redes, firewall, etc.

### Controles Compartilhados

- Geranciamento de patches, configurações, conscientização, treinamentos, etc.

## Billing

### Alerta de Billing

Trata-se de alertas para monitoramento e notificação (por e-mail) de consumo de recursos que podem ser por:

- Custo (Valor monetário).
- Utilização.
- Planos de Economia.


## Infraestrutura Global

### AWS Regions (Regiões)

- São locais físicos distribuídos pelo mundo onde localizam-se os Datacenters da AWS.

### AWS Availability Zones (Zonas de Disponiblidade)

- São Datacenters dentro de uma região AWS com links de conexão entre elas com alta velocidade para manter baixa latência.
- Um o mais Datacenters distintos com energia, rede e conectividade redundantes em uma região.
- São separadas fisicamente por uma distância significativa (até 100 KMs).
- A separação ocorre para que mantenham **backpus** seguros umas das outras e a segurança contra desastres.

### AWS Edge Locations (Pontos de Presença)

- São locais de armazenamento em cache de baixa latência da Amazon Web Services (AWS) que ajudam a acelerar a entrega de conteúdo para os usuários finais. 
- Cada Edge Location é uma infraestrutura física que faz parte da rede de entrega de conteúdo da AWS, o CloudFront.

### AWS Local Zones (Zonas Local)

- São Datacenters menores que ficam entre as zonas de disponibilidade.
- Possuem conexão direta com as zonas de disponibilidade.
- Seu propósito é a redução de latência entre as zonas de disponbilidade para serviços de stream por exemplo.

### AWS Wavelength

- É uma infraestrutura que a AWS implanta nas provedoras de telecomunicação (Vivo, Claro, etd.), para que se conectem aos serviços da AWS com alta velocidade.
- Otimiza a comunicação entre os serviços disponíveis em celulares e os serviços AWS.
- Melhora jogos, stream, etc.
- Não há encargos pelo uso.

### AWS Outspots

- A AWS leva e implanta serviços e infraestrutura em qualquer Datacenter local.
- O cliente pode aproveitar os serviços AWS em seu próprio Datacenter.
- O cliente será responsável pela segurança, pois a infraestrutura está em seu Datacenter.
- Voltado para clientes de grande porte que já possuem seus próprios Datacenters, ou aqueles que não contam com regiões AWS disponíveis.

## IAM (Identity and Accesss Management)

- Serviço **global** da AWS para gerenciamento de identidade e acesso.
- É composto por **Users (Usuários)**, **Groups (Grupos)**, **Policies (Políticas)** e **Roles (Functions)**.

### Users (Usuários)

- Trata-se de uma identidade da AWS que pode-se criar para conceder acesso a serviços e recursos da AWS. 
- Os usuários são autenticados com suas credenciais exclusivas e podem ter permissões e políticas de acesso definidas para controlar o que eles podem e não podem fazer na conta da AWS.

### Groups (Grupos)

- Trata-se de um grupo de usuários da AWS que podem ser gerenciados coletivamente, definindo permissões e políticas de acesso.
- Um usuário pode pertencer a um ou mais grupos.
- **Observação**: Grupos contém apenas usuários e não outros grupos.

### Policies (Políticas)

- Tratam-se de documentos JSON ou YAML que definem as permissões de acesso para usuários, grupos e roles na AWS. 
- Podem ser anexadas diretamente a um usuário ou grupo ou associadas a um IAM role.
- As políticas definem um conjunto de permissões para os usuários, como lançar e configurar serviços por exemplo.
- O **Princípio do Menor Privilégio** é uma boa prática na AWS, onde um usuário terá somente as permissões que precisa. 
- É possível criar as próprias políticas especificando determinadas permissões.

#### Estrutura JSON

```hcl

 {
   "Version": "2012-10-17", // Versão da política de acesso
   "Statement": [ // Declaração de permissões
      {
         "Effect": "Allow", // Efeito das permissões (Permitir ou Negar)
         "Action": [ // Ação permitida na permissão
            "s3:ListBucket", // Listar o conteúdo do bucket
            "s3:GetBucketLocation" // Obter a localização do bucket
         ],
         "Resource": "arn:aws:s3:::NOME_DO_BUCKET" // ARN (Amazon Resource Name) do bucket
      },
      {
         "Effect": "Allow", // Efeito das permissões (Permitir ou Negar)
         "Action": [ // Ação permitida na permissão
            "s3:PutObject", // Enviar (upload) objetos para o bucket
            "s3:GetObject", // Obter (download) objetos do bucket
            "s3:DeleteObject" // Remover objetos do bucket
         ],
         "Resource": "arn:aws:s3:::NOME_DO_BUCKET/*" // ARN (Amazon Resource Name) do bucket para permitir acesso a todos os objetos.
      }
   ]
}

```

### MFA (Multi-Factor Authentication ou Autenticação de Múltiplos Fatores)

Trata-se de um mecanismo de segurança que exige que o usuário forneça mais de uma forma de autenticação para ter acesso a uma conta ou sistema.

Ao usar o MFA, mesmo que um atacante possua a senha de um usuário, ele ainda precisaria de um segundo fator de autenticação para acessar a conta AWS. 

### Roles (Funções)

Tratam-se de permissões atribuídas a recursos e serviços da AWS para que executem determinadas ações em outros serviços da AWS.

#### Funções Comuns

- EC2 Instance Roles
- Lambda Function Roles
- Cloud Formation Roles
- etc...


### Formas de Acesso a Conta AWS

- **AWS Management Console**: Protegido por Senha + MFA.
- **AWS Comand Line Interface (CLI)**: Protegido por chaves de acesso (Access Key).
- **AWS Software Developer Kit (SKD)**: Acesso por código de programação protegido por chaves de acesso (Access Key). Composto por **Access Key ID (Usuário)** e **Secret Access Key (Senha)** que não devem ser compartilhados com outras pessoas.

### IAM Access Advisor (Consultor de Acesso)

Na área de usuários, é possível utilizar o **Access Advisor** para auditar as permissões que foram utilizadas.

### IAM Credentials Report

Lista todos os usuários IAM de uma conta da AWS e o status de suas várias credenciais.

### CLI

- Ferramenta que permite a interação com a AWS por meio de linhas de comando.
- Permite acesso direto as APIs públicas da AWS.
- É um Open Source disponível em (https://github.com/aws/aws-cli).

#### Instalação no Linux

- Comandos para instalação:

```hcl
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

- Comando para verificar se a instalação foi bem sucedida:

```hcl
aws --version
```

Fonte Oficial: (https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

- Comandos para acessar uma conta AWS via CLI após criar a **Access Key** associada ao usuário:
- **Observação**: Os dados de acesso que devem ser fornecidos abaixo, são as credenciais presentes na **Access Key**, que é um requisito **obrigatório** para essa ação. Portanto, não deixe de criar a sua **Access Key**!

```hcl
aws configure
AWS Access Key ID [None]: [sua_access_key_id]
AWS Secret Access Key [None]: [sua_secret_access_key]
Default region name [None]: [sua_região_preferida]
```

- Comando para verificar se a autenticação foi bem sucessida:

```hcl
aws sts get-caller-identity
```

- O comando acima deve apresentar os dados da conta e usuário no formato JSON conforme abaixo:

```hcl
{
    "UserId": "ID_DO_USUARIO",
    "Account": "ID_DA_CONTA_AWS",
    "Arn": "arn:aws:iam::ID_DA_CONTA_AWS:user/NOME_DO_USUARIO"
}
```

- Comando para listar os usuários IAM existentes em uma conta AWS.
- **Observação**: Este comando funcionará para usuários que possuam as devidas permissões (Policies)!

```hcl
aws iam list-users
```

## EC2

- São máquinas virtuais mantidas pela AWS (Virtualização).
- São instâncias **Linux**, **Windows** ou **Mac OS** dentro da plataforma EC2 que substituem servidores físicos (IBM, Dell, etc.).
- É um serviço **regional**, portanto, é possível criar instâncias EC2 em diversas regiões AWS.
- É cobrado por **segundo** de uso.

- Consiste nas capacidades:
  - Lançar máquinas virtuais (**EC2**).
  - Armazenar dados em drivers virtuais (**EBS**).
  - Distribuir carga entre máquinas (**ELB**).
  - Escalar serviços usando grupo de auto scaling (**ASG**).

### Acesso a Instâncias EC2

- IAM User
  - Acesso por CLI utilizando as chaves de acesso (Access Key e Secret Key) associadas a um usuário.
  - **Não recomendado**, pois a instância EC2 terá acesso as credenciais gerando vulnerabilidades de segurança.

- IAM Role
  - Acesso por funções contendo as políticas necessárias para que a instância EC2 acesse os demais recursos AWS desejados.
  - **Recomendado**, pois a instância estará associada a funções e não terá acesso as credenciais.

### Tipos de Instâncias EC2

- Uso geral.
- Otimizada para computação.
- Otimizada para memória.
- Computação acelerada.
- Otimizadas para armazenamento.
- Otimizadas para HPC.
- Recursos das instâncias.
- Medir performance das instâncias.
  
- Fonte Oficial: (https://aws.amazon.com/pt/ec2/instance-types/).

- Demonstra e compara os tipos de instâncias: (https://instances.vantage.sh/)

### Convenção de Nomes de Instâncias EC2

Para a instância do tipo **t2.micro**:

- **t**: Família de instâncias, o prefixo **t** identifica a classe ou tipo de instância.
- **2**: Indica a geração da família de instâncias. 
- **micro**: Tamanho dentro da classe da instância, indica a quantidade de recursos de computação (vCPU), memória RAM e armazenamento disponíveis.

### Security Groups

- É o firewall para as instâncias EC2.
- É um serviço de escopo **regional**.
- Controlam a entrada (Inbound) e saída (Outbound) de dados, portas e range de IPs.
- Por padrão, a entrada é bloqueada e a saída é liberada.
- É possível criar uma composição de security groups, onde um autoriza o outro.
- Pode estar associado a várias instâncias EC2 e uma instância pode ter vários security groups associados.
- Portas comuns:
  - **Porta 22 SSH**
  - **Porta 21 FTP**
  - **Porta 80 HTTP**
  - **Porta 443 HTTPS**
  - **Porta 3389 RDP**

### Tipos de Planos

- **On-Demand Instances**
  - Permite que se provisione uma instância a qualquer momento e imediatamente.
  - Por ser uma categoria não planjeda junto a AWS, será cobrada a mais.
  - Cobrado por segundo (Linux e Windows) e por hora (outros).

- **Reserved Instances**
  - Instâncias a partir de um contrato assinado com a AWS.
  - Paga-se menos pois os recursos necessários são planejados.
  - Custa 75% menos que as demais.
  - Compromisso de reserva de 1 a 3 anos.

- **Spot Instances**
  - São adquiridas por meio de leilões de capacidade ociosa da AWS.
  - Custa 90% a menos que as demais.
  - Recomendado uso de curtíssimo prazo, como testes por exemplo.
  - Não recomendado para produção, pois a AWS pode encerrar a instância sem aviso prévio se alguém pagar mais.

- **Dedicated Hosts**
  - Servidor físico dedicado,logo instâncias dedicadas.
  - É a opção mais cara.
  - Compromisso de reserva de 1 ou 3 anos.

- **Dedicated Instances**
  - São executadas em hardware dedicado exclusivamente para um único cliente.
  - Oferecem maior controle de segurança e conformidade.

    
### Placement Groups

Permite que as instâncias EC2 sejam agrupadas logicamente para melhorar o desempenho, a segurança e a disponibilidade.

Seguem os tipos de Placement Groups abaixo:

- **Cluster**
  - Usado para hospedar instâncias EC2 em um **rack** único dentro de uma única zona de disponibilidade.
  - Se um rack falhar, todas as instâncias EC2 falham.
  - As instâncias do EC2 ficam próximas umas das outras oferecendo computação e rede de alto desempenho.

- **Spread**
  - Usado para distribuir instâncias EC2 em diferentes racks, diferentes datacenters em uma única zona de disponibilidade.
  - Possui o limite de 7 instâncias por zona de disponibilidade.
  - Possui redundância e evita que todas as instâncias sejam afetadas por um único ponto de falha.

- **Partition**
  - Usado para distribuir as instâncias EC2 em partições lógicas, de forma que sejam colocadas em uma máquina distinta em uma zona de disponibilidade. 
  - Aumenta a disponibilidade e tolerância a falhas de aplicações

### Hibernate

## Storage

- Tratam-se de divesos serviços para armazenamento da AWS.
  - S3, Glacier, Snowball, EFS, FSx, CloudFront, EBS, Storage Gateway, Instance Store (EC2).

### Categorias de Storage:

- Block Storage

  - Arnazenamento em formato de blocos.
  - Conectado via HD ou USB.
  - Baixa Latência.
  - **DAS (Direct-Attached Storage)**: Armazenamento de dados conectado diretamente a um único servidor.
        
- File Storage

  - Voltado a dados que precisam ser compartilhados com um ou mais usuários.
  - Os arquivos são associados a uma pasta na nuvem.
  - **NAS (Network-Attached Storage)**: Armazenamento de dados conectado a uma rede.

- Object Storage

  - Armazenamento de objetos.
  - Possui uma identificação única e uma URL.
  - Podemos associar dados de metadata. 

### EBS (Elastic Block Store)

- São servidores físicos de armazenamento compostos por discos.
- Um volume EBS pode ser associado somente a uma instância EC2. 
- Uma instância EC2 pode ter vários volumes EBS associados.
- Um volume EBS deve estar na mesma AZ da instância EC2.
- Para utilizar um volume EBS em uma EC2 em outra AZ, cria-se um **Snapshot** para ser movido em um novo volume EBS na AZ desejada.
- Os discos não ficam dentro das máquinas físicas EC2, e sim em servidores físicos de armazenamento.
- As instâncias EC2 se conectam aos servicores EBS para que sejam seus discos de armazenamento.
- A unidade de medida é o IOPS (Input Output Per Second).
- Usando até 30 Gigas de armazenamento mantém no Free Tier.
- Existe a configuração para remover o volume EBS após encerrar uma instância EC2 (**Delete on Termination**).

#### Tipos de Volume:

- HDD:
  - Recomendado para armazenamento.
  - Menos velocidade.
  - Mais barato.
        
- SSD: 
  - Recomendado para sistemas operacionais, bancos de dados, etc.
  - Mais velocidade.
  - Mais caro.

(https://aws.amazon.com/pt/ebs/volume-types/)

### EBS Snapshot

- São cópias de volumes EBS para fins de backup e restauração.
- Podem ser criados em qualquer zona de disponibilidade.
- Um volume EBS não pode ser movido para outra AZ, neste caso cria-se um Snapshot para um novo volume EBS em outra AZ.

#### EBS Snapshot Features

- EBS Snapshot Archive
  - Mova um Snapshot para um arquivo e pague 75% mais barato.
  - Restaure o arquivo de 24 a 72 horas.
            
- Recicle Bin For EBS Snapshot (lixeira)
  - Configure uma lixeira para retenção de Snapshots removidos.
  - Protege contra deleções acidentais.
  - O tempo de retenção é configurável.
  - O Snapshot é recuperado imediatamente.

### EC2 Instance Store

- Trata-se de um volume conectado direto ao hardware da EC2, é um armazenamento local.
- Volumes EBS são bons, porém, possuem limitações em performance.
- Instance Store é uma boa opção se a prioridade for muita performance para dados de curta duração.
- Excelente para I/O, buffer, cache e conteúdo temporário.
- Se a instância EC2 for parada ou encerrada, os dados se perderão, pois diferentemente do EBS, trata-se de um disco físico conectado ao hardware do EC2.
- Para armazenamento de longa duração, EBS é uma opção melhor.

### AMI (Amazon Machine Image)

- São as imagens de sistemas operacionais que serão executados nas instâncias EC2.
- Representam a personalização de uma instância EC2.
- É possível utilizar AMIs disponibilizadas pela AWS ou construir as próprias AMIs conforme necessidade específica tal como softwares, configurações, sistemas operacionais, monitoramento, etc.  
- É possível lançar uma instância EC2 a partir de:
  - **AMI Publicas**: Disponibilizadas pela AWS.
  - **AMI Próprias**: Construídas e mantidas pelo usuário.
  - **AWS Marketplace**: Construídas e vendidas por usuários no Marketplace.

## Escalabilidade e Alta Disponibilidade

### Escalabilidade

Significa que uma aplicação pode lidar com cargas de trabalho altas e se adaptar.

#### Escala Vertical

Significa aumentar o **tamanho/capacidade computacional** de uma instância.

- **Analogia simbólica**:
  - Capacitar um atendente junior para que se torne um atendente sênior, logo será capaz de lidar com uma quantidade maior de atendimentos.

- **Analogia computacional**: 
  - Aumentar a capacidade de uma instância EC2 de t2.micro para t2.larger.

#### Escala Horizontal

Significa aumentar a **quantidade** de instâncias. A escala horizontal aplicas-e em sistemas distribuídos.

- **Analogia simbólica**:
  - Aumentar o número de atendentes conforme a quantidade de atendimentos solicitados. 

- **Analogia computacional**: 
  - Aumentar a quantidade de instâncias EC2 de acordo com a carga de trabalho demandada.

### Alta Disponibilidade

Significa que a aplicação precisa estar sempre disponível.

- Geralmente atua junto a escala horizontal.
- O objetivo da alta disponibilidade é sobreviver a uma perda de datacenter (**desastres**).

- **Analogia simbólica**:
  - Existir unidades da central de atendimento em locais distintos para que o atendimento não seja interrompido.

- **Analogia computacional**: 
    - Execução das instâncias EC2 em pelo pelo menos 2 zonas de disponibilidade para garantir a disponibilidade das aplicações hospedadas.

## ELB (Elastic Load Balancer)

- Responsável pela distribuição de carga para instâncias EC2.
- Fica a frente das instâncias sendo um ponto único de entrada.
- Distribui percentualmente o tráfego de requisições entre instâncias EC2.
- Capaz de gerenciar instâncias em AZs distintas fomentando alta disponibilidade.
- Recurso crucial para aplicações que estão expostas na Internet e não se conhece o tráfego estimado.

- Integra-se a diversos produtos da AWS:
  - EC2, Auto Scaling Group, ECS.
  - Certificate Manager (ACM), CloudWatch.
  - Route 53, WAF, Global Accelerator.

- O **Auto Scalling** complementa o trabalho do Elastic Load Balancer em momentos de falhas, onde é capaz de provisionar novas instâncias caso uma instância falhe.

- Para obter o endereço IP do cliente, o ALB adiciona um cabeçalho adicional chamado **X-Forwarded-For** que contém o endereço IP do cliente.

### Target Groups

Trata-se do grupo de recursos **alvo** que serão balanceados pelo ALB. 
São capazes de monitorar a saúde dos recursos alvo presentes no target group.

Um target group pode ser composto por:

- Instâncias EC2.
- Tarefas ECS (Tasks).
- Funções Lambda.
- Endereços IP.

**Importante**: Um ALB é capaz de gerenciar o balanceamento de um ou mais target groups.

### Stickness Sessions

É uma configuração do target group onde o ELB associa a sessão de um usuário a um destino específico, ou seja, será redirecionado para uma mesma instância enquanto a sua sessão estiver ativa. 

Uma vez que o stickness está habilitado, o ELB armazena um cookie no navegador do usuário para identificar a instância a qual ele foi direcionado. Esse cookie é enviado a cada requisição subsequente do usuário, permitindo que o ELB o direcione para a mesma instância.

Os cookies podem ser de dois tipos:

- **Application-based Cookies**
  - É baseado em cookies gerados pelo aplicativo.

- **Duration-based Cookies**
  - É baseado em cookies gerados pelo ELB.

### Tipos de ELB

- **Classic Load Balancer - (CLB - 2009)**
  - É uma junção de ALB e NLB aplicado para os protocolos **HTTP**, **HTTPS**, **TCP**, **SSL**.
  - Foi o primeiro Load Balancer criado pela AWS.
  - Focado na aplicação e na rede.
  - **IMPORTANTE**: Não recomendado pois o Classic Load Balancer está depreciado pela AWS.

- **Application Load Balancer (ALB - 2016)**
  - Aplicado para os protocolos **HTTP**, **HTTPS**, **WebSocket** atuando na camada 7 de Aplicação do modelo OSI.
  - É o Load Balancer mais inteligente e detalhado, porém, não é tão rápido.
  - É possível identificar o que um usuário está acessando e consequentemente direcionar o tráfego dele.
  - É capaz de visualizar a URL que foi requisitada.
  - Suporta apontamento para EC2, IP, Lambda, containers, etc.
  - Recomendado para micro services e containers (Docker, ECS)
    
- **Network Load Balancer (NLB - 2017)**
  - Aplicado para os protocolos **TCP**, **TLS (Secure TCP)**, **UDP** atuando nas camadas 3 e 4 do modelo OSI.
  - É o Load Balance mais rápido, com baixa latência e pode lidar com milhões de requisições por segundo.
  - **Possui latência de 100 MS contra 400 MS do ALB**.
  - Focado no tráfego de rede, baseado em roteamento IP.
  - ***Possui apenas 1 IP estático por AZ**.
  - Distribui percentualmente o tráfego de rede.
  - Interessante para jogos onde pecisa lidar com milhões de requisições por segundo.
  - Pode atuar no balanceamento de carga de:
   - Instâncias EC2.
   - IPs (*Devem ser privados*).
   - Application Load Balancers (ALB) - *Válida combinação do balanceamento de Rede TCP com o balanceamento HTTP de aplicação*.

- **Gateway Load Balancer - (GWLB - 2020)**
  - Atua como um ***Gateway de Rede** na camada 3 de rede do modelo OSI para o protocolo IP.
  - Aplicado para segurança, compliance, detecção de intrusão, atuando como um firewall.
  - Controla o tráfego baseando-se em IPs inseridos em Route Tables.
  - Utiliza o protocolo **GENEVE** na porta **6081**.

### ELB Cross Zone

Permite que o ELB disbribua o tráfego de entrada **igualmente e uniformemente entre todas as instâncias em todas as zonas de disponibilidade em que estão implantadas**.

Com o Cross Zone desabilitado, o ELB distribuirá o tráfego de entrada percentualmente considerando a quantidade de instâncias dentro de cada zona de disponibilidade.

- **Application Load Balancer (ALB)**
  - Habilitado por padrão.
  - Não é cobrado por inter AZ.

- **Network Load Balancer (NLB)**
  - Desabilitado por padrão.
  - É cobrado por inter AZ se for habilitado.

- **Classic Load Balancer (NLB)**
  - Desabilitado por padrão.
  - Não é cobrado por inter AZ.

### Connection Draining

Permite que as instâncias em execução terminem as conexões existentes antes de serem desativadas, garantindo que as solicitações em andamento sejam concluídas com êxito e que os usuários não sejam impactados pela interrupção de uma instância. 

A configuração do tempo de conexão para o Connection Draining pode ser personalizada para atender às necessidades específicas da aplicação.

## Auto Scaling Group (ASG)

- Escala automática de instâncias conforme picos de tráfego ou outras métricas definidas pelo usuário.
- Aumenta capacidade de uma instância ou a quantidade de instâncias conforme carga.
- Define-se o mínimo e o máximo de instâncias por configuração.
- Termina instâncias extras conforme a carga é reduzida.
- Capaz de identificar instâncias não saudáveis, terminá-las e iniciar uma nova instância para substituição.
- Não é cobrado, paga-se pelas instâncias provisionadas.

### ASG Template

Trata-se de um modelo que define as configurações e recursos de uma instância ou grupo de instâncias gerenciado por um **Auto Scaling Group**. 

É composto por informações tais como o tipo de instância, o tamanho da instância, a imagem da AMI, as configurações de segurança, as opções de monitoramento e escalabilidade, entre outros. 

### CloudWatch Alarms (CloudWatch)

É possível escalar o ASG baseado em alarmes do CloudWatch, e as regras de escalabilidade são configuradas por métricas.

#### Métricas para escalabilidade

- **CPUUtilization**
  - Média de uso de CPU entre as instâncias.

- **RequestCountPerTarget**
  - Número de requisições por instância.

- **Average Network in/out**
  - Média de tráfego de rede de entrada e saída de uma instância.

- **Custom Metric**
  - Métrica personalizada definida pelo usuário.

### Policies

- **Manual Scaling**
  - O dimensionamento é feito manualmente pelo usuário sem a ajuda do Auto Scaling.

- **Target Tracking**
  - Ajusta o tamanho do Auto Scaling Group com base em uma métrica.

- **Simple/Step Scaling**
  - Aumenta ou diminui o tamanho do Auto Scaling Group em incrementos fixos com base em uma métrica personalizada.
  - **Exemplo**: 
    - CPU > 70%, adicione 2 instâncias.
    - CPU < 30%, remova 1 instância.
  
- **Schedule Actions**
  - Permite que se programe alterações no tamanho do Auto Scaling Group com antecedência com base em padrões conhecidos.
    - **Exemplo**: Aumentar a quantidade de instâncias todas as sextas-feiras às 17h. 

- **Predictive Scalling**
  - Usa Machine Learning para prever necessidades de tráfego futuro com base em histórico.       

### ASG Cooldowns

Tratam-se de períodos de tempo em que o ASG evita ações de dimensionamento automático, como adicionar ou remover instâncias após uma alteração de escala.

O cooldown padrão é de 300 segundos (5 minutos), que é o período mínimo recomendado para permitir que as instâncias sejam iniciadas ou desligadas, configuradas e testadas antes de iniciar uma nova alteração de escala.


## RDS (Relational Database Service)

É um serviço de banco de dados relacional gerenciado pela AWS (**PaaS**), que suporta as *engines*:
- Postgres
- MySQL
- MariaDB
- Oracle
- Microsoft SQL Server
- Aurora (Banco de dados próprio da AWS)

O RDS inclui:
- Provisionamento automatizado e atualização de patches do sistema operacional.
- Backups contínuos e restauração em um *timestamp* específico.
- Painéis de monitoramento.
- Réplicas de leitura para otimizar o desempenho de leitura.
- Configuração Multi-AZ para recuperação de desastres (DR).
- Janelas de manutenção para atualizações.
- Capacidade de dimensionamento (vertical e horizontal).
- Armazenamento suportado pelo **EBS** (gp2 ou io1).

**Importante**: O RDS não suporta conexão SSH em suas instâncias.

### Storage Auto Scaling

- Capaz de aumentar o armazenamento das instâncias de banco de dados RDS dinamicamente.
- Ao detectar que está ficando sem armazenamento gratuito, o RDS escala automaticamente.
- Aconselhavel evitar o dimensionamento manual do armazenamento do banco de dados.
- Definir o limite máximo de armazenamento de banco de dados.
- Modifique automaticamente o armazenamento se:
  - O armazenamento livre for inferior a 10% do armazenamento alocado.
  - Se passaram 6 horas desde a última modificação.
- Útil para aplicações com cargas de trabalho imprevisíveis.

### Read Replicas

- Permite a escalabilidade de leitura segregando réplicas de uma instância de banco de dados.
- Suporta até 15 réplicas em uma AZ, Cross AZ ou Cross Region.
- A replicação entre a instância Master e as Réplicas, são assíncronas, gerando **Inconsistência Eventual**.

**Importante**: Read Replicas não suportam instruções de *INSERT, DELETE, UPDATE*, aceitam somente instruções de leitura, neste caso *SELECT*.

#### Read Replicas - Network Cost

- Para Read Replicas dentro de uma AZ ou AZs diferentes, porém, na mesma Region, não será cobrado pela taxa de transferência da replicação.
- Para Read Replicas em Regions diferentes (Cross Region), será cobrada pela taxa de transferência da replicação.

#### Multi-AZ (Disaster Recovery)

Trata-se de uma configuração que fornece resiliência em caso de falhas em uma AZ da AWS e consequentemente onde a instância RDS pode estar alocada.

- Ao habilitar o **Multi-AZ**, a AWS provisiona e mantém automaticamente e continuamente uma réplica da instância **Master** chamada **Stand By**, que será sincronizada em uma AZ secundária.
- Também utilizada para realização de manutenções programadas, atualizações de software e atualizações de patches de segurança. 
- A réplica **Stand By** pode ser promovida automaticamente a **Master** se houver uma interrupção na AZ primária, permitindo que as operações do banco de dados continuem sem interrupção.
- É uma opção para atender aos requisitos de recuperação de desastres, permitindo a recuperação de um banco de dados em outra região da AWS em caso de falha da região principal.
- Quando a promoção para **Master** é concluída, o DNS do banco de dados é atualizado para apontar para o novo endereço IP primário.
- A antiga instância **Master** é convertida em uma réplica para permitir a recuperação e a reparação dela, caso necessário.
- Multi-AZ mantém a mesma string de conexão independentemente de qual banco de dados está ativo.

### RDS Custom

Trata-se do recurso do RDS que permite a execução de instâncias de banco de dados em uma instância EC2 permitindo ao usuário flexibilidade e controle, como por exemplo acesso SSH, instalação de bibliotecas, etc. 

#### RDS vs RDS Custom

- **RDS**: O banco de dados e o sistema operacional serão gerenciados pela AWS.
- **RDS Custom**: Acesso administrativo total ao sistema operacional e ao banco de dados.

**Porém, o gerenciamento automático ofertado pelo RDS (PaaS) é desabilitado**, de forma que o usuário terá toda autonomia de gerenciamento do banco de dados sob o RDS Custom.

### Aurora

Trata-se de uma tecnologia proprietária da AWS (Não é Open Source), e foi criado para ser compatível com MySQL e Postgres, ou seja, podemos nos conectar em um banco de dados Aurora como se fosse MySQL ou Postgres.

- Possui **5 vezes mais desempenho em relação ao RDS MySQL** e **3 vezes mais desempenho em relação ao RDS Postgres**.
- O armazenamento cresce automaticamente, iniciando com 10GB e pode subir até 128TB conforme a inclusão de dados.
- Suporta 15 Read Replicas com um atraso inferior a 10 ms.
- Seu custo é cerca de 20% maior, porém, muito mais eficiênte.
- 6 cópias dos dados em 3 AZ:
  - 4 cópias de 6 necessárias para gravações.
  - 3 cópias de 6 necessárias para leituras.
  - O armazenamento é dividido em centenas de volumes.

#### Custom Endpoints

Tratam-se de Read Repĺicas que possuem DNS exclusivos e que permitem associação a instâncias com maior poder computacional para que possam receber maiores cargas de trabalho, como por exemplo consultas complexas.

#### Aurora Serverless

Trata-se da modalidade sem servidor do Aurora, e permite o dimensionamento automático de computação e armazenamento do banco de dados de acordo com a demanda.

- Diferente do Aurora RDS, não há necessidade de provisionar instâncias de banco de dados. 
- O Aurora Serverless é uma opção econômica para cargas de trabalho com picos de tráfego imprevisíveis.
- Gerencia automaticamente a escalabilidade, o desempenho, a disponibilidade, a segurança e as tarefas administrativas, permitindo que os desenvolvedores se concentrem na construção de aplicações.
- É capaz de desligar o banco de dados quando não está sendo usado, reduzindo significativamente os custos.
- É cobrado por segundo de uso.

**Observação do Autor**: Podemos fazer um paralelo com o **Fargate** para o ECS, onde não é necessário o provisionamento de instâncias EC2 para gestão dos containers.

#### Aurora Multi-Master

Trata-se de uma configuração que permite a criação de diversos bancos de dados **Master** em uma única instância do Aurora, permitindo a criação de várias cópias que podem receber gravações.

- Os clientes podem realizar gravações em qualquer um dos bancos de dados Master sem conflitos, o que ajuda a escalar aplicações críticas em termos de leitura/gravação.
- Aumenta a disponibilidade, pois, em caso de falha em um dos bancos de dados Master, outros bancos de dados Master podem assumir a carga de trabalho imediatamente.

#### Global Aurora 

Permite que o banco de dados esteja disponível em várias regiões geográficas (**Regions**) aumentando a disponibilidade.

- É possível criar uma réplica primária em uma região primária e réplicas secundárias em outras regiões secundárias. 
- As réplicas secundárias são sincronizadas continuamente com a réplica primária, leitura e gravação podem ser roteadas para qualquer réplica global, independentemente de sua localização geográfica.

#### Aurora Machine Learning

Permite a utilização de modelos de aprendizado de máquina (*Machine Learning*) para melhorar o desempenho e a disponibilidade do banco de dados.

Suporta os serviços:
- AWS SageMaker.
- AWS Comprehend.

**Casos de uso**: Detecção de fraude, segmentação de anúncios, análise de sentimentos, recomendações de produtos, etc.

### Backup e Restore

#### RDS Backup 

- **Backup Automatizado**
  - Realiza backup diário do banco de dados (durante a janela de backup).
  - Os logs de transações são copiados pelo RDS a cada 5 minutos.
  - Capaz de restaurar a qualquer ponto no tempo (do backup mais antigo até 5 minutos atrás).
  - Possui de 1 a 35 dias de retenção (*Para desabilitar os backups automáticos defina 0 dias*).
  - Os backups automáticos expiram.

- **Backup Manual - Snapshots**
  - É acionado manualmente pelo usuário.
  - Retenção de backup pelo tempo que se desejar.
  - Os backups manuais não expiram.

#### Aurora Backup

- **Backup Automatizado**
  - Possui retenção de 1 a 35 dias (*Não pode ser desativado*). 
  - Possibilita recuperação pontual durante o período de retenção.

- **Backup Manual - Snapshots**
  - É acionado manualmente pelo usuário.
  - Retenção de backup pelo tempo que se desejar.
  - Os backups manuais não expiram.

### Restore (RDS & Aurora)

- Resturação de backup RDS, Aurora ou um Snapshot:
  - É possível a restauração de um backup automatizado ou snapshot criando um novo banco de dados a partir deste backup ou snapshot.

- Resturação de um banco de dados RDS a partir do S3.
  1. Cria-se um backup do banco de dados.
  2. Armazena-se o backup como um objeto em um bucket S3.
  3. Restaura-se o backup em uma nova instância RDS a partir do objeto no bucket S3.

- Resturação de um banco de dados Aurora a partir do S3.
  1. Cria-se um backup do banco de dados usando o **Percona XtraBackup**.
  2. Armazena-se o backup como um objeto em um bucket S3.
  3. Restaura-se o backup em um novo cluster Autora a partir do objeto no bucket S3.

### Aurora Cloning

Trata-se do recurso capaz de criar um novo cluster Aurora a partir de um cluster existente.

- Mais rápido que Restore e Snapshot.
- Utiliza o protocolo **copy-on-write**.
  - O novo cluster utiliza o mesmo volume de dados do cluster original. 
  - Quando o novo cluster sofre autalizações, o armazenamento adicional e os dados são copiados para que estejam separados.
- Recomendado para criar bancos de dados de desenvolvimento ou testes a partir de um banco de dados de produção sem gerar impactos no ambiente produtivo.
  
### Security (RDS & Aurora)

É possível criptografar os dados no RDS e Aurora, isso significa que os dados armazenados estarão criptografados nos volumes.

- **Criptografia em Repouso**
  - Os bancos de dados (*Master e Replicas*) são criptografados utilizando o AWS KMS, e a criptografia deve ser habilitada no momento do lançamento da instância.
  - Se o banco de dados *Master* não for definido para utilizar a critografia, as *Replicas* não serão criptografadas.
  - Para criptografar um banco de dados que não está criptografado, será necessário criar um snapshot deste banco, e criar uma nova instância a partir desse snapshot habilitando a criptografia.
  - O banco de dados Oracle não suporta *IAM Database Authentication*.

- **Criptografia em Trânsito**
  - Deve-se ter comunicação segura entre cliente e servidor utilizando certificado TLS.

- **IAM Role**
  - Utilização de Roles do IAM para conectar a um banco de dados como camada de segurança adicional.

- **Security Groups**
  - Controle de acesso de rede para canectar a um banco de dados (Entradas e saídas nas portas).

- **CloudWatch Logs**
  - Os logs podem ser habilitados e enviados para o CloudWatch e ter uma retenção mais longa.

### RDS Proxy

É possível reforçar a segurança das instâncias RDS utilizando o RDS Proxy, que é um proxy de banco de dados totalmente gerenciado para RDS. As aplicações não se conectam diretamente ao banco de dados, e sim ao proxy para que este se conecte ao banco de dados.

Otimiza a eficiência caso a instância possua muitas conexões abertas, o RDS Proxy pode agrupá-las minimizando a sobrecarga.

- Reduz a sobrecarga nos recursos do banco de dados (*CPU, RAM*) e minimiza as conexões abertas (*timeouts*).
- Serverless, autoescalável e altamente disponível (multi-AZ).
- Reduz o tempo de failover do RDS e Aurora em até 66%.
- Suporta RDS (MySQL, PostgreSQL, MariaDB, MS SQL Server) e Aurora (MySQL, PostgreSQL).
- Aplica autenticação IAM para o banco de dados e armazena as credenciais no AWS Secrets Manager.
- Não é acessível publicamente (deve ser acessado a partir da VPC).

## Elastic Cache

Trata-se de um serviço gerenciado pela AWS de banco de dados em memória que oferece suporte ao **Redis** e ao **Memcached**, abstraindo e simplificando as configurações, escalabilidade e gerenciamento de um cluster de cache, além de ter alto desempenho e baixa latência.

- Colabora para reduzir a carga do bancos de dados em operações de leitura intensas.
- Torna a aplicação **Stateless**.
- AWS se responsabiliza pela manutenção, otimizações, configuração, monitoramento, recuperação de falhas e backups.

**Redis**: Banco de dados em memória de código aberto (*Open Source*) que suporta armazenamento em disco.
- Multi AZ com failover automático.
- Réplicas de leitura para dimensionar leituras e tem alta disponibilidade.
- Recursos de backup e restauração.

**Memcached**: Sistema de cache em memória de código aberto (*Open Source*) com recursos limitados como suporte a strings e cache distribuído.
- Multi-node para particionamento de dados (*sharding*).
- Arquitetura multi thread.
- Não possui alta disponibilidade (*replicação*).
- Não possui persistência.
- Não possui backup e restore.

### Elastic Cache Security 

- Oferece suporte à autenticação IAM para Redis.
- As políticas IAM no ElastiCache são usadas apenas para Segurança no nível da API da AWS.
- Redis AUTH:
  - É possível definir uma senha/token ao criar um cluster Redis e forçar os usuários se autenticarem com essas credenciais.
  - É um nível adicional de segurança para o cache.
  - Suporte SSL para criptografia de trânsito.
- Memcached
  - Suporta autenticação baseada em SASL.

### Elastic Cache Patterns

- **Lazy Loading**
 - Os dados são carregados do banco de dados para o cache somente quando são solicitados pela aplicação (*sob demanda*), podendo ficar obsoletos.
 - Evita a sobrecarga da aplicação e banco de dados, e otimiza o uso do cache.

- **Write Through**
  - Insere ou atutaliza os dados no cache no mesmo momento em que ocorre uma inclusão ou atualização no banco de dados.
  - Garante que os dados mais recentes estejam sempre disponíveis em cache.
  - Os dados não ficam obsoletos.

- **Session Store**
  - Os dados são temporariamente armazenados no cache para reduzir o tempo de resposta da aplicação e melhorar a experiência do usuário (*TTL*).
  - Usado para armazenar dados da sessão de um usuário, como informações de login, carrinho de compras, preferências, etc.
  - Evita a necessidade de acessar o banco de dados a todo momento.
  - Alteranativa ao **ALB Stickness Sessions**.

### Sorted Sets

Trata-se de um tipo de estrutura de dados do Redis que armazena dados em pares chave-valor, com a diferença de que os valores são ordenados com base em uma pontuação (score) atribuída a cada valor.

- **Caso de Uso**
 - Jogo online, onde é necessário manter uma classificação dos jogadores baseada em pontuações. Nesse caso, é possível usar o Redis Sorted Set para armazenar as pontuações como os valores do conjunto e os nomes dos jogadores como as chaves. 

### Lista de Portas 

#### Comuns

- FTP: 21
- SSH: 22
- SFTP: 22 (mesma da SSH)
- HTTP: 80
- HTTPS: 443

#### Banco de Dados

- PostgreSQL: 5432
- MySQL: 3306
- Oracle RDS: 1521
- Microsoft SQL Server: 1433
- MariaDB: 3306 (same as MySQL)
- Aurora: 5432 (PostgreSQL) or 3306 (MySQL)

## Desacoplamento - Integração e Mensageria

Comunicação **assíncrona** trata-se da integração entre múltiplas aplicações por meio troca de informações a partir de eventos trafegados em recursos de mensageria.

- SQS: Modelo de filas.
- SNS: Modelo pub/sub.
- Kinesis: Modelo de stream em tempo real.

### SQS (Simple Queue Service)

Serviço de filas geranciado pela AWS (**PaaS**) para desacoplamento de aplicações, que fomenta a comunicação assíncrona.

#### SQS Security

- Criptografia
  - Em trânsito usando API HTTPS.
  - Em repouso usando AWS KMS.
  - Criptografia do lado do cliente por conta própria.

- Controle de Acesso
  - Políticas do IAM para controle de acesso API do SQS.

- Políticas de Acesso
  - Útilizado para acesso a filas SQS em contas AWS distintas (*Cross Account*).

#### Visibility Timeout

Recurso que garante que uma mensagem se torne invisível para oturos consumidores por um período de tempo definido, enquando outro cosumidor já estiver processando. Após esse *timeout*, a mensagem estará disponível para ser processada pelos demais consumidores.
	
- O visibility timeout é ajustável entre 0 e 12 horas (**Por padrão o timeout é ajustado para 30 segundos**).
- Se uma mensagem não for processada dentro do visibility timeout, ela será processada duas vezes.
- Se o visibility timeout for alto (horas) e o consumidor demorar a processar a mensagem, o reprocessamento levará bastante tempo.
- Se o visibility timeout for muito baixo (segundos), pode existir mensagens duplicadas.
- A API **ChangeMessageVisibility** permite que o consumidor obtenha mais tempo para processar a mensagem.
- A API **DeleteMessage API** notifica o SQS que a mensagem foi processada.

#### Long Polling

Recurso que visa reduzir a quantidade de requisições para uma fila SQS via API, ou seja, ao invés de fazer requisições repetidas para verifificar a existência de novas mensagens na fila, o SQS mantém uma conexão aberta por um período de tempo préviamente especificado, e quando a mensagem é recebida, é imediatamente disponibilizada otimizando latência e custo de chamadas a API.

- Fornece a opção de aguardar pela chegada de novas mensages na fila caso estiver vazia. O SQS mantém a conexão aberta durante o tempo determinado no Long Polling.
- Reduz o número de requisições na API do SQS, aumentando a eficiência e reduzindo os custos.
- O tempo de espera (*Wait Time*) pode ser ajustado entre 1 segundo (min) a 20 segundos (max) (recomendado para a maioria dos casos).
- Pode ser habilitado no nível da fila ou no nível da API usando o parâmetro **WaitTimeSeconds**.

### FIFO Queue (First In / First Out)
		
- A primeira mensagem a entrar na fila, será a primeira mensagem a sair.
- **As mensagens são processadas em ordem.**
- Por convenção, o nome da fila deve terminar com **.fifo (Exemplo: **nome-da-fila.fifo)**.
- **Possui baixo **Throughtput (taxa de transferência)*, 300 mensagens por segundo sem lote e 3000 mensagens por segundo em lote**.
- Não possui delay por mensagem, somente delay por fila.
- Garante que uma mensagem não seja entregue duas vezes para um mesmo consumidor dentro de um intervalo de tempo especificado.

### Standard Queue
		
- Capaz de escalonar de 1 até 10.000 mensagens por segundo.
- Armazena uma mensagem de 4 a 14 dias **Default Retention of Message**.
- Não existe limite de quantas mensagens podem ser armazenadas na fila.
- Capaz de escalonar consumidores horizontalmente.
- Podem existir mensagens duplicadas.
- **Não garante ordenação das mensagens (*Best Effort Ordering*)**.
- Suporta no máximo mensagens de até 256 KB.
- **Possui **Throughtput (taxa de transferência)* ilimitado**.
- Baixa latência (menos 10 ms na publicação e recepção de mensagens).
- Limitação de 256 KB por mensagem enviada.
- As mensagens podem ser lidas em paralelo por instâncias consumidoras.
- É possível escalar instâncias em ASG a partir do tamanho da fila, por meio de alarmes no CloudWatch com a métrica disponível no SQS **ApproximateNumberOfMessages**.

### SNS (Simple Notification Service)

Recurso para notificações de mensagens de um assinante para um ou mais destinatários (**Pub Sub**).

- Funciona na abordagem *Publish/ Topic / Subscriber*.
- Um produtor de eventos (**Producer**) envia mensagens somente para um tópico SNS *(1 : N)*.
- Suporta até **100.000** tópicos SNS como limite.
- Suporta até **12.500.000** de assinantes (**Subscribers**) por tópico SNS.
- Cada assinante receberá todas as mensagens enviadas.
- Possui o recurso para filtro de mensagens *(documentos JSON dentro das configurações do tópico)*.

#### SNS Security

- Criptografia
  - Em trânsito usando API HTTPS.
  - Em repouso usando AWS KMS.
  - Criptografia do lado do cliente por conta própria.

- Controle de Acesso
  - Políticas do IAM para controle de acesso API do SQS.

- Políticas de Acesso
  - Útilizado para acesso a tópicos SNS em contas AWS distintas (*Cross Account*).
  - Útil para permitir que outros serviços AWS produzam mensagens em um tópico do SNS.

#### Mailinator

 Serviço de e-mails descartáveis, gratuito e sem necessidade de registro, aderente a testes no SNS e SES.

- https://www.mailinator.com/

**Observação**: O Kinesis Data Streams não é compatível com o SNS, o Kinesis Firehouse sim.

#### Fun-Ont

### Kinesis

Recurso para coleta, processamento e análise de *stream* de dados em tempo real. Fomenta a ingestão de dados como logs de aplicação, métricas, cliques de sites, dados de IoT, vídeos, etc.

### Kinesis Data Stream

- On Demand
  - Há um nível gratuíto.

## Route 53

Trata-se do serviço da AWS de escopo global para gerenciar DNS (Domain Name System).

- O nome "53" é dado porque funciona na porta 53.
- Monitora os servidores para roteamento de tráfego.
- Roteia o tráfego para servidores mais próximos.
- Capaz de verificar a saúde dos recursos.
- **Único serviço da AWS que oferece 100% de SLA de disponibilidade**.
- Resumo: Possui registro de domínios, DNS, Health Checks, Routing Policy.

### DNS

**DNS - Domain Name Service** é o serviço responsável por traduzir endereços IP para nomes amigáveis.

- **Exemplo**: Para o endereço IP *172.217.18.36* temos o DNS *www.google.com*.

### Record (Registro)

Trata-se da configuração responsável por associar um *hostname (nome de domínio)* a um recurso como um IP ou um CNAME. Ou seja, direciona o tráfego DNS para o local correto de acordo com a requisição do usuário.

#### Record Types

- **A**: Mapeia um *hostname* para um endereço IP IPv4.
- **AAAA**: Mapeia um *hostname* para um endereço IP IPv6.
- **CNAME**: Mapeia um *hostname* para um outro nome de domínio.
  - O destino é um hostname que deve ter um registro A ou AAAA.
  - Não é possível criar um registro CNAME para o nó superior de um namespace DNS (zona
Apex).
  - Exemplo: Não é possível criar para *exemplo.com*, mas é possível de criar para *www.example.com*.
- **NS**: Servidores de nome para Hosted Zone.
  - Controla como o tráfego é roteado para um domínio.

### Hosted Zones

Tratam-se de um conteiner para manter informações sobre registros de DNS para um domínio específico. Permite o gerenciamento das configurações de DNS para os domínios. 

- **Public Hosted Zone**
  - Responsável por rotear solicitações para DNS públicos na internet.
  - **Exemplo**: aplicacao.dominiopublico.com

- **Private Hosted Zone**
  - Responsável por rotear solicitações para DNS privados dentro uma rede privada como por exemplo uma VPC.
  - **Exemplo**: aplicacao.empresa.interno

### TTL (Time to Live)

Define por quanto tempo um registro DNS deve ser armazenado em cache antes de ser atualizado. 

- **High TTL** (Exemplo: 24 horas)
  - Menor tráfego no Route 53.
  - Risco de registros desatualizados.

- **Low TTL** (Exemplo: 60 segundos)
  - Maior tráfego no Route 53, isso significa maior custo também.
  - Registros desatualizados por menos tempo.
  - Simples para atualizar registros.

Para registros de Alias, o TTL é obrigatório para cada registro de DNS.
Cada registro DNS tem um TTL que ordena por quanto tempo armazenar os valores em cache esses para não sobrecarregar o DNS.

### CNAME vs Alias

- **CNAME**
  - Usado para criar um apelido ou alias para um domínio ou subdomínio, e direciona as consultas de DNS para o nome de destino.
  - Apenas para domínios que não são raís.

- **Alias**
  - Tipo de registro *(Record)* exclusivo no Route 53.
  - Usado para mapear um nome de domínio para recursos AWS *(ELB, CloudFront, S3 Website, Beanstalk, VPC Interface Endpoint, Global Accelerator)*.
  - Não funciona para DNS de instâncias EC2.
  - Funciona para domínios que são raíz e para os que não são.
  - Não é cobrado.
  - Possui *Health Check* nativo.

### Health Check

Recurso que permite o monitoramento da saúde e disponitilidade de um endpoint, como um servidor web, instâncias EC2, Load Balancers, etc.

- **Monitor an Endpoint**: Verifica a disponibilidade de um endpoint específico.
- **Calculated Health Checks**: Verifica a disponibilidade de um conjunto de endpoints.
- **Private Hosted Zones**: Verifica a disponiblidade de endpoints internos em uma VPC em uma infraestrutura privada.

### Políticas de Roteamento (Routing Policies)

Tratam-se de regras utilizadas pelo Route 53 para determianr como as aplicações serão distribuídas e como vão responder as consultas DNS.

- **Simple**
  - Fará uma consulta ao servidor DNS e obterá o IPV4 correspondente como resposta.
  - Roteia o tráfego de requisições para um único recurso.
  - Suporta várias valores para um mesmo registro.
  - Única política que não possui Health Check.

- **Wighted**
  - Distribui percentualmente o tráfego de requisições entre diversos recursos.
  - Semelhante a um Load Balancer, mas em uma ótica de roteamento de DNS.
  - Possui Health Check.

- **Latency**
  - Direciona o tráfego conectando usuários aos servidores mais próximos.
  - Baseia-se na distância entre usuários e Regions AWS, reduzindo a latência.
  - Possui Health Check.

- **Failover**
  - Possui uma instância *primária* e uma instância *failover* evitando desastres *(desaster recover)*.
  - Verifica a saúde da instância primária, caso falhe, direciona o tráfego para a instância failover.
  - Possui Health Check. 

  - **Geolocation**
    - Direciona as requisições para uma localização geográfica específica *(Continente, País, Estado)*.
    - Diferentemente do *Latency*, se baseia na localização geográfica do usuário.
    - Possui Health Check. 

  - **Geoproximity**
    - Direciona as requisições considerando a proximidade geográfica entre o usuário e o endpoints mais próximo.
    - Visa reduzir a distância entre usuário e recursos AWS basenando-se na localização geográfica dos usuários e recursos AWS e recursos não AWS.
    - Suporta a transferência de tráfego entre regiões com base no parâmetro **BIAS**, especificando os valores de polarização. *É possível previlegiar determinadas regiões independente de estarem mais próximas ou mais distantes*.
    - Possui Health Check. 

  - **IP-Based**
    - Considera o endereço IP do cliente para direionar suas requisições para recursos baseando-se em *ranges* específicos de endereços IP.
    - Otimiza performance e reduz custos de rede.
    - Possui Health Check. 

  - **Multi Value**
    - Permite distribuir o tráfego das requisições entre mútiplos recursos de destino de forma equilibrada.
    - É semelhante a um Load Balancer, mas seu objetivo é o balanceamento de carga no lado do cliente.
    - Possui Health Check. 

## Elastic Beanstalk

Trata-se de um serviço centralizado para implantar, gerenciar e escalar aplicações Web, simplificando os processos de implantação e provisionamento de recursos de infraestrutura tais como servidores, balanceadores, bancos de dados e tarefas como monitoramento e escalonamento automático.

- Plataforma como serviço (PaaS), gerencia-se somente dados e aplicações.
- Suporta a implantação de aplicações como *Docker, Go, NodeJs, PHP, Python, .Net (IIS e .Net Core), Apache, NGINX*, etc.
- Abstrai os serviços como *EC2, ELB, ASG, RDS, Security Group, Elastic IP*, etc, peocupa-se apenas com a codificação das aplicações.
- Serviço gratuito, paga-se pelas instâncias provisionadas.
- Suporta monitoramento, envia métricas para o CloudWatch, verifica saúde das aplicações hospedadas.
- Pode ser usado para monitorar e verificar a integridade de um ambiente.
- Cria uma stack CloudFormation no momento da criação dos recursos que serão utilizados.

## S3 (Simple Storage Service)

Trata-se de um serviço para armazenamento de objetos seguro, escalável e altamente disponível.

- Possui capacidade **infinita** de armazenamento de objetos em *Buckets*.
- Possui escopo global.

- **Casos de Uso**
  - Backup e armazenamento.
  - Desastres *(Disaster Revovery)*.
  - Arquivo.
  - Armazenamento para Cloud Híbrida.
  - Hospedagem de mídias.
  - Data Lakes e Big Data.
  - Entrega de software.
  - Websites estáticos.

### Buckets

Os objetos *(Arquivos)* são armazenados em diretórios conhecidos como **Buckets**.

- Devem ter **nome único global** para todas as contas e regiões da AWS.
- Embora o S3 seja um serviço de escopo **global**, os Buckets são criados em nível **regional (AWS Region específica)**.
- Os Buckets podem ter pastas internas para armazenamento dos objetos conhecidas como **Prefix (Prefixo)**.

- **Convernção para nomear Buckets**:
  - Não deve conter letras maiúsculas e *Underscore*.
  - Deve ter entre 3 e 63 caracteres.
  - Não pode ser um IP.
  - Deve iniciar com letra minúscula ou um número.
  - Não deve ter o sufixo *-s3alias*.

### Objects 

Trata-se do conteúdo armazenado nos Buckets, podem ser arquivos, vídeos, websites estáticos, imagens, etc.

- O tamanho máximo suportado para um objeto é *5TB (5000 GB)*.
- Para carregar um arquivo maior que 5GB, considerar o uso do *multi-part Upload*, para que o arquivo seja carregado em pequenas partes.

### Security

- **Used-Based** 
  - *IAM Policy*: Chamadas de API permitidas a um usuário IAM específico.
  
- **Resource-Based**
  - *Buckets Policies*: Mais comuj, as regras são aplicadas ao Bucket via Console AWS, permite *Cross Accont*.
  - *Object Access Control List (ACL)*: - granularidade mais fina, pode ser desabilitado.
  - *Bucket Access Control List (ACL)*: - Menos comum, pode ser desabilitado.

- É possível permitir acesso a um Bucket por usuários de outras contas AWS via Bucket Policy  permitindo *Cross Account*.
- Objetos em um Bucket podem ser criptografados.

- **Block Public Access** fornece uma camada de segurança adicional para não permitir acesso público ao Bucket, **é habilitado por padrão**.

#### Bucket Policies

Tratam-se de políticas de acesso no formado *JSON* aplicadas a um determinado Bucket. Essas políticas definem permissões granulares para controlar o acesso aos objetos armazenados e especificam quais ações serão permitidas ou negadas para diferentes usuários, grupos de usuários ou até mesmo para todo o público.

- Abaixo segue um exemplo de uma política que permite acesso para que qualquer usuário obtenha os objetos contidos em um Bucket chamado *nome-do-bucket*:

```hcl
{
  "Version": "2012-10-17", // Versão da política do IAM
  "Statement": [ // Lista de declarações (statements) na política.
    {
      "Sid": "AllowPublicGetObject", // Identificador único da declaração
      "Effect": "Allow", // Acesso permitido ou negado, neste caso permitido
      "Principal": "*", // Conta ou usuário que terá acesso permitido ou negado, neste caso todos terão acesso.
      "Action": "s3:GetObject", // API com a ação permitida, neste caso obter objetos
      "Resource": "arn:aws:s3:::nome-do-bucket/*" // Recurso (Resource Name) ao qual a política se aplicará (bucket e objetos)
    }
  ]
}
```

- **Documentação Oficial da AWS referente a Bucket Policies**:
  - (https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-iam-policies.html)


- **AWS Policy Generator**
  - Ferramenta que permite criar políticas que controlam o acesso a produtos e recursos da AWS.
  - (https://awspolicygen.s3.amazonaws.com/policygen.html)


### Website Estático

Trata-se do recurso do S3 que permite que hospedar sites estáticos *(HTML, CSS, Javascript, imagens, etc)* em Buckets e torná-los acessíveis na internet.

### Versionamento (Versioning)

Trata-se de uma configuração que permite versionar os objetos armazenados em um Bucket.

- É habilitado a nível de Bucket.
- Uma vez habilitado não há como desabilitar, é possível suspender.  
- Recomendado para evitar deleções assidentais de objetos.
- É possível restarurar versões anteriores de objetos deletados.
- Cada versão de objeto é uma cópia física do objeto original, portanto, o armazenamento aumenta com as versões e consequentemente o custo.
  - **Exemplo**: *Para 1 objeto com 2 versões, temos 3 objetos armazenados no Bucket*.           
- A quantidade de versionamentos de objetos é ilimitada.

### Replicação de Objetos (Replication)

Trata-se do recurso que permite a cópia automática de objetos entre Buckets em regiões diferentes.

- Para utilizar a replicação, os Buckets de origem e destino devem ter o versionamento habilitado.

- **Cross Region Replication (CRR)**
  - Replicação de objetos entre buckets em regiões diferentes, garantindo a durabilidade dos dados em diferentes localizações geográficas.

- **Same Region Replication (SRR)**
  - Replicação de objetos entre buckets na mesma região, fornecendo redundância de dados dentro da mesma área geográfica para fins de alta disponibilidade.

### Storage Classes

- **Standard - General Purpose**
  - Indicado para *Upload e Download* com frequencia muito alta.
  - 99,99% disponível.
  - Baixa latência e altas taxas de transferência.
  - Envia os objetos para 3 ou mais AZs.
  - É o mais caro, porém, mais rápido e mais confiável.

- **Standard-Infrequent Access (IA)**
  - Indicado para *Upload e Download* com baixa frequencia, por exemplo, uma vez por semana.
  - 99,9% disponível *(Pouco menos disponível que o Standard)*.
  - Casos de uso: Desastres e backups.
  - Envia os objetos para 3 ou mais AZs.
  - Consequentemente, paga-se mais barato que o Satandard.

- **One Zone-Infrequent Access**
  - Os objetos serão armazenados em uma única AZ *(Zona de Disponibilidade)*.
  - 99,5% disponível.
  - 99.999999999% durável.
  - Indicado se momentos de indisponibilidade *(minutos ou horas)* não for um problema.
  - Paga-se menos.

- **Glacier** 
  - Recomendado para backup, quando não precisa de acesso imediato.
  - Não é disponibilizado para *download* no mesmo momento do *upalod*.
  - Nessa classe, a AWS envia os objetos para servidores mais lentos, porém com muito mais espaço.
  - **É cobrado pelo armazenamento e recuperação do objeto**.
  - *Seria como colocar os arquivos em uma geladeira*.

- **Glacier Deep Archive**
  - Recomendado para Backup, e a frequencia de acesso é extremamente baixa.
  - Classe mais barata de todas.
  - Após o *uplaod*, o *download* será possível após 12 horas.
  - *Seria como colocar os arquivos em um freezer*.

- **Glacier Instant Retrieval**
 - Recuperação em milissegundos, indicado para objetos acessados ​​uma vez por trimestre.
 - Duração mínima de armazenamento de 90 dias.

- **Glacier Flexible Retrieval**
  - Duração mínima de armazenamento de 90 dias.
    
- **Intelligent Tiering**
  - Mantém na classe Standard e de acordo com a frequencia de uso move os objetos automaticamente para as classes mais baratas.
  - Balanceia automaticamente os custos.
  - Envia os objetos para 3 ou mais AZs.
  - Duração mínima de armazenamento de 180 dias.

### Ciclo de Vida (Lifecicle)

Recurso utilizado para mover objetos entre as classes de armazenamento dos Buckets.
    
- Para objetos acessados ​​com pouca frequência, mova-os para o **Standard-Infrequent Access**.
- Para objetos que não necessitam de acesso rápido, mova-os para **Glacier** ou **Glacier Deep Archive**.
- Objetos em constante movimento podem ser automatizados usando regras de ciclo de vida.

- **Transition Actions**
  - Transição de objetos de uma classe de armazenamento para outra.
  - Move objetos para classe **Standard-Infrequent Access** 60 dias após a criação.
  - Mover objetos para o **Glacier** para arquivamento após 6 meses.

- **Expiration Actions**
  - Objetos expiram após algum tempo.
  - Os arquivos de log de acesso podem ser configurados para serem excluídos após 365 dias.
  - Pode ser usado para excluir versões antigas de objetos *(se o controle de versão estiver ativado)*.
  - Pode ser usado para excluir *Multi-Part uploads* incompletos.

### Requester For Pay (Pagamento pelo Solicitante) 

Sabe-se que os proprietários de Buckets S3 pagam pelo armazenamento e pela transferência de dados em rede. O **Requester For Pay** permite que os custos sejam transferidos ao solicitante do *download ou upload* dos objetos. 

### Event Notifications

Tratam-se de notificações de eventos ocorridos em um objeto disparado por um Bucket, por exemplo:

- S3:ObjectCreated
- S3:ObjectRemoved
- S3:ObjectRestore
- S3:ObjectReplication
- etc.

- As notificações de eventos podem ser enviadas para diversos destinos como *SNS, SQS, Lambda, Event Bridge*.
  - *A partir do **Event Bridge**, é possível notificar mais 18 serviços AWS como destino dos eventos disparados pelo Bucket*.

- São necessárias permissões *IAM* para que o Bucket seja capaz de notificar os destinos, neste caso não se usa *IAM Roles*, define-se *IAM Policies*.

### S3 Select 

Permite recuperar um subconjunto específico de dados de um objeto armazenado no Bucket, de forma que não necessite recuperar o objeto inteiro. 

Utiliza consultas SQL para extrair dados diretamente dos objetos no formato CSV, JSON ou Parquet, reduzindo a quantidade de dados transferidos pela rede.

### S3 Analytics 

Fornece insights detalhados sobre o uso e acesso dos dados armazenados no Bucket, permitindo monitorar métricas de desempenho, como a quantidade de solicitações de acesso, tamanho dos objetos etc, de forma que seja possível otimizar custos.

### S3 Inventory

Fornece uma listagem detalhada de todos os objetos armazenados em um Bucket. Coleta informações sobre os objetos, como nome, tamanho, data de modificação e metadados associados.

### S3 Access Log 

Registra informações sobre as solicitações de acesso feitas aos Buckets como endereço IP do solicitante, ação solicitada, código de status da resposta, etc. Colabora para garantir a visibilidade e a rastreabilidade das operações realizadas.

### S3 Batch Operations 

Permite a execução de operações em lote em grandes conjuntos de objetos armazenados nos Buckets tais como cópia, exclusão, modificação de metadados e restauração de objetos do Amazon S3 Glacier.

### Criptografia

Os Buckets S3 permitem criptografia de objetos por meio de 4 métodos:

- **Server-Side Encryption (SSE)**

  - *Server-Side Encryption com Amazon S3-Managed Keys (SSE-S3)* **Habilitado por padrão**.
    - Criptografia de objetos utilizando chaves gerenciadas pela AWS.

  - *Server-Side Encryption com com KMS Keys armazenadas no AWS KMS (SSE-KMS)*.
    - Criptografia de objetos utilizando o **AWS KMS** para gerenciamento das chaves.
    - Controle total sobre a política de rotação da chave de criptografia.

  - *Server-Side Encryption com Customer-Provided Keys (SSE-C)*
    - Criptografia de objetos utilizando chaves gerenciadas pelo próprio usuário.
    - HTTPS é obrigatório.

- **Client-Side Encryption**
  - Criptografia gerenciada pelo usuário e desenvolvida utilizando bibliotecas *(Exemplo: Amazon S3 Client-Side Encryption Library)*.

### Multi-Part upload

Recurso que permite a transmissão de arquivos grandes dividindo-o em partes menores e transmitindo essas partes em paralelo, melhorando a velocidade de upload e a resiliência 
- Capaz de retomar o upload de onde parou em caso de falhas.
- Recomenda-se para arquivos maiores que 5GB.

### Transfer Acceleration

Recurso que aumenta a velocidade de transferência de um arquivo para um *Edge Location*, que encaminhará para o Bucket na Region de destino.
- **Foco na de transferência de dados específicos para o AWS S3**.
- Compatível com o *Multi-Part Upload*.

### CORS (Cross-Origin Resource Sharing)

Mecanismo que permite que uma URL de destino especifique quais URLs de origem estão autorizadas a fazer requisições para recursos hospedados em um determinado domínio. 

### MFA Delete

Configuração de segurança aplicada nos Buckets que exige autenticação por meio de um dispositivo *MFA (Multi-Factor Authentication)* para excluir objetos, acidionando uma camada extra de proteção para evitar exclusões acidentais ou maliciosas de dados críticos.

### Access Log

Registra as atividades de acesso aos Buckets, fornecendo informações detalhadas sobre operações de leitura, gravação e exclusão de objetos.

- Recomendado para fins de auditoria.
- Os logs das ações do Bucket principal serão escritos em outro Bucket adicional.
- Os logs podem ser analisados usando ferramentas de análise de dados.
- O Bucket de registro de logs deve estar na mesma região da que o Bucket principal.

Formatos de log para o S3 (https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html)

### URL Pré Assinada

Recurso que permite a geraçao de uma URL temporária e assinada para permitir que usuários acessem objetos específicos em um Bucket sem a necessidade de autenticação direta.

- Podem ser geradas a partir do Console S3, AWS CLI ou SDK.
- Expiração de uma URL Pré Assinada:
  - Console S3: 1 minuto até 720 minutos (12 horas).
  - AWS CLI: Configure a expiração com o parâmetro --expires-in em segundos (padrão 3.600 segundos, máx. 604.800 segundos ~ 168 horas)

### Glacier Vault 

Recurso que permite o bloqueio de um vault no Amazon S3 Glacier, impedindo alterações ou exclusões de objetos por um período definido.

- Garante a conformidade e a imutabilidade dos objetos armazenados, tornando-os invioláveis durante o período especificado.
- Colabora para atender a requisitos regulatórios e de governança.

### S3 Object Lock

Recurso que bloqueia a exclusão de versões de objeto por um período de tempo especificado.

- Retention Mode - Compliance
- Retention Mode - Governance
- Retention Period
- Legal Hold

### Access Point

Endpoint personalizado que permite o acesso granular e seguro aos objetos armazenados em um Bucket.

Cada Access Point possui:
- Seu próprio nome DNS (origem da Internet ou origem da VPC).
- Acess Point Policy (semelhante à política de Bucket).

### Object Lambda

Recurso que permite processar e transformar objetos no momento em que são solicitados, antes de serem retornados aos usuários. 

- Executa funções Lambda para personalizar e modificar os dados do objeto durante a recuperação, possibilitando a aplicação de lógica de negócios.
- Simplifica o processamento de objetos no Bucket, evitando a necessidade de pré-processamento externo antes do armazenamento.

## Cloud Front

Trata-se do recurso para entrega de conteúdo na Web via CDN (Content Delivery Network).

- É a versão da AWS de CDN (Content Delivery Network).
- Armazena conteúdo em cache em todo o mundo.
- É composto por 216 pontos de presença *(Edge Locations)*.
- Capaz de solucionar problemas de latência por localização.
- Faz cópias de um web site para a localização mais próxima ao usuário.
- Integra-se com WAF e Shield para prevenção de ataques.

### Global Acceleration

melhorar a disponibilidade, a performance e a segurança de aplicações públicas.

Recurso que melhora a disponibilidade e performance global de aplicações usando a rede global da AWS.

- Aproveita a rede interna da AWS para otimizar a rota das aplicações em cerca de 60%.
- As Edge Locations enviam o tráfego para as aplicações.
- Diferentemente do CloudFront, não possui armazenamento em cache, e funciona para aplicações executadas em uma ou mais regiões da AWS.

## Snow Family

Tratam-se de dispositivos *offline* **físicos, portáteis e altamente seguros** para coletar, processar e migrar dados para dentro e fora da AWS.

- **Snowball Edge**
  - Solução física para transporte e migração de dados.
  - Move a importância de *TBs ou PBs* de dados para dentro ou para fora da AWS.
  - Recomendado para grandes migrações de dados, desaster recovery.
        
  - **Snowball Edge Storage Optimized**
    - **80TB** de capacidade de HDD para volume de bloco e objeto compatível com S3.

  - **Snowball Edge Compute Optimized**   
    - **42TB** de capacidade de HDD para volume de bloco e objeto compatível com S3.

- **Snowcone**
  - Pequeno e portátil, robusto e seguro, resiste a ambientes agressivos.
  - **8TB** de capacidade para uso.
        
- **Snowmobile**
  - Transfere exabytes de dados (1EB = 1.000PB = 1.000.000TBs).
  - Cada Snowmobile tem 100 PB de capacidade (use vários em paralelo).
  - Alta segurança: temperatura controlada, GPS, vigilância por vídeo 24 horas por dia, 7 dias por semana.
  - Superior ao Snowball se transferir mais de **10PB**.

### Transferindo do Snowball para Glacier

Não é possível transferir dados diretamente do Snowball para o Glacier, a estratégia é transferir os dados do Snowball para um Bucket S3, e via *Lifecycle*, transferir do Bucket para o Glacier.

## FSx (Fast Storage File system)

Trata-se do sistema de arquivos de alta performance gerenciado pela AWS.

- É uma alternativa ao EFS e ao S3.
- É o mesmo que RDS para banco de dados, mas para arquivos.
- Pode reduzir os custos de armazenamento em 50 a 60%.

- **Fsx for Windows** 
  - Sistema de arquivos para cargas de trabalho corporativas.
  - Sistema de compartilhamento nativo do Windows.
  - Suporta os protocolos SMB (Server Message Block) e Windows NTFS.
  - Integra-se com Microsoft Active Directory.
  - Pode ser acessado da AWS ou da infraestrutura local *(on-premise)*.

- **FSx for Lustre (Linux Cluster)**
  - Sistema de arquivos para cargas de trabalho de alto desempenho (HPC).
  - Recomendado para Machine Learning, análise, processamento de vídeo, modelagem financeira, etc.

- **FSx for NetApp ONTAP**
  - Sistema de arquivos *NetApp ONTAP* gerenciado na AWS.

- **FSx for OpenZFS**
  - Sistema de arquivos *OpenZFS* gerenciado na AWS.

## Storage Gateway

Trata-se do sistema híbrido de armazenamento, que estabelece uma conexão segura entre o os ambientes local (on-premise) e a cloud ou vice versa.
  
- Utilizado para backup ou transição de arquivos de on-premise para cloud.
- Pode conectar o ambiente on-premise ao EBS, S3 e FSx.

- Tipos de Gateway:

  - File Gateway 
  - FSx File Gateway
  - Volume Gateway 
  - Backup Gateway 
  
## Transfer Family

Trata-se do serviço que permite a transferência de arquivos para **S3 e EFS** por meio do protocolo FTP.

Suporta os protocolos:

- FTP (File Transfer Protocol (FTP))
- FTPS (File Transfer Protocol over SSL (FTPS))
- SFTP (Secure File Transfer Protocol (SFTP))

## Data Synk

Trata-se do um serviço online que automatiza e acelera a movimentação de dados entre serviços de armazenamento em ambientes on-premises e AWS.

Pode sincronizar para:
- S3 **(qualquer classe de armazenamento, incluindo Glacier)**
- EFS.
- FSx **(Windows, Lustre, NetApp, OpenZFS)**.

- Não é contínuo, as transferenicas podem ser agendadas por hora, por dia, por semana.
- **Única opção de armazenamento que mantém as permissões de arquivos e os metadados**.

## Comparação entre os Recursos de Armazenamento (Storage)

| **Recurso** | **Objetivo** | 
| ---- | ----- | 
| S3 | Armazenamento de objetos |
| S3 Glacier | Arquivamento de objetos |
| EBS | Armazenamento de bloco para uma instância EC2 |
| Instance Store | Armazenamento de bloco **temporário** para uma instância EC2 |
| EFS | Sistema de arquivos em rede (Network File System) |
| FSx for Windows | Sistema de arquivos em rede para servidores Windows |
| FSx for Lustre  | Sistema de arquivos em rede de alta performance para servidores Linux |
| FSx for NetApp ONTAP | Sistema de arquivos compatível com *NetApp ONTAP* | 
| FSx for OpenZFS | Sistema de arquivos compatível com *OpenZFS* | 
| Storage Gateway | Sistema híbrido de arquivos | 
| Transfer Family | Interface FTP, FTPS, SFTP com S3 e EFS | 
| DataSync | Sincronismo de dados agendados do local para a AWS ou da AWS para a AWS | 
| Snowcone / Snowball / Snowmobile | Move uma grande quantidade de dados fisicamente para a AWS | 

## Containers

### ECS (Elastic Container Service)

Serviço de orquestração de contêineres próprio da AWS que permite executar, gerenciar e dimensionar aplicações em contêineres utilizando clusters com instâncias EC2 ou Fargate *(Serveless)*.

- Iniciar contêineres do Docker na AWS é o mesmo que iniciar tasks (Tarefas) nos clusters ECS.

- **Instâncias EC2**
  - O usuário é responsável por provisionar e gerenciar a infraestrutura das instâcias EC2.
  - Cada instância EC2 deve executar o *ECS Agent* para se registrar no Cluster ECS.

- **Fargate (Serveless)**
  - O usuário não provisiona instâncias EC2, somente as Task Definitions.
  - A AWS executa as Tasks com base na demanda por CPU e RAM.
  - Para escalar, basta aumentar o número de Tasks, sem necessidade de aumentar instâncias EC2.

### EKS (Elastic Kubernetes Service)

### ECR (Elastic Container Registry)

- As imagens Docker são armazenadas em repositórios.

  - **Docker Hub (https://hub.docker.com)**
    - Repositório público.

  - **ECR**
    - Repositório privado.
    - Repositório público (ECR Public Gallery https://gallery.ecr.aws)

### App Runner

## Network

### ENI (Elastic Network Interface)




