import unittest
from tb_tareas import Tb_Tareas



class TestTbTareas(unittest.TestCase):
    def setUp(self):
        self.tb_tareas = Tb_Tareas()

    def tearDown(self):
        self.tb_tareas.close()

    def test_alta_tarea(self):
        tarea_id = self.tb_tareas.alta_tarea("Test Tarea")
        self.assertIsNotNone(tarea_id)

    def test_obtener_tareas(self):
        tareas = self.tb_tareas.obtener_tareas()
        self.assertIsInstance(tareas, list)

    def test_borrar_tarea(self):
        tarea_id = self.tb_tareas.alta_tarea("Test Tarea")
        self.tb_tareas.borrar_tarea(tarea_id)
        tareas = self.tb_tareas.obtener_tareas()
        self.assertNotIn(tarea_id, [tarea['id'] for tarea in tareas])

    def test_actualizar_tarea(self):
        tarea_id = self.tb_tareas.alta_tarea("Test Tarea")
        self.tb_tareas.actualizar_tarea(tarea_id, "Updated Tarea")
        tareas = self.tb_tareas.obtener_tareas()
        updated_tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
        self.assertIsNotNone(updated_tarea)
        self.assertEqual(updated_tarea['nombre'], "Updated Tarea")



if __name__ == '__main__':
    unittest.main()