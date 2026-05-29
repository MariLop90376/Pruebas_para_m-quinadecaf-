from MaquinadeCafe import MaquinadeCafe
from time import perf_counter_ns

mc = MaquinadeCafe("Maquina de Cafe", 1.0)

print("\n--- PERFILADO DE PREPARACION MOKACCINO) ---")

mc.encender_máquina()
receta = mc.obtener_receta("Mokaccino", 16)
inicio = perf_counter_ns()

resultado = mc.preparar_bebida(receta)
fin = perf_counter_ns()
tiempo = (fin - inicio) / 1_000_000_000

print("Resultado:", resultado)
print(f"Tiempo de preparación: {tiempo:.8f} segundos")
                   
