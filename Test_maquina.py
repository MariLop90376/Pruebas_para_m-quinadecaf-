import unittest
from MaquinadeCafe import MaquinadeCafe

class TestMaquinaCafe(unittest.TestCase):
  
  def setUp(self):
    self.maquina = MaquinadeCafe()

  def test_preparar_bebida(self):
    receta = self.maquina.obtener_receta("Americano", 8 )
    agua_inicial = self.maquina._tanque_de_agua

    resultado = self.maquina_preparar_bebida(receta)

    self.assertEqual(resultado["Code"], 1)
    self.assertLess(self.maquina._tanque_de_agua, agua_inicial)

  def test_verificar_reservas_fail(self):
    self.maquina._tanque_de_agua = 0
    receta = {"agua_ml": 100}

    resultado = self.maquina.verificar_reservas(receta)
    self.assertEqual(resultado["Code"], 0)

  def test_mantenimiento(self):
    self.maquina.mantenimiento(agua=5000, leche=2000, cafe=3000, chocolate=1000)

    self.assertEqual(self.maquina._tanque_de_agua, 5000)
    self.assertEqual(self.maquina._recipiente_de_leche,2000)

  def test_obtener_receta_invalida(self):
    receta = self.maquina.obtener_receta("Te", 8)
    self.assertIn("error",receta)

if __name__ == "__main__":
unittest.main()
