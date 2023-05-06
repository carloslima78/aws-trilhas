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
  - Aplicado para os protocolos **TCP**, **TLS (Secure TCP)**, **UDP*** atuando nas camadas 3 e 4 do modelo OSI.
  - É o Load Balance mais rápido e com baixa latência.
  - Toma decisões através dos protocolos TCP e UDP.
  - Focado no tráfego de rede, baseado em roteamento IP.
  - Interessante para jogos onde pecisa lidar com milhões de requisições por segundo.
  - Distribui percentualmente o tráfego de rede.

- **Gateway Load Balancer - (GWLB - 2020)**
  - Atua na camada 3 de rede do modelo OSI para o protocolo IP.
  - Aplicado para segurança, compliance, detecção de intrusão, firewall, etc.

### ALB Target Groups

Trata-se de um grupo de recursos **alvo** que serão balanceados pelo ALB que pode ser composto por:

- Instâncias EC2.
- Tarefas ECS (Tasks).
- Funções Lambda.
- Endereços IP.

Um ALB é capaz de gerenciar o balanceamento de um ou mais target groups além de monitorar a saúde das aplicações alvo presentes no grupo.

## Network

### ENI (Elastic Network Interface)