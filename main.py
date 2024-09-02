def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def gerar_sequencia(n, seq=None):
    if seq is None:
        seq = [0]
    if seq[-1] < n:
        next_num = fibonacci(len(seq))
        seq.append(next_num)
        return gerar_sequencia(n, seq)
    return seq

def verificar_numero(n):
    fib_seq = gerar_sequencia(n)
    if n in fib_seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."


num = int(input("Digite o número: "))
print(verificar_numero(num))
