
num = int(input("Введите число: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f'{i} * {j} = {(i * j):<2}', end=' ')
        
        
        
# Это императивная структурная парадигма, т.к. здесь используется последовательность команд, 
# последовательность четко структурирована, нет оператора goto, используется утверждение и ветвление.