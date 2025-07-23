# %%
count = 4

while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)
    count += 1
    
# %%
num = 4

while num <= 100:
    resto = num % 4
    if resto == 0:
        print(num)
    num += 1

# %%
i = 0
soma = 0
while i < 4:
    altura = input('Digite a altura')
    altura = int(altura)
    soma = soma + altura
    i += 1
print(soma)
# %%
