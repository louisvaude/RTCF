"""
RTCF · Pétales — Launcher
Embarque rtcf_fleurs.html dans l'exe et l'ouvre depuis un chemin fixe
pour que les données localStorage persistent entre les sessions.
"""
import os, sys, webbrowser, shutil

def main():
    # Chemin fixe : les données localStorage restent intactes à chaque ouverture
    app_dir  = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'RTCF_Petales')
    html_dst = os.path.join(app_dir, 'index.html')

    # Source HTML : dossier temp de PyInstaller (exe) ou dossier script
    if getattr(sys, 'frozen', False):
        src = os.path.join(sys._MEIPASS, 'rtcf_fleurs.html')
    else:
        src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rtcf_fleurs.html')

    # Copie / mise à jour du fichier HTML
    os.makedirs(app_dir, exist_ok=True)
    shutil.copy2(src, html_dst)

    # Ouverture dans le navigateur par défaut
    webbrowser.open('file:///' + html_dst.replace('\\', '/'))

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, f'Erreur au lancement :\n{exc}',
                                              'RTCF · Pétales', 0x10)
        except Exception:
            print('Erreur :', exc)
