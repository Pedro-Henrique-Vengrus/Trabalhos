import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#Variável e função s(t)
t = sp.Symbol('t')
s_t = t**3 - 6*t**2 + 9*t  

#Derivadas 
v_t = sp.diff(s_t, t)  # Velocidade 
a_t = sp.diff(v_t, t)  # Aceleração 

#Converter para funções numéricas
s_func = sp.lambdify(t, s_t, modules=['numpy'])
v_func = sp.lambdify(t, v_t, modules=['numpy'])
a_func = sp.lambdify(t, a_t, modules=['numpy'])

#Intervalo de tempo
tempo = np.linspace(0, 10, 500)
s_vals = s_func(tempo)
v_vals = v_func(tempo)
a_vals = a_func(tempo)

#Tamanho gráfico
plt.figure(figsize=(12, 8))

plt.plot(tempo, s_vals, label='Posição s(t)', linewidth=2)
plt.plot(tempo, v_vals, label='Velocidade v(t)', linestyle='--', linewidth=2)
plt.plot(tempo, a_vals, label='Aceleração a(t)', linestyle='-.', linewidth=2)

plt.title('Trabalho Movimento com derivadas')
plt.xlabel('Tempo (t)')
plt.ylabel('Valores')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.show()
