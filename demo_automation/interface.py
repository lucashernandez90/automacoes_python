import config
import threading
import customtkinter
from functions import sign_up_function, inicialize_button

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automatização do Site Demo Automation")
        self.geometry("300x300")
        self.grid_columnconfigure((0, 1), weight=1)

        #Botao para inicializar
        self.init_button = customtkinter.CTkButton(self, text="Inicializar", command=self.run_inicialize)
        self.init_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        #Botao para Login
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.run_sign_up)
        self.login_button.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        #Label para mostrar o resultado
        self.result_label = customtkinter.CTkLabel(self, text="")
        self.result_label.grid(row=1, column=0, columnspan=2, pady=10)

    def run_inicialize(self):
        self.result_label.configure(text="Inicialização realizada")
        inicialize_button()

    def run_sign_up(self):
        self.result_label.configure(text="Login realizado")
        sign_up_function()

app = App()
app.mainloop()
