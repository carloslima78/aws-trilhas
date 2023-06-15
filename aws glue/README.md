# AWS Glue

Trata-se de um serviço *serveless* para **ETL (Extract, Transform, Load)**, baseado no **Apache Spark**, totalmente gerenciado que é oferecido de forma nativa pela AWS.

A estrutura do AWS Glue é composta por:

- Data Catalog.
- Database.
- Table.
- Partitions.
- Crawler.

## Data Catalog

Trata-se de um serviço centralizado para os metadados armazenados em diversos outros serviços da AWS tais como S3, RDS, etc. Permite a descoberta organização e acesso simplificado aos dados armazenados de forma que facilite a análise e processamento dos dados.

O Glue Data Catalog possui escopo regional e os controles de identidade e acesso são realizados via políticas do IAM.

### Metadados

São descritivos dos dados que detalham seu conteúdo, estrutura e características que colaboram na descoberta, organização e entendimento e processamento dos dados.

Seguem alguns exemplos de metadados logo abaixo:

- **Nome da tabela**: Indica o nome de uma tabela de banco de dados.
- **Schema da tabela**: Descreve a estrutura de uma tabela como nomes e tipos de colunas, chaves, primárias e estrangeiras, etc.
- **Partições**: Indicam como os dados são particionados como região, data, categoria, etc.
- **Localiação dos dados**: Local físico onde os dados estão armazenados como prefixo do Bucket S3, tabela do banco de dados, etc.
- **Formato dos dados**: Especifica o formato dos dados como CSV, JSON, Parquet, Avro, etc.

### Database

Trata-se de um banco de dados utilizado para organizar logicamente as tabelas de metadados no AWS Glue. Ao definir uma tabela (Table) no Glue Data Catalog, a mesma deve ser adicionada a um Glue Database.

O Glue Database pode conter tabelas que definem dados de muitos armazenamentos diferentes como por exemplo, buckets S3 e tabelas relacionais do RDS.

Vale observar que os dados continuam residindo em suas fontes originais, e o AWS Glue não move os dados dessas fontes, apenas os organiza nas tabelas do Glue Database de forma lógica.

Quando um Glue Database é excluído do Glue Data Catalog, todas as tabelas presentes também serão excluidas.

Fonte: (https://docs.aws.amazon.com/glue/latest/dg/define-database.html)

### Table

Representam 

### Partitions

Representam o mapeamento lógico das entidades que estarão presentes nas tabelas. As pastas em buckets S3 é onde os dados são armazenados de forma física, as entidades são mapeadas em partições de forma lógica.  

## Crawler

Trata-se de uma aplicação criada pela AWS que se conecta a uma fonte de dados (Ex. bucket S3, banco de dados RDS, etc.), extrai o schema das tabelas e insere na estrutura do Data Catalog, de forma que não seja necessária uma inclusão manual desses schemas.

Vale observar que é possível incluir os schemas manualmente criando as tabela, colunas e tipos de dados por meio do AWS Console.

- Criando Crawlers com Terraform: (https://geeks.wego.com/creating-glue-crawlers-via-terraform/)

## Connection

Permite 

## Jobs

## Triggers

Inicia um Job ETL, e podem ser definidas baseadas em tarefas agendadas ou por eventos.

## Mão na Massa

- Criar um Bucket S3.

  - Criar uma pasta para armazenar scripts.
  - Criar uma pasta para armazenar logs.
  - Criar uma pasta para os arquivos contendo os dados de origem (formato CSV).
  - Criar uma pasta para os arquivos contendo os dados transformados (formato Parquet).
  - Criar uma pasta para os arquivos contendo os dados transformados (formato JSON).

- Criar uma função IAM e anexar uma política *(AdministratorAccess)* concedendo acesso total ao AWS Glue. Com essa politica, o AWS Glue realizará ações por você para execução de ações em outros recursos da AWS.

- Criar um Database no Glue.

- Criar os Crawlers necessários para extrais os metadados e criar as tabelas do Glue, possiblitando a visualização dos dados com o AWS Athena.

- Criar os Jobs

