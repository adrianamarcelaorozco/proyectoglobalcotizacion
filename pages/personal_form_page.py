from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Manejo de esperas en Selenium
from selenium.webdriver.support import expected_conditions as EC # Condiciones de espera explícitas
import time
from config import config
from selenium.webdriver.common.action_chains import ActionChains  # Permite realizar interacciones avanzadas

class PersonalFormPage(BasePage):
    def personal_form_mayor(self):
        self.enter_text(By.XPATH, "//input[@data-id='date-picker-slds-input']", '12/28/1984') # Ingresar la fecha en el campo de fecha usando el input de tipo date
        # Haz clic en el combobox
        wait = WebDriverWait(self.driver, 15)
        # Espera hasta que el label "Sexo" esté presente
        label_sexo = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//label[@for="comboboxId-387" and contains(., "Sexo")]')
        ))
        # Scroll al label
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label_sexo)
        time.sleep(1)  # Espera que la animación termine (por si hay transiciones de Salesforce)        
        #Encuentra el input que está cerca del label "Sexo"
        dropdown_input = self.driver.find_element(By.XPATH, '//*[@id="comboboxId-387"]')  
        dropdown_input.click()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)  # Configura la espera explícita para el siguiente paso.
        M_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="Masculino"]]')))  # Espera hasta que la opción "01" sea clickeable.
        M_option.click()  # Hace clic en la opción "01"
        #dropdown_input.send_keys('Masculino')
        time.sleep(1)  # Deja que se rendericen las opciones
        # 4️⃣ Seleccionar opción "Masculino"
        radio = self.wait_for_element(By.XPATH, "//input[@type='radio' and @value='Pareja con hijos menores de edad']")  # Espera hasta que el radio button sea visible.
        self.driver.execute_script("arguments[0].click();", radio)  # Usa Javascript para hacer clic en el radio button.
        dropdown = self.driver.find_element(By.XPATH, '//*[@id="comboboxId-412"]')  # Encuentra el dropdown.
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)  # Desplaza el dropdown a la vista si es necesario.
        dropdown.click()  # Hace clic para desplegar las opciones del dropdown.
        wait = WebDriverWait(self.driver, 10)  # Configura la espera explícita para el siguiente paso.
        one_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="01"]]')))  # Espera hasta que la opción "01" sea clickeable.
        one_option.click()  # Hace clic en la opción "01".
        time.sleep(5)  # Pausa de 2 segundos para garantizar que la acción se complete.
        self.enter_text(By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[5]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-block[1]/div/div/section/fieldset/slot/vlocity_ins-omniscript-text[1]/slot/c-input/div/div[2]/input', config.NOMBRED)  # Ingresa el nombre en el campo correspondiente.
        self.enter_text(By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[5]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-block[1]/div/div/section/fieldset/slot/vlocity_ins-omniscript-text[2]/slot/c-input/div/div[2]/input', config.PAPELLIDOD)  # Ingresa el primer apellido en el campo correspondiente.
        self.enter_text(By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[5]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-block[1]/div/div/section/fieldset/slot/vlocity_ins-omniscript-text[3]/slot/c-input/div/div[2]/input', config.SAPELLIDOD)  # Ingresa el segundo apellido en el campo correspondiente.
        time.sleep(5)
        dropdown_input_h = self.driver.find_element(By.XPATH, '//*[@id="comboboxId-426"]')  
        dropdown_input_h.click()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)  # Configura la espera explícita para el siguiente paso.
        H_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="Hijo/a"]]')))  # Espera hasta que la opción "01" sea clickeable.
        H_option.click()  # Hace clic en la opción "01"
        #dropdown_input.send_keys('Masculino')
        time.sleep(1)  # Deja que se rendericen las opciones
        date_input = self.driver.find_element(By.XPATH, '//*[@id="date-input-430"]')  # Encuentra el campo de fecha.
        date_input.send_keys('01/18/1970')  # Ingresa la fecha manualmente (por ejemplo, 01/18/1970).
        pass

    def boton_guardar(self):
        save_button = self.wait_for_element(By.XPATH, '//button[contains(text(), "Guardar y continuar")]')  # Espera hasta que el botón esté visible.
        self.driver.execute_script("arguments[0].scrollIntoView();", save_button)  # Desplaza el dropdown a la vista si es necesario.
        # Desplaza el botón a la vista si no está visible.
        save_button.click()  # Hace clic en el botón para continuar.
        time.sleep(5)  # Espera 5 segundos para asegurar que la acción se haya completado.
        print("Validación Información Personal")
        pass


    def personal_form_menor(self):
        self.enter_text(By.XPATH, "//input[@data-id='date-picker-slds-input']", '12/28/1992') # Ingresar la fecha en el campo de fecha usando el input de tipo date
        dropdown = self.driver.find_element(By.XPATH, '//*[@id="comboboxId-366"]')  # Encuentra el combobox (desplegable) para seleccionar un valor.
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)  # Desplaza el combobox a la vista.
        dropdown.click()  # Hace clic en el combobox para mostrar las opciones.
        wait = WebDriverWait(self.driver, 10)  # Configura la espera explícita para el siguiente paso.
        option_xpath = f'//div[@role="option" and @data-value="Masculino"]'  # XPath para la opción "Masculino" en el dropdown.
        option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))  # Espera hasta que la opción esté clickeable.
        time.sleep(2)  # Pausa de 2 segundos para garantizar la interacción completa.
        option.click()  # Hace clic en la opción "Masculino".
        radio = self.wait_for_element(By.XPATH, "//input[@type='radio' and @value='Pareja con hijos menores de edad']")  # Espera hasta que el radio button sea visible.
        self.driver.execute_script("arguments[0].click();", radio)  # Usa Javascript para hacer clic en el radio button.
        dropdown = self.driver.find_element(By.XPATH, '//*[@id="comboboxId-391"]')  # Encuentra el dropdown.
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)  # Desplaza el dropdown a la vista si es necesario.
        dropdown.click()  # Hace clic para desplegar las opciones del dropdown.
        wait = WebDriverWait(self.driver, 10)  # Configura la espera explícita para el siguiente paso.
        one_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="01"]]')))  # Espera hasta que la opción "01" sea clickeable.
        one_option.click()  # Hace clic en la opción "01".
        time.sleep(5)  # Pausa de 2 segundos para garantizar que la acción se complete.
        self.enter_text(By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[5]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-block[1]/div/div/section/fieldset/slot/vlocity_ins-omniscript-text[1]/slot/c-input/div/div[2]/input', config.NOMBRED)  # Ingresa el nombre en el campo correspondiente.
        self.enter_text(By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[5]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-block[1]/div/div/section/fieldset/slot/vlocity_ins-omniscript-text[2]/slot/c-input/div/div[2]/input', config.PAPELLIDOD)  # Ingresa el primer apellido en el campo correspondiente.
        self.enter_text(By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[5]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-block[1]/div/div/section/fieldset/slot/vlocity_ins-omniscript-text[3]/slot/c-input/div/div[2]/input', config.SAPELLIDOD)  # Ingresa el segundo apellido en el campo correspondiente.
        time.sleep(5)
        self.select_dropdown_option(
            (By.XPATH, '//*[@id="comboboxId-405"]'),
            (By.XPATH, '//div[@role="option" and .//span[text()="Hijo/a"]]')
        )
        date_input = self.driver.find_element(By.XPATH, '//*[@id="date-input-409"]')  # Encuentra el campo de fecha.
        date_input.send_keys('01/18/2020')  # Ingresa la fecha manualmente (por ejemplo, 01/18/1970).
        date_input.click()  # Hace clic en el campo para completar la interacción.
        date_input.click()  # Hace clic en el campo para completar la interacción.
        time.sleep(10)  # Pausa de 2 segundos para garantizar la interacción completa.
        wait = WebDriverWait(self.driver, 10) # Define una espera explícita de hasta 10 segundos para encontrar un elemento en la página
        # 🔹 XPath del input del combobox
        dropdown_xpath = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[5]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-block[1]/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[2]/slot/c-combobox/div/div/div[2]/div[1]/div/input"
        dropdown_input = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath))) # Espera explícita hasta que el elemento del dropdown sea clickeable    
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_input) # Desplaza la vista para centrar el dropdown en la pantalla  
        dropdown_input.click() # Hace clic en el dropdown para desplegar las opciones     
        self.enter_text(By.XPATH, dropdown_xpath, config.ESCOLARIDAD) # Ingresa el dato de escolaridad en el campo del dropdown (por ejemplo, la ciudad)  
        opcion = WebDriverWait(self.driver, 10).until(  
        # Espera explícita hasta que la opción "Primero" del dropdown sea visible en la lista  
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='Primero']")
            )
        )
        
        ActionChains(self.driver).move_to_element(opcion).perform() # Mueve el cursor del mouse hasta la opción seleccionada para asegurar que sea interactuable      
        opcion.click() # Hace clic en la opción seleccionada dentro del dropdown
        wait = WebDriverWait(self.driver, 5) # Define una nueva espera explícita de 5 segundos para garantizar la carga de la siguiente acción

        # 🔹 XPath del input del combobox
        dropdown_xpaths = "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/c-gsv-formulary-english/div/article/div[2]/vlocity_ins-omniscript-step[5]/div[3]/slot/vlocity_ins-omniscript-block/div/div/section/fieldset/slot/vlocity_ins-omniscript-block[1]/div/div/section/fieldset/slot/vlocity_ins-omniscript-select[3]/slot/c-combobox/div/div/div[2]/div[1]/div/input"      
        dropdown_inputs = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpaths))) # Espera hasta que el campo desplegable (dropdown) esté disponible para hacer clic      
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_inputs) # Desplaza la vista hacia el dropdown para asegurarse de que sea visible en pantalla
        dropdown_inputs.click() # Hace clic en el campo desplegable para mostrar las opciones disponibles       
        self.enter_text(By.XPATH, dropdown_xpaths, config.CALENDARIOE) # Ingresa el valor correspondiente al calendario escolar en el campo del dropdown
        # Espera hasta que la opción "Calendario A (Enero - Diciembre)" sea visible en el desplegable
        opciones = WebDriverWait(self.driver, 10).until(  
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(@class, 'slds-listbox__option-text') and text()='Calendario A (Enero - Diciembre)']")
            )
        )
            # 🔹 Esperar la opción dentro del dropdown y hacer clic en ella
        ActionChains(self.driver).move_to_element(opciones).perform()
        opciones.click()
        pass

    def button_regresar(self):
        boton_anterior = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='button-container']/button[1]"))
        )
        boton_anterior.click()  
        pass
