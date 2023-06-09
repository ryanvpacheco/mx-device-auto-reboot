import meraki
import schedule
import time
import logging

# Configuração do logger
logging.basicConfig(
    filename='meraki_reboot.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Defina a sua chave de API como uma variável de ambiente
# em vez de defini-la diretamente no código
API_KEY = ''

# Crie uma instância do objeto DashboardAPI
dashboard = meraki.DashboardAPI(API_KEY)

# Substitua 'SEU_NUMERO_DE_SERIE' pelo número de série correto do dispositivo
serial = ''

def reboot_device():
    """
    Função para reiniciar o dispositivo MX.
    """
    response = dashboard.devices.rebootDevice(serial)
    logger.info(f'Reinicializando o dispositivo. Resposta: {response}')
    print(f'Reinicializando o dispositivo. Resposta: {response}')
    logger.info('Monitorando o dispositivo...')
    print('Monitorando o dispositivo...')
    monitor_device()

def monitor_device():
    was_offline = False
    while True:
        try:
            device_status = dashboard.devices.getDevice(serial)
            if device_status and "status" in device_status:
                logger.info(f'Status do dispositivo: {device_status["status"]}')
                print(f'Status do dispositivo: {device_status["status"]}')
                if device_status["status"] == 'online':
                    if was_offline:
                        logger.info('O dispositivo está online novamente. Reinicialização feita com sucesso!')
                        print('O dispositivo está online novamente. Reinicialização feita com sucesso!')
                        break  # Interrompe o loop de verificação quando o dispositivo estiver online novamente
                    else:
                        logger.info('O dispositivo está online.')
                        print('O dispositivo está online.')
                else:
                    was_offline = True
                    logger.info('Buscando conexão com o equipamento...')
                    print('Buscando conexão com o equipamento...')
            else:
                logger.info('A resposta da API não contém status do dispositivo.')
                print('A resposta da API não contém status do dispositivo.')
            time.sleep(180)  # Aguarde 200 segundos antes de verificar novamente
        except Exception as e:
            logger.error(f'Erro ao monitorar o dispositivo: {e}')
            print(f'Erro ao monitorar o dispositivo: {e}')
            break  # Interrompe o loop de verificação

# Agende a reinicialização para ocorrer todos os dias às 07:00
schedule.every().day.at('').do(reboot_device)

while True:
    schedule.run_pending()
    time.sleep(1)