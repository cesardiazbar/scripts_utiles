import os
import subprocess

def close_cold_turkey():
    # Terminar el proceso de Cold Turkey Blocker
    try:
        # Usa taskkill para cerrar la aplicación y el icono de la bandeja
        subprocess.run(["taskkill", "/f", "/im", "ColdTurkey.exe"], check=True)
        subprocess.run(["taskkill", "/f", "/im", "ColdTurkeyTray.exe"], check=True)
        print("Cold Turkey Blocker and tray icon closed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to close Cold Turkey Blocker. It might not be running.")
        