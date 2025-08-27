# Algoritmo de Multiplicação com Karatsuba 
Dado dois inteiros `num1` e `num2`, a tarefa é calcular o produto `num1 × num2` de forma mais eficiente que a multiplicação tradicional.

---

## Descrição do Projeto

O algoritmo **Karatsuba** é um método de **divisão e conquista** que permite multiplicar dois números grandes com menos operações de multiplicação que a abordagem tradicional.

Enquanto a multiplicação tradicional de dois números com **n** possui a complexidade de O(n²), com o algoritmo Karatsuba, a complexidade vai para O(n^log₂3) ≈ O(n^1.585), tornando-se, assim, mais eficiente em números grandes.

---

## Explicação do Código

```python
def karatsuba(num1: int, num2: int, n: int) -> int:
    # Caso o número de dígitos seja pequeno, é realizada a multiplicação direta
    if n <= 3:
        return num1 * num2

    # Divide os números em duas partes
    m = (n + 1) // 2
    p, q = quebrar_num(num1, m) # quebra os numeros em 2 partes: p= parte alta; q= parte baixa de num1
    r, s = quebrar_num(num2, m) # quebra os numeros em 2 partes: r= parte alta; s= parte baixa de num2

    # Chamadas recursivas
    pr = karatsuba(p, r, m) # multiplicação da parte alta
    qs = karatsuba(q, s, m) # multiplicação da parte baixa
    y  = karatsuba(p + q, r + s, m + 1) # multiplicação cruzada

    # Combinação dos resultados
    uv = pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs
    return uv

def quebrar_num(num: int, m: int) -> tuple[int, int]:
    """
    Divide um número em duas partes:
    - parte alta (num // 10^m)
    - parte baixa (num % 10^m)
    """
    return divmod(num, 10 ** m)
```

### `main` de execução:

```python
if __name__ == "__main__":
    a = 1111111111111111
    b = 2222222222222222
    n = max(len(str(a)), len(str(b))) # pega o número de dígitos do maior entre a e b

    print(karatsuba(a, b, n)) # resultado pelo Karatsuba
    print(a * b) # comparação com multiplicação nativa
```

---

## Como executar o projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/iannovais/fpaa-karatsuba.git
   cd fpaa-karatsuba
   ```

2. Execute o código em Python 3:

   ```bash
   python main.py
   ```

3. O programa exibirá:

   * O resultado da multiplicação via **Karatsuba**
   * O resultado via operador `*` do Python (para validação)

---

## Relatório Técnico

### Complexidade de Ciclomática:

**I. Representação da função em fluxo de controle**
1. Início da função.
2. Verificação da condição n <= 3.
     - Se verdadeiro: retorna num1 * num2 e termina a execução.
     - Se falso: continua para os próximos passos.
3. Cálculo de m = (n + 1) // 2 para determinar o ponto de divisão dos números.
4. Divisão de num1 em partes alta e baixa: p, q = quebrar_num(num1, m).
5. Divisão de num2 em partes alta e baixa: r, s = quebrar_num(num2, m).
6. Chamada recursiva para a parte alta: pr = karatsuba(p, r, m).
7. Chamada recursiva para a parte baixa: qs = karatsuba(q, s, m).
8. Chamada recursiva cruzada: y = karatsuba(p + q, r + s, m + 1).
9. Combinação dos resultados: uv = pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs
10. Retorno do resultado final: return uv.


**II. Estruturando o Grafo de fluxo**
Um grafo de controle representa os caminhos possíveis da execução:
  - Nó: Representa um ponto de decisão ou instrução;
  - Aresta: Representa a transição entre nós.
  - Componentes conexos (𝑃): A função é uma unidade única, então 𝑃 = 1 (é um bloco único de código sem chamadas externas a outras funções ou estruturas separadas).
    
  Nós (𝑁):
  1. N1 - Início da função
  2. N2 - Verificação da condição if n <= 3.
  3. N3 - Retorno pela multiplicação tradicional
  4. N4 - Cálculo de m = (n + 1) // 2
  5. N5 - Divisão de num1 em partes alta e baixa (p, q = quebrar_num(num1, m))
  6. N6 - Divisão de num2 em partes alta e baixa (r, s = quebrar_num(num2, m))
  7. N7 - Chamada recursiva pr = karatsuba(p, r, m)
  8. N8 - Chamada recursiva qs = karatsuba(q, s, m)
  9. N9 - Chamada recursiva y = karatsuba(p+q, r+s, m+1)
  10. N10 - Combinação dos resultados (uv = pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs)
  11. N11 - Retorno do resultado uv
  - TOTAL: 11 nós
      
  Arestas (𝐸):
  1. N1 -> N2 - Início da função para verificação do if n <= 3: 1 aresta
  2. N2 -> N3 - Caso n <= 3: retorna multiplicação tradicional: 1 aresta
  3. N2 -> N4 - Caso n > 3: continua com divisão do número: 1 aresta
  4. N4 -> N5 - Cálculo de m para dividir num1 em partes alta e baixa: 1 aresta
  5. N5 -> N6 - Divisão de num2 em partes alta e baixa: 1 aresta
  6. N6 -> N7 - Chamada recursiva para parte alta (pr): 1 aresta
  7. N7 -> N1 - Retorno da recursão pr para continuar execução: 1 aresta
  8. N7 -> N8 - Continuação com recursão da parte baixa (qs): 1 aresta
  9. N8 -> N1 - Retorno da recursão qs para continuar execução: 1 aresta
  10. N8 -> N9 - Continuação com recursão cruzada (y): 1 aresta
  11. N9 -> N1 - Retorno da recursão y para continuar execução: 1 aresta
  12. N9 -> N10 - Combinação dos resultados pr, qs, y: 1 aresta
  13. N10 -> N11 - Retorno do resultado final uv: 1 aresta
  - TOTAL: 13 arestas

**III. Calcular a complexidade ciclomática**
- 𝑀 = 𝐸 − 𝑁 + 2𝑃
- M = 13 - 11 + 2.1
- M = 2 + 2
- M = 4 

**IV. Desenho do grafo de fluxo**
<img width="1400" height="469" alt="Diagrama em branco" src="https://github.com/user-attachments/assets/31254dda-a7c0-4c35-acc1-6f585f72c273" />

### Complexidade de assintótica:

#### Complexidade de temporal

- Melhor caso: O(1), ocorre quando os números possuem 3 dígitos ou menos, permitindo multiplicação direta.
- Caso médio: O(n^log₂3), ocorre para números grandes, refletindo a recursão típica do algoritmo.
- Pior caso: O(n^log₂3), ocorre para números grandes, quando todas as chamadas recursivas são executadas até o nível máximo.

#### Complexidade de espacial
- O(n^log₂3)

---

## Referência

[O algoritmo de Karatsuba para multiplicação de números](https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/karatsuba.html)

