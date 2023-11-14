import unittest
from unittest.mock import patch

class MyClassTeste(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(2+2,4)

    def test_some_function(self):
        # Substituir a dependência externa com um mock
        with patch("some_module.some_function") as mock_function:
            mock_function.return_value = "foo"

            # Executar a função que depende da dependência externa
            result = some_function()

            # Verificar o resultado da função
            self.assertEqual(result, "foo")

if __name__ == "__main__":
    unittest.main()

#Esquema para teste já config, só replicar para os outros casos ;)

#Faz o resto das coisas!!!

#Falta o mock