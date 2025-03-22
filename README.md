# 🖥️ Lista Completa de Expected Conditions (EC) no Selenium

O Selenium oferece diversas condições para esperar elementos na página antes de interagir com eles. Essas condições são usadas com WebDriverWait para garantir que os elementos estejam prontos antes de executar ações como clique ou envio de texto.

## 🔹**1. Condições relacionadas à presença de elementos**

### 📌 **EC.presence_of_element_located(`locator`)**

- Espera até que um único elemento esteja presente no `DOM`.

- ⚠️ O elemento pode não estar visível ainda!

```bash
wait.until(EC.presence_of_element_located((By.ID, "meu-elemento")))
```

### 📌**EC.presence_of_all_elements_located(`locator`)**

- Espera até que todos os elementos do seletor estejam no `DOM`.

```bash
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "item-lista")))
```

## 🔹 **2. Condições relacionadas à visibilidade**

### 📌 **EC.visibility_of(`element`)**

- Espera até que um elemento específico esteja visível.

```bash
elemento = driver.find_element(By.ID, "botao")
wait.until(EC.visibility_of(elemento)).click()
```

### 📌 **EC.visibility_of_element_located(`locator`)**

- Igual ao anterior, mas recebe um `locator` em vez de um elemento.

```bash
wait.until(EC.visibility_of_element_located((By.NAME, "campo-texto"))).send_keys("Teste")
```

### 📌 **EC.visibility_of_all_elements_located(`locator`)**

- Espera até que todos os elementos do seletor fiquem visíveis.

```bash
elementos = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "tr")))
```

## 🔹 **3. Condições relacionadas à interatividade**

### 📌 **EC.element_to_be_clickable(`locator`)**

- Espera até que o elemento esteja visível e habilitado para clique.

```bash
botao = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continuar")))
botao.click()
```

### 📌 **EC.element_to_be_selected(`element`)**

- Espera até que um elemento (como um `checkbox`) esteja marcado (`selected`).

```bash
checkbox = driver.find_element(By.ID, "meu-checkbox")
wait.until(EC.element_to_be_selected(checkbox))
```

### 📌 **EC.element_located_to_be_selected(`locator`)**

- Igual ao anterior, mas recebe um locator.

```bash
wait.until(EC.element_located_to_be_selected((By.XPATH, "//input[@type='checkbox']")))
```

### 📌 **EC.element_selection_state_to_be(`locator, estado`)**

- Espera até que o estado de seleção (`True` ou `False`) seja atingido.

```bash
wait.until(EC.element_selection_state_to_be((By.CSS_SELECTOR, ".check"), True))
```

## 🔹 **4. Condições relacionadas à invisibilidade**

### 📌 **EC.invisibility_of_element(`element`)**

- Espera até que um elemento específico desapareça.

```bash
wait.until(EC.invisibility_of_element(driver.find_element(By.ID, "carregando")))
```

### 📌 **EC.invisibility_of_element_located(`locator`)**

- Igual ao anterior, mas recebe um locator.

```bash
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-spinner")))
```

## 🔹 **5. Condições relacionadas a textos e atributos**

### 📌 **EC.text_to_be_present_in_element(`locator, texto`)**

- Espera até que um determinado texto apareça em um elemento.

```bash
wait.until(EC.text_to_be_present_in_element((By.ID, "mensagem"), "Sucesso"))
```

### 📌 **EC.text_to_be_present_in_element_value(`locator, texto`)**

- Espera até que o texto esteja no valor do input.

```bash
wait.until(EC.text_to_be_present_in_element_value((By.NAME, "campo"), "Preenchido"))
```

### 📌 **EC.attribute_to_be(`locator, atributo, valor`)**

- Espera até que um atributo específico tenha um valor desejado.

```bash
wait.until(EC.attribute_to_be((By.ID, "botao"), "disabled", "true"))
```

### 📌 **EC.attribute_contains(`locator, atributo, substring`)**

- Espera até que um atributo contenha uma substring específica.

```bash
wait.until(EC.attribute_contains((By.CLASS_NAME, "status"), "class", "ativo"))
```

## 🔹 **6. Condições relacionadas a frames e alertas**

### 📌 **EC.frame_to_be_available_and_switch_to_it(`locator`)**

- Espera até que um `<iframe>` esteja disponível e troca para ele.

```bash
wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))
```
### 📌 **EC.alert_is_present()**

- Espera até que um alerta (`alert`) esteja presente.

```bash
alerta = wait.until(EC.alert_is_present())
alerta.accept()
```

## 🔹 **7. Condições personalizadas**

### 📌 **EC.staleness_of(`element`)**

- Espera até que um elemento fique obsoleto no DOM (exemplo: uma página recarregando).

```bash
elemento = driver.find_element(By.ID, "popup")
wait.until(EC.staleness_of(elemento))
```

### 📌 **EC.new_window_is_opened(`janela_atual`)**

- Espera até que uma nova aba ou janela seja aberta.

```bash
wait.until(EC.new_window_is_opened(driver.window_handles))
```

### 📌 **EC.number_of_windows_to_be(`num`)**

- Espera até que um determinado número de janelas esteja aberto.

```bash
wait.until(EC.number_of_windows_to_be(2))
```
---

# 🔢 Principais opções do ChromeDriver no Selenium

## 🔹 1. Configuração básica

```bash
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-gpu")  # Desativa aceleração por GPU (relevante no Windows)
options.add_argument("--no-sandbox")  # Necessário para evitar problemas de permissão (Linux)
options.add_argument("--disable-dev-shm-usage")  # Evita uso excessivo de memória compartilhada
options.add_argument("--headless")  # Executa o navegador sem interface gráfica

driver = webdriver.Chrome(options=options)
```
## 🔹 2. Explicação das opções

### ✅ --headless

    Executa o navegador sem interface gráfica (modo invisível).

    Útil para execução em servidores e pipelines de CI/CD.

### ✅ --disable-gpu

    Desativa a aceleração por GPU (relevante para Windows, sem efeito no Linux).

### ✅ --no-sandbox

    Evita erros de permissão, principalmente ao rodar o Selenium como root (necessário no Linux).

### ✅ --disable-dev-shm-usage

    Usa o sistema de arquivos normal ao invés da memória compartilhada /dev/shm(necessário para evitar problemas de memória em contêineres Docker).

## 🔹 3. Outras opções úteis

### ✅ Iniciar o Chrome maximizado:

options.add_argument("--start-maximized")

### ✅ Definir um tamanho específico da janela:

    options.add_argument("window-size=1920,1080")

### ✅ Mudar o user-agent:
```bash
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
```

### ✅ Desativar notificações do Chrome:

```bash
options.add_argument("--disable-notifications")
```

### ✅ Ignorar certificados SSL inválidos:

```bash
options.add_argument("--ignore-certificate-errors")
```

### ✅ Executar em segundo plano (sem mostrar a janela):

```bash
options.add_argument("--remote-debugging-port=9222")
```

## ✅ Conclusão

**As ExpectedConditions do Selenium são fundamentais para garantir que sua automação funcione de forma estável. Escolha a condição mais adequada para cada situação e evite erros de carregamento assíncrono.**
