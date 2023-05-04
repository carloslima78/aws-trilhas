# AWS - Solutions Architect Associate

Esta trilha tem o propósito de fornecer pílulas de conhecimento para direcionamento para gatilhos de estudos mais aprofundados referente a certificação **Solutions Architect Associate**.

A certificação **Solutions Architect Associate** está posicionada entre a certificação **AWS Practitioner** e a **Solutions Architect Professional**.

<br>

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

<br>

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

<br>

## Billing

### Alerta de Billing

Trata-se de alertas para monitoramento e notificação (por e-mail) de consumo de recursos que podem ser por:

- Custo (Valor monetário).
- Utilização.
- Planos de Economia.

<br>

## Infraestrutura Global

### Regions (Regiões)

- São locais físicos distribuídos pelo mundo onde localizam-se os Datacenters da AWS.

### Availability Zones (Zonas de Disponiblidade)

- São Datacenters dentro de uma região AWS com links de conexão entre elas com alta velocidade para manter baixa latência.
- Um o mais Datacenters distintos com energia, rede e conectividade redundantes em uma região.
- São separadas fisicamente por uma distância significativa (até 100 KMs).
- A separação ocorre para que mantenham **backpus** seguros umas das outras e a segurança contra desastres.

### Local Zones (Zonas Local)

- São Datacenters menores que ficam entre as zonas de disponibilidade.
- Possuem conexão direta com as zonas de disponibilidade.
- Seu propósito é a redução de latência entre as zonas de disponbilidade para serviços de stream por exemplo.

### Wavelength

- É uma infraestrutura que a AWS implanta nas provedoras de telecomunicação (Vivo, Claro, etd.), para que se conectem aos serviços da AWS com alta velocidade.
- Otimiza a comunicação entre os serviços disponíveis em celulares e os serviços AWS.
- Melhora jogos, stream, etc.
- Não há encargos pelo uso.

### Outspots

- A AWS leva e implanta serviços e infraestrutura em qualquer Datacenter local.
- O cliente pode aproveitar os serviços AWS em seu próprio Datacenter.
- O cliente será responsável pela segurança, pois a infraestrutura está em seu Datacenter.
- Voltado para clietnes de grande porte que já possuem seus próprios Datacenters, ou não possuem regiões AWS disponíveis.
