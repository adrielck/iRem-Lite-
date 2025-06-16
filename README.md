# iRemoval Pro Lite - Diagnóstico e Estudo de iDevices

Uma ferramenta gráfica (GUI) simples feita em Python, com o objetivo de facilitar o diagnóstico e interação com dispositivos iOS (iPhone, iPad, etc). Foi desenvolvida para fins **educacionais e de estudo**, com foco em auxiliar no uso de comandos da suíte `libimobiledevice`.

---

## 📌 Funcionalidades

- 📱 Exibir informações básicas do dispositivo iOS (`ideviceinfo`)
- 📦 Listar aplicativos instalados (`ideviceinstaller -l`)
- 📂 Montar sistema de arquivos do dispositivo (modo AFC) usando `ifuse`
- 📤 Desmontar o sistema de arquivos (AFC)
- 📋 Exibir logs do sistema iOS com filtros de `warn` e `error` (`idevicesyslog`)
- 🔒 Simular a remoção da conta iCloud (APENAS SIMULAÇÃO)

---

## ⚠️ Aviso Legal

> Esta ferramenta **não realiza qualquer tipo de desbloqueio real**. A função de remoção de iCloud é apenas **simulada** para aprendizado. O uso indevido de ferramentas reais pode ser ilegal. Este projeto é **100% educativo**.

---

## 💻 Tecnologias e Dependências

### Linguagem:
- Python 3.6+

### Bibliotecas Python:
- `tkinter` (interface gráfica)
- `subprocess` (execução de comandos do sistema)
- `tkinter.scrolledtext` (área de log rolável)

### Pacotes externos necessários:
Para o script funcionar corretamente, os seguintes utilitários da suíte `libimobiledevice` devem estar instalados no seu sistema operacional:

- `ideviceinfo`
- `ideviceinstaller`
- `ifuse`
- `fusermount`
- `idevicesyslog`

#### Instalação no Ubuntu/Debian:
```bash
sudo apt update
sudo apt install libimobiledevice-utils ifuse
```

#### No macOS (via brew):
```bash
brew install libimobiledevice ifuse
```

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado (preferencialmente 3.6 ou superior).
2. Instale os pacotes do sistema conforme explicado acima.
3. Conecte o dispositivo iOS via USB.
4. Execute o script:

```bash
python3 teste.py
```

---

## 🧠 Como Funciona

Cada botão na interface chama uma função que executa comandos CLI (via `subprocess`) e exibe os resultados na interface com o `ScrolledText`. A estrutura do script segue uma lógica limpa e funcional, ideal para iniciantes em automação de tarefas com dispositivos iOS.

---

## 📁 Estrutura

```
iRemoval-Pro-Lite/
│
├── teste.py           # Código-fonte principal
├── README.md          # Este arquivo
```

---

## 📚 Objetivo Educacional

Este projeto visa:

- Demonstrar como usar `libimobiledevice` em Python
- Explorar conceitos de GUI com `tkinter`
- Simular tarefas comuns em diagnóstico de iDevices
- Reforçar o uso de subprocessos em automações

---

## 👨‍💻 Autor

Desenvolvido por: **Adriel Cardoso Araújo**  
Email: [adrielaraujook@gmail.com](mailto:adrielaraujook@gmail.com)  
LinkedIn: [linkedin.com/in/adrielcardosoaraujo](https://linkedin.com/in/adrielcardosoaraujo)

---

## 🛑 Licença

Este projeto é distribuído para fins de estudo e uso pessoal.  
Não é permitido o uso comercial ou distribuição para fins ilegais.