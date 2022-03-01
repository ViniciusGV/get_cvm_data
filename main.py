from datetime import datetime
from urllib import response
from dateutil.relativedelta import relativedelta
import os
from requests import get
import pandas as pd
from matplotlib import pyplot as plt


def check_if_path_exists_and_create_if_not(path='downloads'):
    """
    Check if path exists.
    """
    if os.path.exists(path):
        print('Já existe')
    else:
        os.mkdir(path)
        print('Criado')

def download_file(url, file_name, path='downloads', type='csv'):
    response = get(url)
    with(open(path + '/' + file_name + '.' + type, 'wb')) as file:
        file.write(response.content)


start_date = datetime.now()

base_url = 'http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/'

base_name = 'inf_diario_fi_'

target_date = datetime.now() - relativedelta(months=1)
target_date_year_month = target_date.strftime('%Y%m')
file_name = base_name + target_date_year_month

url = base_url + file_name + '.csv'

check_if_path_exists_and_create_if_not()
download_file(url, file_name)

print(datetime.now() - start_date)
df = pd.read_csv(f'downloads/'+file_name + '.csv', sep=';', decimal='.')
df = df.loc[df['CNPJ_FUNDO'] == '00.017.024/0001-53']

plt.plot(df['DT_COMPTC'], df['VL_QUOTA'])
plt.show()
