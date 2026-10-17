import os
import webview

def get_storage_path():
    # Définit et crée le dossier local dédié au stockage du profil et des cookies
    base_dir = os.path.dirname(os.path.abspath(__file__))
    profile_dir = os.path.join(base_dir, "gemini_profile")
    os.makedirs(profile_dir, exist_ok=True)
    return profile_dir

def main():
    # Initialise la fenêtre webview et applique l'icône au démarrage
    base_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(base_dir, "assets", "icon.ico")

    webview.create_window(
        title="Tochiro",
        url="https://gemini.google.com",
        width=1280,
        height=720,
        resizable=True
    )

    webview.start(
        icon=icon_path,
        private_mode=False,
        storage_path=get_storage_path()
    )

if __name__ == "__main__":
    main()