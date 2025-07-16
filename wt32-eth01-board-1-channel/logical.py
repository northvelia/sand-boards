import urequests
import time

# Configuración genérica (debe ser reemplazada por el usuario)
device_id = "GENERIC_DEVICE_ID"  # Identificador genérico del dispositivo

# Función para activar/desactivar el relé (simulación)
def set_relay(state):
    if state:
        Pin(pin_number, 1) # GPIO utilizado / 1 nivel lógico alto 
        print("Relé activado")  # En un sistema real, controla el pin GPIO
    else:
        Pin(pin_number, 0) # GPIO utilizado / 0 nivel lógico bajo 
        print("Relé desactivado")

# Función para enviar el QR y controlar el relé
def requestPost(qr_code):
    url = "API_ENDPOINT"  # Reemplazar con la URL de la API del cliente
    headers = {"Content-Type": "application/json"}
    payload = {"flairId": device_id, "qrCode": qr_code}

    try:
        response = urequests.post(url, json=payload, headers=headers)
        print("Código de respuesta HTTP:", response.status_code)

        if response.status_code == 200:
            set_relay(True)  # Activar relé
            time.sleep(1)    # Mantener abierto 1 segundo
            set_relay(False) # Desactivar relé

        response.close()
        return response.status_code == 200

    except Exception as e:
        print("Error en la solicitud:", e)
        return False

# Ejemplo de uso
if __name__ == "__main__":
    # Simular lectura de un QR
    qr_data = "123456"  # Ejemplo de código QR
    if len(qr_data) >= 6:
        requestPost(qr_data)
