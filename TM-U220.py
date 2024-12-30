import time
import win32print

# Variables de ejemplo
nombre = "Juan Perez"
placa1 = "ABC123"
placa2 = "XYZ456"
peso1 = "200.5 kg"
peso2 = "150.0 kg"
tara = "50.5 kg"
empresa = "Transportes XYZ"
origen = "Ciudad A"
destino = "Ciudad B"
observaciones = "Cargar y descargar en el mismo sitio."

# Nombre de la impresora
printer_name = "EPSON TM-U220 Receipt"  # Cambia esto al nombre de tu impresora

# Conectar a la impresora
printer = win32print.OpenPrinter(printer_name)
job = win32print.StartDocPrinter(printer, 1, ("Ticket de Carga", None, "RAW"))
win32print.StartPagePrinter(printer)

# Comandos ESC/POS
ticket = b'\x1b\x40'  # Reset de la impresora
ticket += b'\x1b\x61\x01'  # Centrado
ticket += b'                  TICKET DE CARGA                  \n'
ticket += b'\x1b\x61\x00'  # Alineación izquierda
ticket += b'Nombre:       ' + nombre.encode() + b'\n'
ticket += b'Empresa:      ' + empresa.encode() + b'\n'
ticket += b'Origen:       ' + origen.encode() + b'\n'
ticket += b'Destino:      ' + destino.encode() + b'\n'
ticket += b'Placa 1:      ' + placa1.encode() + b'\n'
ticket += b'Placa 2:      ' + placa2.encode() + b'\n'
ticket += b'Peso 1:       ' + peso1.encode() + b'\n'
ticket += b'Peso 2:       ' + peso2.encode() + b'\n'
ticket += b'Tara:         ' + tara.encode() + b'\n'
ticket += b'\nObservaciones:\n' + observaciones.encode() + b'\n'
ticket += b'------------------------------\n'
ticket += b'Gracias por su preferencia.\n'

# Agregar avance de línea para que sobresalga más el papel
ticket += b'\n' * 4  # Avanza 5 líneas

# Agregar avance de papel para asegurar que sobresalga
ticket += b'\x1b\x64\x05'  # Avanza el papel 5 unidades (ajusta este valor si es necesario)

# Enviar datos a la impresora
win32print.WritePrinter(printer, ticket)

# Finalizar el trabajo de impresión
win32print.EndPagePrinter(printer)
win32print.EndDocPrinter(printer)
win32print.ClosePrinter(printer)

# Esperar antes de continuar con el siguiente ticket (si es necesario)
time.sleep(1)
