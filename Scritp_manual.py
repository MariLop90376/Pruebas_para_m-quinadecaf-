from MaquinadeCafe import MaquinadeCafe

mc = MaquinadeCafe("MaquinadeCafe",1.0)

print("-\n--- Caso 1 ---")
mc.encender_máquina()

agua_inicial = mc._tanque_de_agua

receta = mc.obtener_receta("Americano", 12)
resultado = mc.preparar_bebida(receta)
print("resultado")

if resultado["Code"] == and mc._tanque_de_agua < agua_inicial:
  print("Caso 1 OK")
else:
  print("Error")

print("-\n---- Caso 6 ---")
mc._encendido = False
receta = mc.obtener_receta("Americano", 8)
resultado = mc.preparar_bebida(receta)

if mc._encendido == False:
  print("Caso 6 OK")
else:
  print("Error")
  
