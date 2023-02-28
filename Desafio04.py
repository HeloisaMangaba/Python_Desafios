## Heloísa M Coletti
# DESAFIO 04 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçõe possiveis sobre ele.

leia = input('Digite algo: ')

print(f'O tipo primitivo de {leia} é', type(leia))
print('Só tem espaço?', leia.isspace())
print('É um número?', leia.isnumeric())
print('É alfabético?', leia.isalpha())
print('É alfanumérico?', leia.isalnum())
print('Está em maiúsculas?', leia.isupper())
print('Esta em minúsculas?', leia.islower())
print('Está capitalizada?', leia.istitle())
