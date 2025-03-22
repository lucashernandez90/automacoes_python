import config
import interface
import functions
from interface import App
from selenium.webdriver.chrome.options import Options
if __name__ == "__main__":

    functions.executar_pesado()

    options = Options()
    #options.add_argument("--headless")  # Executa sem abrir janela
    options.add_argument("--disable-gpu")  # Desativa GPU (melhor para Windows)
    options.add_argument("--no-sandbox")  # Evita problemas de permissão
    options.add_argument("--disable-dev-shm-usage")  # Evita uso excessivo de memória compartilhada

    app = App()
    app.mainloop()

