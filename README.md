## Implementação do processador de 8bits (com modificações) apresentado em _Step-by-step design and simulation of a simple CPU architecture_ [1]

_Trabalho desenvolvido para a disciplina de **Arquitetura e Organização de Computadores** sob orientação do [Profº M.Sc. Bruno Farias](https://github.com/bruno-carvalho)_.

Equipe: [@allexlima](https://github.com/allexlima), [@pauloigormoraes](https://github.com/pauloigormoraes), [@renanbarroncas](https://github.com/renanbarroncas)

### Especificações

1. Endereçamento de 5bits;
2. Registradores de 8bits;
3. Memória de 32x24-bits para armazenamento de instruções;
4. Operações disponíveis (na ULA):
    a) A,
    b) B,
    c) A+1,
    d) B + 1,
    e) A+B,
    f) A-B,
    g) A AND B, e
    h) A OR B
5. **[Extra]** Instruções de 24bits (No projeto original, o autor utiliza 16bits);
6. **[Extra]** Tradutor em _Python_: possibilita a escrita de instruções em Assembly em um formato inspirado no MIPS-Assembly para que possam ser convertidas para sequencias em hexadecimal (formato que Logisim exige para armazenar as instruções na memória ROM/RAM que o mesmo disponibiliza); e
7. **[Extra]** Introdução de novas instruções.

### Organização dos componentes
    
1. ALU (Unidade Lógica e Aritmética)
    a) Arquitetura
    ![alt tag](https://raw.githubusercontent.com/allexlima/SimpleProcessor8Bits/master/Photos/ula.png)
    b) Chip
    ![alt tag](https://raw.githubusercontent.com/allexlima/SimpleProcessor8Bits/master/Photos/1.png)

2. Datapath (Caminho de dados)
    a) Arquitetura
    ![alt tag](https://raw.githubusercontent.com/allexlima/SimpleProcessor8Bits/master/Photos/datapath.png)
    b) Chip
    ![alt tag](https://raw.githubusercontent.com/allexlima/SimpleProcessor8Bits/master/Photos/2.png)

3. Unidade de Controle
    a) Arquitetura
    ![alt tag](https://raw.githubusercontent.com/allexlima/SimpleProcessor8Bits/master/Photos/control_unit.png)
    b) Chip
    ![alt tag](https://raw.githubusercontent.com/allexlima/SimpleProcessor8Bits/master/Photos/3.png)

4. Visão principal/final
    ![alt tag](https://raw.githubusercontent.com/allexlima/SimpleProcessor8Bits/master/Photos/main.png)

### Requisitos para a simulação

1. [Logisim](http://www.cburch.com/logisim/)
2. [Python 2.7.x](https://www.python.org/)

### Inicialização

1. Clone este repositório
  ```
  $ git clone https://github.com/allexlima/SimpleProcessor8Bits
  $ cd SimpleProcessor8Bits/
  ```

1. Abra o arquivo ```Processor.circ``` com o Logisim.

#### Criando programinhas em "Assembly"

Como informado, nós desenvolvemos uma espécie de tradudor que converte as instruções do nosso processador (que são escritas em um formato inspirado no MIPS-Assembly) para o formato hexadecimal, para poder ser lido pelo Logisim.

##### Quais instruções estão disponíveis?

![alt tag](https://raw.githubusercontent.com/allexlima/SimpleProcessor8Bits/master/Photos/4.jpeg)

Todos os arquivos em assembly (```.asm```) devem ficar na pasta ```./Assembly/```, enquanto que os no formato hexadecimal (```.hex```), os que são gerados pelo tradutor, são criados diretamente na pasta ```./Test/```

##### Utilizando o tradutor (exemplos)

Na pasta ```./Assembly/``` já existem dois exemplos ```soma.asm``` e ```fibonacci.asm```.

1. Abra o arquivo ```soma.asm```, que deve estar como código abaixo:
    ```
    input .a, 6
    inc .a
    print .a
    inc .a
    print .a
    input .b, 4
    add .a, .b
    print .a
    ```
2. Observe que as parcelas da soma encontram-se nas linhas 1 e 6. Altere como queira.
3. Feche o arquivo e abra o terminal.
4. Informe o nome do arquivo a ser "traduzido" para hexadecimal, nesse caso ```soma.asm```, para o programa ```translator.py```:
    ```
    $ python translator.py soma.asm
    ```
5. O programa irá converter e salvar a saída com o mesmo nome (porém extensão diferente) na pasta ```./Test/```
6. Com o projeto ```Processor.circ``` aberto no Logisim, carregue o arquivo ```.hex```de saída do tradutor na memória RAM e em seguida inicie o _clock_.
7. O resultado será exibido nos displays do processador. 


### Mais detalhes

Na pasta ```./Docs/``` desse repositório, você pode encontrar os slides que utilizamos nas apresentações do projeto (```Apresentação 01 - Resumo do projeto.pdf``` é um resumo geral do trabalho original enquanto que ```Apresentação 02 - Trabalho final.pdf``` são itens referentes ao nosso projeto). Além dos slides, há também a tabela ```ISA.ods``` que contém alguns detalhes técnicos importantes.

Você também pode encontrar mais conteúdos legais sobre o tema nas referências [2] e [3].

Dúvidas? Sugestões? Bugs? Entre em contato conosco :)


### Referências
1. Schuurman, D. C. (2013, March). Step-by-step design and simulation of a simple CPU architecture. In Proceeding of the 44th ACM technical symposium on Computer science education (pp. 335-340). ACM. Available in http://dl.acm.org/citation.cfm?id=2445296&dl=ACM&coll=DL&CFID=795199471&CFTOKEN=65361630
2. TANENBAUM, A. S.Organização e estruturada de computadores. São Paulo: PearsonPrentice Hall, 2013. ISBN 9788581435398.
3. MONTEIRO, M. A.Introdução à Organização de Computadores. 5. ed. Rio de Janeiro:LTC, 2007. ISBN 9788521615439.