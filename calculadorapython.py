#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Calculadora em Python
print("\n****************CALCULADORA EM PYTHON***********************")

print("Selecione uma das Operaçôes")
print("1- Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")

operacao = input("Digite sua operação: ")
primeiNum = int(input("Digite o primeiro número: "))
segundoNum = int(input("Digite o segundo número: "))

if operacao == '1':
    resultado = primeiNum + segundoNum
    print('%s + %r = %x' %(primeiNum, segundoNum, resultado))
elif operacao == '2':
    resultado = primeiNum - segundoNum
    print('%s - %r = %x' %(primeiNum, segundoNum, resultado))
elif operacao == '3':
    resultado = primeiNum * segundoNum
    print('%s * %r = %x' %(primeiNum, segundoNum, resultado))
elif operacao == '4':
    resultado = primeiNum / segundoNum
    print('%s / %r = %x' %(primeiNum, segundoNum, resultado))
else:
    print("Digite uma operação válida!")

