
#TODO: Importaciones de las librerías necesarias
from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam

#* Pulsadores
pulsador1 = pin(15, pin.IN, pin.PULL_UP)
pulsador2 = pin(16, pin.IN, pin.PULL_UP)
pulsador3 = pin(27, pin.IN, pin.PULL_UP)
pulsador4 = pin(14, pin.IN, pin.PULL_UP)
pulsador_mas = pin(12, pin.IN, pin.PULL_UP )
pulsador_menos = pin(13, pin.IN, pin.PULL_UP)

#* Variables tiempo
espera = 100#! ms
paso = 20

#? Forma 1
leda = pin(5,pin.OUT)
ledb = pin(18,pin.OUT)
ledc = pin(19,pin.OUT)
ledd = pin(21,pin.OUT)
lede = pin(22,pin.OUT)
ledf = pin(23,pin.OUT)
ledg = pin(26,pin.OUT)
ledh = pin(25,pin.OUT)
ledi = pin(33,pin.OUT)
ledj = pin(32,pin.OUT)

  #! 1
def secuencia_1():
  leda.value(1)
  pausam(espera)
  leda.value(0)
  pausam(espera)
    
  ledb.value(1)
  pausam(espera)
  ledb.value(0)
  pausam(espera)
    
  ledc.value(1)
  pausam(espera)
  ledc.value(0)
  pausam(espera)
    
  ledd.value(1)
  pausam(espera)
  ledd.value(0)
  pausam(espera)
    
  lede.value(1)
  pausam(espera)
  lede.value(0)
  pausam(espera)
    
  ledf.value(1)
  pausam(espera)
  ledf.value(0)
  pausam(espera)
    
  ledg.value(1)
  pausam(espera)
  ledg.value(0)
  pausam(espera)
    
  ledh.value(1)
  pausam(espera)
  ledh.value(0)
  pausam(espera)
    
  ledi.value(1)
  pausam(espera)
  ledi.value(0)
  pausam(espera)
    
  ledj.value(1)
  pausam(espera)
  ledj.value(0)
  pausam(espera)

  #! 2
def secuencia_2():
  ledj.value(1)
  pausam(espera)
  ledj.value(0)
  pausam(espera)
    
  ledi.value(1)
  pausam(espera)
  ledi.value(0)
  pausam(espera)
    
  ledh.value(1)
  pausam(espera)
  ledh.value(0)
  pausam(espera)
    
  ledg.value(1)
  pausam(espera)
  ledg.value(0)
  pausam(espera)
    
  ledf.value(1)
  pausam(espera)
  ledf.value(0)
  pausam(espera)
    
  lede.value(1)
  pausam(espera)
  lede.value(0)
  pausam(espera)
    
  ledd.value(1)
  pausam(espera)
  ledd.value(0)
  pausam(espera)
    
  ledc.value(1)
  pausam(espera)
  ledc.value(0)
  pausam(espera)
    
  ledb.value(1)
  pausam(espera)
  ledb.value(0)
  pausam(espera)
    
  leda.value(1)
  pausam(espera)
  leda.value(0)
  pausam(espera)

  #! 3
def secuencia_3():
  leda.value(0)
  ledc.value(0)
  lede.value(0)
  ledg.value(0)
  ledi.value(0)
  ledb.value(1)
  ledd.value(1)
  ledf.value(1)
  ledh.value(1)
  ledj.value(1) 
  pausam(espera) 
  leda.value(1)
  ledc.value(1)
  lede.value(1)
  ledg.value(1)
  ledi.value(1)
  ledb.value(0)
  ledd.value(0)
  ledf.value(0)
  ledh.value(0)
  ledj.value(0) 
  pausam(espera) 


#? Forma 2
def print_led(a,b,c,d,e,f,g,h,i,j):
  leda.value(a)
  ledb.value(b)
  ledc.value(c)
  ledd.value(d)
  lede.value(e)
  ledf.value(f)
  ledg.value(g)
  ledh.value(h)
  ledi.value(i)
  ledj.value(j)

  pausam(espera)
  

  #! 4
def secuencia_4():
  print_led(1,1,1,1,1,0,0,0,0,0)
  print_led(0,0,0,0,0,1,1,1,1,1)
  

  #! 5
def secuencia_5():
  print_led(1,1,0,0,0,0,0,0,0,0)
  print_led(0,1,1,0,0,0,0,0,0,0)
  print_led(0,0,1,1,0,0,0,0,0,0)
  print_led(0,0,0,1,1,0,0,0,0,0)
  print_led(0,0,0,0,1,1,0,0,0,0)
  print_led(0,0,0,0,0,1,1,0,0,0)
  print_led(0,0,0,0,0,0,1,1,0,0)
  print_led(0,0,0,0,0,0,0,1,1,0)
  print_led(0,0,0,0,0,0,0,0,1,1)

  #! 6
def secuencia_6():
  print_led(0,0,0,0,0,0,0,0,0,0)
  print_led(1,0,0,0,0,0,0,0,0,0)
  print_led(1,1,0,0,0,0,0,0,0,0)
  print_led(1,1,1,0,0,0,0,0,0,0)
  print_led(1,1,1,1,0,0,0,0,0,0)
  print_led(1,1,1,1,1,0,0,0,0,0)
  print_led(1,1,1,1,1,1,0,0,0,0)
  print_led(1,1,1,1,1,1,1,0,0,0)
  print_led(1,1,1,1,1,1,1,1,0,0)
  print_led(1,1,1,1,1,1,1,1,1,0)
  print_led(1,1,1,1,1,1,1,1,1,1)
  print_led(1,1,1,1,1,1,1,1,1,0)
  print_led(1,1,1,1,1,1,1,1,0,0)
  print_led(1,1,1,1,1,1,1,0,0,0)
  print_led(1,1,1,1,1,1,0,0,0,0)
  print_led(1,1,1,1,1,0,0,0,0,0)
  print_led(1,1,1,1,0,0,0,0,0,0)
  print_led(1,1,1,0,0,0,0,0,0,0)
  print_led(1,1,0,0,0,0,0,0,0,0)
  print_led(1,0,0,0,0,0,0,0,0,0)

  #! 7
def secuencia_7():
  print_led(0,0,0,0,1,1,0,0,0,0)
  print_led(0,0,0,1,0,0,1,0,0,0)
  print_led(0,0,1,0,0,0,0,1,0,0)
  print_led(0,1,0,0,0,0,0,0,1,0)
  print_led(1,0,0,0,0,0,0,0,0,1)


#? Forma 3
todos = [leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi,ledj]
#! 8
def secuencia_8():
  print_led(0,0,0,0,1,1,0,0,0,0)
  print_led(0,0,0,1,0,0,1,0,0,0)
  print_led(0,0,1,0,0,0,0,1,0,0)
  print_led(0,1,0,0,0,0,0,0,1,0)
  print_led(1,0,0,0,0,0,0,0,0,1)

  #! 9
def secuencia_9():
  for elemento in todos:
    elemento.value(1)
    pausam(espera)
    elemento.value(1)
    pausam(espera)

  for elemento in todos:
    elemento.value(0)
    pausam(espera)
    elemento.value(0)
    pausam(espera)

  for elemento in todos:
    elemento.value(1)
    pausam(espera)
    elemento.value(1)
    pausam(espera)

  for elemento in todos:
    elemento.value(0)
    pausam(espera)
    elemento.value(0)
    pausam(espera)

  #! 10
def secuencia_10():
  print_led(1,0,0,0,1,1,0,0,0,1)
  print_led(0,1,0,1,0,0,1,0,1,0)
  print_led(0,0,1,0,0,0,0,1,0,0)
  print_led(0,1,0,1,0,0,1,0,1,0)


#? Forma 4


leds = [leda,ledb,ledc,ledd,lede, ledf, ledg,ledh,ledi,ledj]

  #! 11
def secuencia_11():
    for i in leds:
        for j in range (1):
            i.value(not i.value())
            pausam(espera)
  #! 12
def secuencia_12():
  print_led(1,0,0,0,1,1,0,0,0,1)
  print_led(0,1,0,1,0,0,1,0,1,0)
  print_led(0,0,1,0,0,0,0,1,0,0)
  print_led(0,1,0,1,0,0,1,0,1,0)
  
  #! 13
def secuencia_13():
  print_led(1,0,0,0,1,1,0,0,0,1)
  print_led(0,1,0,1,0,0,1,0,1,0)
  print_led(0,0,1,0,0,0,0,1,0,0)
  print_led(0,1,0,1,0,0,1,0,1,0)



#? Forma 5

pines = [5, 18, 19, 21, 22, 23, 26, 25, 33, 32]
conjunto = []
for i in pines:
    conjunto.append(pin(i, pin.OUT))

print(conjunto)

  #! 14 
def secuencia_14():
    for i in conjunto:
            i.value(not i.value())
    pausam(espera)  
    for i in reversed(conjunto):
            i.value(not i.value())
    pausam(espera)

  #! 15
def secuencia_15():
    for i in reversed(conjunto):
        for j in range(1):
            i.value(not i.value())
        pausam(espera)
    for i in conjunto:
        for j in range(0):
            i.value(not i.value())
        pausam(espera)
  #! 16
def secuencia_16():
    for i in conjunto:
        for j in range(1):
            i.value(not i.value())
        pausam(espera)
    for i in reversed(conjunto):
        for j in range(0):
            i.value(not i.value())
        pausam(espera)


#* Funciones para bajar y subir la velocidad de la secuencia
def mas(esperemos):
    mas_velocidad = espera + paso
    return (mas_velocidad)
def menos(esperemos):
    menos_velocidad = espera - paso
    if menos_velocidad <= 0:
        menos_velocidad = 20
    return (menos_velocidad)

#* Activación por botones
while True:
    
  if pulsador_mas.value()==1 and pulsador_menos.value()==0:
    espera= mas(espera)
  if pulsador_mas.value()==0 and pulsador_menos.value()==1:
    espera= menos(espera) 
    
  if pulsador1.value()==0:
    if pulsador2.value()==0:
      if pulsador3.value()==0:
        if pulsador4.value()==0:
          secuencia_1()

  if pulsador1.value()==1:
    if pulsador2.value()==0:
      if pulsador3.value()==0:
        if pulsador4.value()==0:
          secuencia_2()

  if pulsador1.value()==0:
    if pulsador2.value()==1:
      if pulsador3.value()==0:
        if pulsador4.value()==0:
          secuencia_3()

  if pulsador1.value()==1:
    if pulsador2.value()==1:
      if pulsador3.value()==0:
        if pulsador4.value()==0:
          secuencia_4()

  if pulsador1.value()==0:
    if pulsador2.value()==0:
      if pulsador3.value()==1:
        if pulsador4.value()==0:
          secuencia_5()

  if pulsador1.value()==1:
    if pulsador2.value()==0:
      if pulsador3.value()==1:
        if pulsador4.value()==0:
          secuencia_6()

  if pulsador1.value()==0:
    if pulsador2.value()==1:
      if pulsador3.value()==1:
        if pulsador4.value()==0:
          secuencia_7()

  if pulsador1.value()==1:
    if pulsador2.value()==1:
      if pulsador3.value()==1:
        if pulsador4.value()==0:
          secuencia_8()

  if pulsador1.value()==0:
    if pulsador2.value()==0:
      if pulsador3.value()==0:
        if pulsador4.value()==1:
          secuencia_9()

  if pulsador1.value()==0:
    if pulsador2.value()==1:
      if pulsador3.value()==0:
        if pulsador4.value()==1:
          secuencia_10()
    
  if pulsador1.value()==1:
    if pulsador2.value()==1:
      if pulsador3.value()==0:
        if pulsador4.value()==1:
          secuencia_11()

  if pulsador1.value()==0:
    if pulsador2.value()==0:
      if pulsador3.value()==1:
        if pulsador4.value()==1:
          secuencia_12()

  if pulsador1.value()==1:
    if pulsador2.value()==0:
      if pulsador3.value()==1:
        if pulsador4.value()==1:
          secuencia_13()

  if pulsador1.value()==0:
    if pulsador2.value()==1:
      if pulsador3.value()==1:
        if pulsador4.value()==1:
          secuencia_14()

  if pulsador1.value()==1:
    if pulsador2.value()==0:
      if pulsador3.value()==0:
        if pulsador4.value()==1:
          secuencia_15()

  if pulsador1.value()==1:
    if pulsador2.value()==1:
      if pulsador3.value()==1:
        if pulsador4.value()==1:
          secuencia_16()