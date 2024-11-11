import subprocess


# Comando a ejecutar
comando = ['python', 'alerta_MD.py'] 

# Lanzar el subproceso
proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Obtener la salida y errores
salida, errores = proceso.communicate()

print("Código de retorno:", proceso.returncode)