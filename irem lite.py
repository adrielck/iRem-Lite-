import subprocess
import tkinter as tk
from tkinter import messagebox, scrolledtext

def executar_comando(cmd):
    try:
        resultado = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        if resultado.returncode != 0:
            return f"[ERRO] {resultado.stderr.strip()}"
        return resultado.stdout.strip()
    except FileNotFoundError:
        return "[ERRO] Comando não encontrado. Verifique se libimobiledevice está instalado."
    except subprocess.TimeoutExpired:
        return "[ERRO] Tempo esgotado para o comando."

def info_dispositivo():
    saida = executar_comando(["ideviceinfo"])
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, saida)

def listar_apps():
    saida = executar_comando(["ideviceinstaller", "-l"])
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, saida)

def montar_afc():
    import os
    if not os.path.exists("mnt_ios"):
        os.mkdir("mnt_ios")
    saida = executar_comando(["ifuse", "mnt_ios"])
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, saida)
    if "Permission denied" not in saida and "ERRO" not in saida:
        messagebox.showinfo("Montagem AFC", "✅ Pasta 'mnt_ios' montada com sucesso.")
    else:
        messagebox.showerror("Erro", "Falha ao montar 'mnt_ios'. Verifique permissões e confiança no dispositivo.")

def desmontar_afc():
    saida = executar_comando(["fusermount", "-u", "mnt_ios"])
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, saida)
    messagebox.showinfo("Desmontagem AFC", "📁 Pasta 'mnt_ios' desmontada.")

def mostrar_logs():
    saida = executar_comando(["idevicesyslog", "-d", "-k", "error", "-k", "warn"])
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, saida)

def simular_remover_icloud():
    resposta = messagebox.askyesno("Remover iCloud (Simulação)",
                                  "Esta função é apenas uma simulação para fins educacionais.\n"
                                  "Remoção real de iCloud não é implementada.\n\nDeseja continuar?")
    if resposta:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END,
            "[Simulação] Remoção de conta iCloud NÃO executada.\n"
            "Ferramentas reais são complexas e ilegais sem autorização.\n"
            "Este programa é só para estudo e diagnóstico.")

# --- GUI ---

root = tk.Tk()
root.title("iRemoval Pro Lite - Estudo e Diagnóstico")
root.geometry("780x520")

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

btn_info = tk.Button(frame_botoes, text="📱 Info do Dispositivo", command=info_dispositivo, width=20)
btn_info.grid(row=0, column=0, padx=5)

btn_listar_apps = tk.Button(frame_botoes, text="📦 Listar Apps", command=listar_apps, width=20)
btn_listar_apps.grid(row=0, column=1, padx=5)

btn_montar = tk.Button(frame_botoes, text="📂 Montar AFC", command=montar_afc, width=20)
btn_montar.grid(row=1, column=0, padx=5, pady=5)

btn_desmontar = tk.Button(frame_botoes, text="📤 Desmontar AFC", command=desmontar_afc, width=20)
btn_desmontar.grid(row=1, column=1, padx=5, pady=5)

btn_logs = tk.Button(frame_botoes, text="📋 Mostrar Logs (warn & error)", command=mostrar_logs, width=43)
btn_logs.grid(row=2, column=0, columnspan=2, pady=5)

btn_remover_icloud = tk.Button(frame_botoes, text="🔒 Remover iCloud (Simulação)", command=simular_remover_icloud, width=43)
btn_remover_icloud.grid(row=3, column=0, columnspan=2, pady=10)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=22)
output_text.pack(pady=10)

root.mainloop()
