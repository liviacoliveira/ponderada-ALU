# ALU de 8 bits

## Sobre o Projeto

A ALU (Arithmetic Logic Unit) é um dos componentes centrais da unidade central de processamento (CPU) de um computador, responsável por executar operações matemáticas e lógicas. 

Esta implementação específica de 8 bits conta com:
- **Registrador AC (Acumulador):** Registrador primário de operações e saídas.
- **Registrador MQ (Multiplier/Quotient):** Utilizado para lidar com a parte mais significativa (MSB) em multiplicações e armazenar o quociente em divisões.
- **Seletor de Operações:** Circuito integrado principal responsável por chavear qual operação deverá ser executada com base em um conjunto de sinais de controle.

### Operações Suportadas

A ALU foi projetada para suportar e executar as seguintes operações com operandos de 8 bits (sendo **N** a entrada de 8 bits e **AC** o acumulador atual):

| Operação | Lógica Matemática | Saída |
| :--- | :--- | :--- |
| **Soma** | AC + N | AC (8 bits) |
| **Subtração** | AC - N | AC (8 bits) |
| **Multiplicação** | AC * N | AC (8 bits - LSB) e MQ (8 bits - MSB) |
| **Divisão** | AC / N | AC (Resto) e MQ (Quociente) |
| **Shift Lógico** | Shift em AC | AC (8 bits) |
| **NAND Lógico** | AC NAND N | AC (8 bits) |
| **XOR Lógico** | AC XOR N | AC (8 bits) |

### Seletor de Operações (Multiplexador)

Para exibir qual operação será executada na saída, o circuito utiliza um multiplexador controlado por um seletor de 3 bits. A configuração de seleção das operações é dada por:

- `000` (0): **Soma**
- `001` (1): **Subtração**
- `010` (2): **NAND**
- `011` (3): **XOR**
- `100` (4): **Divisão** (Apresenta o Resto no registrador AC e o Quociente no registrador MQ)
- `101` (5): **Shift Lógico** *(Necessita de um bit de controle adicional: `0` para shift à Esquerda e `1` para shift à Direita)*
- `110` (6): **Multiplicação** (Apresenta os 8 bits menos significativos - LSB no AC e os 8 bits mais significativos - MSB no MQ)

## Estrutura dos Arquivos

Os circuitos componentes foram criados de forma unitária nos seguintes arquivos `.dig` e integrados na `ALU.dig`:

- `ALU.dig`: Circuito principal contendo a integração de todas as portas, seletores, multiplexadores e os registradores AC e MQ.
- **Registradores:**
  - `registrador8bits.dig`: Registrador de 8 bits (composto por Flip-Flops D sincronizados por um clock comum), utilizado para armazenar e salvar as informações e estados do AC (Acumulador) e do MQ (Multiplier/Quotient).
- **Operações Aritméticas e Lógicas:**
  - `somador1bit.dig`, `somador8bits.dig`, `somador9bits.dig`: Módulos de soma que abstraem a adição, usados de base para outras operações.
  - `subtrator8bits.dig`: Módulo para a subtração bit-a-bit (utilizando complemento de 2).
  - `mult8bits.dig`: Lógica de multiplicação utilizando soma de produtos parciais em cascata.
  - `divisor8bits.dig` e `divisaointerna.dig`: Circuitos de divisão sequencial. \`divisor8bits.dig\` é o módulo principal que encadeia diversos passos da \`divisaointerna.dig\`.
  - `shift.dig`: Implementação das operações de deslocamento lógico.
  - `NAND8bits.dig` / `XOR8bits.dig`: Implementação das portas lógicas bit a bit aplicadas às barramentos de 8 bits.
  - `inversor.dig`: Porta lógica inversora de suporte a complementos e operações lógicas.

## Como as operações foram feitas

Para atender a cada uma das funcionalidades requeridas da ALU, os componentes foram construídos e abstraídos com a seguinte lógica:

- **Soma:** Realizada através do encadeamento de *Full Adders* (somadores de 1 bit, `somador1bit.dig`) dentro de um módulo de 8 bits (`somador8bits.dig`), repassando o *carry-out* de cada bit para o *carry-in* do próximo.
- **Subtração:** Implementada no `subtrator8bits.dig` utilizando a álgebra do Complemento de 2. O módulo utiliza cópias do `inversor.dig` para inverter os bits do operando e, em seguida, reaproveita o `somador8bits.dig` com o *carry-in* do LSB igual a `1`.
- **Multiplicação:** O circuito `mult8bits.dig` gera os 8 produtos parciais a partir de portas AND. Para processar a soma desses produtos sem perder informações de carry, ele instancia 7 módulos de `somador9bits.dig` em cascata, resultando ao fim em 16 bits (8 LSB para o AC e 8 MSB para o MQ).
- **Divisão:** O módulo principal `divisor8bits.dig` encadeia 8 instâncias do bloco `divisaointerna.dig` de forma combinacional. Cada `divisaointerna.dig` executa um "passo" da divisão, utilizando o `subtrator8bits.dig` para verificar se o divisor cabe no valor atual (resto parcial), construindo o Quociente e o Resto iterativamente.
- **Shift Lógico (Deslocamento):** Arquitetado combinando portas lógicas e Multiplexadores (`shift.dig`). De acordo com o bit seletor direcional, o valor de cada bit avança ou recua uma casa posicional, preenchendo as casas faltantes com `0`.
- **NAND e XOR Lógicos:** Implementação direta *bit a bit* (bitwise). Por meio de chaves e barramentos de 8 vias, cada um dos bits do acumulador (AC) possui uma porta equivalente que é processada junto com o bit respectivo da variável de entrada `N`.

## Vídeo explicativo

`https://youtu.be/7b4gUEznvLU`