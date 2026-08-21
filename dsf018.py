from math import sin, cos, tan, radians
print('====== DESAFIO 18 ======')
angulo = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}.\nO ângulo de {} tem o COSSENO de {:.2f}.\nO ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, sin(radians(angulo)), angulo, cos(radians(angulo)), angulo, tan(radians(angulo))))
