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
    # Caso o n não está definido, é coletado o número de digitos do maior entre num1 e num2
    if n is None:
        n = max(len(str(num1)), len(str(num2)))

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
    return pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs

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
2. Verificação se n is None
     - Se verdadeiro: pega a quantidade de números do maior número.
     - Se falso: continua para os próximos passos.
3. Verificação da condição n <= 3.
     - Se verdadeiro: retorna num1 * num2 e termina a execução.
     - Se falso: continua para os próximos passos.
3. Cálculo de m = (n + 1) // 2 para determinar o ponto de divisão dos números.
4. Divisão de num1 em partes alta e baixa: p, q = quebrar_num(num1, m).
5. Divisão de num2 em partes alta e baixa: r, s = quebrar_num(num2, m).
6. Chamada recursiva para a parte alta: pr = karatsuba(p, r, m).
7. Chamada recursiva para a parte baixa: qs = karatsuba(q, s, m).
8. Chamada recursiva cruzada: y = karatsuba(p + q, r + s, m + 1).
9. Retorno do resultado final: return pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs.


**II. Estruturando o Grafo de fluxo**
Um grafo de controle representa os caminhos possíveis da execução:
  - Nó: Representa um ponto de decisão ou instrução;
  - Aresta: Representa a transição entre nós.
  - Componentes conexos (𝑃): A função é uma unidade única, então 𝑃 = 1 (é um bloco único de código sem chamadas externas a outras funções ou estruturas separadas).
    
  Nós (𝑁):
  1. N1 - Início da função
  2. N2 - Verificação da condição n is none
  3. N3 - N é atribuído com a quantidade de números do maior número
  4. N4 - Verificação da condição if n <= 3
  5. N5 - Retorno pela multiplicação tradicional
  6. N6 - Cálculo de m = (n + 1) // 2
  7. N7 - Divisão de num1 em partes alta e baixa (p, q = quebrar_num(num1, m))
  8. N8 - Divisão de num2 em partes alta e baixa (r, s = quebrar_num(num2, m))
  9. N9 - Chamada recursiva pr = karatsuba(p, r, m)
  10. N10 - Chamada recursiva qs = karatsuba(q, s, m)
  11. N11 - Chamada recursiva y = karatsuba(p+q, r+s, m+1)
  12. N12 - Retorno do resultado (uv = pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs)
  - TOTAL: 12 nós
      
  Arestas (𝐸):
1. N1 → N2 - Início da função, para verificação se n is None
2. N2 → N3 - Caso n is None, atribui valor a n
3. N2 → N4 - Caso n já definido, verifica se n <= 3
4. N3 → N4 - Após atribuir n, verifica se n <= 3

5. N4 → N5 - Caso n <= 3, retorna multiplicação direta
6. N4 → N6 - Caso n > 3, continua com cálculo de m

7. N6 → N7 - Calcula m e vai para quebrar num1
8. N7 → N8 - Após quebrar num1, quebra num2
9. N8 → N9 - após quebrar num2, inicia atribuição de pr

10. N9 → N1 - Retorno da recursão pr para continuar execução
11. N9 → N10 - Chamada recursiva para multiplicação da parte baixa qs

12. N10 → N1 - Retorno da recursão qs para continuar execução
13. N10 → N11 - Chamada recursiva (y = karatsuba(p+q, r+s, m+1))
14. N11 → N1 - Retorno da recursão y para combinar resultados

15. N11 → N12 - Combina resultados e retorna o valor final
  - TOTAL: 15 arestas

**III. Calcular a complexidade ciclomática**
- 𝑀 = 𝐸 − 𝑁 + 2𝑃
- M = 15 - 12 + 2.1
- M = 3 + 2
- M = 5 

**IV. Desenho do grafo de fluxo**


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

