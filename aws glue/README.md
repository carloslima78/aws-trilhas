# AWS Glue

Trata-se de um serviço *serveless* para **ETL (Extract, Transform, Load)**, baseado no **Apache Spark**, totalmente gerenciado que é oferecido de forma nativa pela AWS.

A estrutrua do AWS Glue é composta por:

- Glue Data Catalog.
- Glue Database.
- Glue Table.
- Partitions.

## AWS Glue Data Catalog

Trata-se de um serviço centralizado para os metadados armazenados em diversos outros serviços da AWS tais como S3, RDS, etc. Permite a descoberta organização e acesso simplificado aos dados armazenados de forma que facilite a análise e processamento dos dados.

O Glue Data Catalog possui escopo regional e será criado um por região além que os controles de identidade e acesso são realizados via políticas do IAM.

### Metadados

São descritivos dos dados que detalham seu conteúdo, estrutura e características que colaboram na descoberta, organização e entendimento e processamento dos dados.

Seguem alguns exemplos de metadados logo abaixo:

- **Nome da tabela**: Indica o nome de uma tabela de banco de dados.
- **Schema da tabela**: Descreve a estrutura de uma tabela como nomes e tipos de colunas, chaves, primárias e estrangeiras, etc.
- **Partições**: Indicam como os dados são particionados como região, data, categoria, etc.
- **Localiação dos dados**: Local físico onde os dados estão armazenados como prefixo do Bucket S3, tabela do banco de dados, etc.
- **Formato dos dados**: Especifica o formato dos dados como CSV, JSON, Parquet, Avro, etc.

## AWS Glue Database

## Mão na Massa

- Criar um Bucket S3.
- Criar uma função IAM e anexar uma política *(AdministratorAccess)* concedendo acesso total ao AWS Glue. Com essa politica, o AWS Glue realizará ações por você para execução de ações em outros recursos da AWS.