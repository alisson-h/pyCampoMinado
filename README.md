# Campo Minado (versão simples em Python)

Projeto: jogo Campo Minado implementado em Python.  
Ponto de entrada: `main.py`.

## O que é Campo Minado?
Campo Minado é um jogo de lógica onde você abre casas em um tabuleiro tentando evitar bombas.  
- Cada célula pode conter uma bomba ou um número.  
- O número indica quantas bombas há nas 8 casas adjacentes.  
- O objetivo é marcar corretamente todas as bombas com bandeiras ou abrir todas as casas sem bombas.

## Como funciona esta versão
- O usuário escolhe número de linhas e colunas (entre 2 e 50).
- O usuário escolhe a dificuldade (Fácil, Médio, Difícil). Isso determina a porcentagem de bombas.
- Bombas são posicionadas aleatoriamente. (O primeiro clique tenta garantir que não seja uma bomba.)
- Existem dois modos de ação: abrir uma casa ou marcar/desmarcar uma bandeira.
- Interface em terminal com cores ANSI (se o terminal suportar).

## Como rodar
1. Abra o terminal/cmd na pasta do projeto (onde está `main.py`).
2. Execute:
   - Windows / macOS / Linux:
        python main.py
   - (Se necessário) python3 main.py
3. Requisitos: Python 3.8+ (não há dependências externas).

## Como jogar (comandos)
Ao iniciar, o jogo mostra o tabuleiro e espera comandos. Exemplos e comandos disponíveis:

- Modos de jogo:
  - `!mode abrir` ou `!a` → muda para o modo "abrir".
  - `!mode marcar` ou `!m` → muda para o modo "marcar".
- Comandos gerais:
  - `!help` → mostra ajuda e explicação dos comandos.
  - `!ver` → exibe o tabuleiro atual.
  - `!bandeiras` → mostra quantas bandeiras restam.
  - `!leave` → sai do jogo.
- Para abrir/marcar uma posição:
  - Digite a posição no formato `<linha><coluna>` (ex.: `a0`, `j10`, `A5`).
  - A primeira letra indica a linha (a, b, c, ...). O restante é o número da coluna.
  - Observação: `a10` e `A10` são tratados de forma diferente internamente (o projeto diferencia letras maiúsculas na tabela interna), então prefira letras minúsculas para linhas.

Fluxo típico:
1. Defina o modo (`!a` ou `!m`) ou deixe em branco para usar abrir como padrão.
2. Digite a posição desejada (ex.: `a0`).
3. O jogo atualizará o tabuleiro; marque bandeiras para indicar bombas suspeitas.

## Exemplos

## Conclusão
Esta é uma implementação simples do Campo Minado, pensada para rodar em terminal. É uma boa base para aprender lógica de tabuleiro, recursão (abertura de células vazias) e interação via linha de comando.

## Limitações conhecidas
- Sem interface gráfica (apenas terminal).
- Cores dependem do suporte ANSI do terminal.

Obrigado por testar!
