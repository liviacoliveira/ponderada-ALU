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

## Como foi feito e Estrutura dos Arquivos

Os circuitos componentes foram criados de forma unitária nos seguintes arquivos `.dig` e integrados na `ALU.dig`:

- `ALU.dig`: Circuito principal contendo a integração de todas as portas, seletores, multiplexadores e os registradores AC e MQ.
- **Operações Aritméticas e Lógicas:**
  - `somador1bit.dig`, `somador8bits.dig`, `somador9bits.dig`: Módulos de soma que abstraem a adição, usados de base para outras operações.
  - `subtrator8bits.dig`: Módulo para a subtração bit-a-bit (utilizando complemento de 2).
  - `mult8bits.dig`: Lógica de multiplicação sequencial e combinacional.
  - `visor8bits.dig` / `divisaointerna.dig`: Algoritmo e lógica estrutural de divisão, definindo os restos e quocientes.
  - `shift.dig`: Implementação das operações de deslocamento lógico.
  - `NAND8bits.dig` / `XOR8bits.dig`: Implementação das portas lógicas bit a bit aplicadas às barramentos de 8 bits.
  - `inversor.dig`: Porta lógica inversora de suporte a complementos e operações lógicas.


## Vídeo explicativo

No vídeo abaixo, detalho os conceitos por trás do projeto e demonstro o funcionamento prático da ALU que foi construída e suas operações!

*Ou caso queira apenas deixar o link do YouTube, cole aqui: `https://youtube.com/watch?v=LINK_DO_SEU_VIDEO_AQUI`*