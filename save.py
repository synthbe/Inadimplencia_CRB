import pandas as pd

planilha_geral = pd.read_excel("../planilhas/principal.xlsx")

planilha_atrasados = pd.read_excel("../planilhas/inadimplentes.xlsx")

# chrome_driver_path = "../drive/chromedriver_win32.zip/chromedriver" #Windows

chrome_driver_path = "../drive/chromedriver_linux64.zip/chromedriver"

#Local de armazenar os cookies, importante para não ter que ficar logando o tempo todo no zap web:

chrome_save_path = r'user-data-dir=C:\\Users\\public\\AppData\\Local\\Google\\Chrome\\User Data\\save_cash' #Windows
