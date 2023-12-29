from qiskit import QuantumCircuit, Aer, execute
import numpy as np

# Define a função exponencial
def f(x, N, a):
    return pow(a, x) % N

# Define a função para encontrar o período
def find_period(a, N):
    # Cria um circuito quântico com N qubits para encontrar o período
    circuit = QuantumCircuit(N+1, N)

    # Aplica o gate H em todos os qubits de entrada
    for i in range(N):
        circuit.h(i)

    # Aplica a função exponencial controlada pelo qubit N
    for i in range(N):
        circuit.append(f(i, N, a), [i] + [N])

    # Aplica a transformada de Fourier quântica
    for i in range(N):
        for j in range(i):
            circuit.cu1(2*np.pi/(2**(i-j)), j, i)
        circuit.h(i)

    # Mede os qubits de entrada para obter o período
    for i in range(N):
        circuit.measure(i, i)

    # Executa o circuito na simulação local do Qiskit
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, backend=simulator, shots=1).result()
    measured_period = int(result.get_counts(circuit).most_frequent(), 2)

    return measured_period

# Define a função para encontrar os fatores primos
def find_factors(N):
    # Escolhe um número aleatório menor que N
    a = np.random.randint(2, N)

    # Encontra o período
    r = find_period(a, N)

    # Calcula os possíveis fatores primos
    factor1 = np.gcd(pow(a, r//2) - 1, N)
    factor2 = np.gcd(pow(a, r//2) + 1, N)

    return factor1, factor2

# Testa a função para fatorar o número 15
# factors = find_factors(15)
# print(factors)
