# Manipulação de clientes inadimplentes

## Contexto

O pequeno projeto a seguir foi uma demanda da empresa CRB Soluções Financeiras.
Tal empresa faz empréstimos para seus clientes para que os mesmos comprem motos nas lojas Moto Certa e Carbumotos.
A empresa usa o sistema e banco de dados da Intech para ter o controle de todos os financiamentos. 

No entanto, havia um problema na hora de consultar os clientes inadimplentes: A intech fornece dois tipos de relatórios, o do clientes gerais *principal* e do clientes em atraso *inadimplentes*.
Ao ver a primeira, percebia-se que se possuia todos os dados úteis do cliente, enquanto na segunda, apenas a quantidade de parcelas, mas sem informações úteis para entrar em contato com a pessoa.

O que se era feito, era consultar cliente por cliente pelo seu código, ou seja, um trabalho manual bem demorado, principalmente devido a quantidade de clientes inadimplentes.

## Solução:

A solução foi rodar um código em python para poder fazer uma nova planilha de inadimplentes, dessa vez com todos os dados úteis dos clientes inadimplentes

## Recursos

Obviamente, além da linguagem python, se usou algumas bibliotecas:
* Pandas (Para manipulação dos dados)
* Re (Para o regex dos números dos clientes)
* Selenium (Para entrar em contato com o clientes através do whatsapp web)
* Urllib (Para tornar as strings compatíveis com links)
* Time (Para otimizar o uso do webdriver)

Com exceção da Time e da Re, todas são necessárias fazer a instalção para uso. Para instalar, tenha a ferramenta pip instalada no computador e rode no terminal "pip install <nome_da_biblioteca>

## Lógica do código

O código possui uma lógica extremamente simples, ele pega o clinete da *planilh2* e o consulta na *planilha1*.

A consulta é feita com a busca binária, com o Big(o) = lg(n), como o excel permite ordenar os clientes pelo código, essa busca se tornou a melhor opção mesmo. Poderia ter usado apenas o operados *in* do python, no entanto esse operador realiza uma busca linear, com o Big(o) = n. Então, como se teria que fazer n consultas, o tempo para consultar todos os clientes seria n². Com a busca binárias, esse tempo ficará n*lg(n), ou seja, mais otimizado.

Após achar o cliente na planilha principal, adicionar todos os seus dados correspondentes no data_frame, e segue essa lógica até o último.

Entretanto, muitos dos clientes indimplentes estão sem o telefone preenchido, então se adicionou uma condição para verificar isso, caso o telefone esteja preenchido, ele será salvo no data frame, caso não, o código prossegue para o próximo cliente

Após finalizar, com o data frame preenchido, cria-se um arquivo em excel baseado no data frame.

E então se usa o selenium, como a planilha possui o contato dos clientes, ele abre o whatsapp web e através do link http://web.whatsapp.com/send?phone=55ddd_numero&text=mensagem, o qual basta substiuir as variáveis ddd_numero e mensagem por suas repectivas strings.

Como muitos dos números são inválidos, há uma última lógica em remover os clientes com tais números da planilha, sobrando apenas os clientes indimplentes com contatos de acesso via whatsapp

## Arquvios:

Dentro da pasta planilhas, estão as planilhas que serão analisadas, a principal é a planilha com todos os clientes e a que inclui todos os dados de interesse. A inadimplentes é a com os clientes inadimplentes, e que informa apenas so dados do atraso do cliente.

Dentro da pasta drive, estão apenas os webdrives para o funcionamento do Selenium, tanto para windows como para linux

Dentro da pasta src:
* busca_binaria.py
    * Arquivo com a implementação da busca binária
* regex.py
    * Arquivo com a implementação do regex
* filtro.py
    * Arquivo para realizar toda a lógica de filtragem ja explicada
* save.py
    * Arquivo com o caminho de todos os arquivos e diretórios

## Uso

Para usar o algoritmo, navegue até a src e execute os arquivos filtro.py para criar a planilha filtradas, e o arquivo mensagens.py para usar o webdriver

## Observações

* O mensagens.py não está enviando as mensagens para os clientes, apenas abrindo a conversa. Para enviar, basta descomentar a linha 22 do arquivo
* Como as planilhas tinha informações pessoais dos clientes, tive que obviamente modificálas com numeros aleatorios, mas o codigo irá funcionar normalmente com dados reais.
