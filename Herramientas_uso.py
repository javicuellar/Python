#   Para uso en PC añadir
import sys, os

# Añadimos path a librerías python, para añadir librerías mías de Herramientas
sys.path.append(os.path.join(os.path.dirname(__file__), '\Python'))
#   Fin uso en PC

from Herramientas.variables import Variables
from Herramientas.mail import email_alert