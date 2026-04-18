import winreg
import sys
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def register_meta_extension():
    if not is_admin():
        print("❌ ERROR: Anda HARUS menjalankan terminal/skrip ini sebagai ADMINISTRATOR.")
        print("💡 Caranya: Klik kanan CMD/PowerShell -> Run as Administrator")
        return
    current_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(current_dir, "meta_icon", "icon.ico")
    interpreter_path = os.path.join(current_dir, "meta_runner.py")
    if not os.path.exists(icon_path):
        print(f"⚠️ Peringatan: File icon tidak ditemukan di: {icon_path}")
    if not os.path.exists(interpreter_path):
        print(f"❌ ERROR: File interpreter tidak ditemukan di: {interpreter_path}")
        return

    try:
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, ".meta") as key:
            winreg.SetValue(key, "", winreg.REG_SZ, "MetaLanguageFile")
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "MetaLanguageFile") as key:
            winreg.SetValue(key, "", winreg.REG_SZ, "Meta Language Script")      
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"MetaLanguageFile\DefaultIcon") as key:
            winreg.SetValue(key, "", winreg.REG_SZ, f'"{icon_path}"')
        command = f'"{sys.executable}" "{interpreter_path}" "%1"'
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"MetaLanguageFile\shell\open\command") as key:
            winreg.SetValue(key, "", winreg.REG_SZ, command)
            
        print("---")
        print("✅ REGISTRASI BERHASIL!")
        print(f"📍 Icon: {icon_path}")
        print(f"📍 Runner: {sys.executable}")
        print("---")
        print("💡 TIPS: Jika icon belum berubah, buka Task Manager, klik kanan 'Windows Explorer', lalu pilih 'Restart'.")

    except Exception as e:
        print(f"❌ Terjadi kesalahan teknis: {e}")

if __name__ == "__main__":
    register_meta_extension()