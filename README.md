# Reinicialização Automática do Dispositivo MX

Este é um projeto de automação para reinicialização automática de um dispositivo MX da Cisco Meraki todos os dias às 07:00.

## Pré-requisitos

- Python 3.x instalado
- Biblioteca `meraki` instalada (use o comando `pip install meraki` para instalar)
- Chave de API do Cisco Meraki

## Configuração

1. Clone este repositório para o seu ambiente local.

2. Substitua `'SUA_CHAVE_DE_API'` pela sua própria chave de API do Cisco Meraki no arquivo `api.py`.

3. Substitua `'SEU_NUMERO_DE_SERIE'` pelo número de série correto do dispositivo MX no arquivo `api.py`.

## Uso

1. Abra o terminal ou prompt de comando e navegue até o diretório do projeto.

2. Execute o seguinte comando para iniciar o programa:

   ```shell
   python api.py


Aprimorado por Ryan Pacheco

________________________________________________________________________________________________
Reinicialização Automática do Dispositivo MX
A "Reinicialização Automática do Dispositivo MX" é um programa em Python que automatiza o processo de reinicialização de um dispositivo Cisco Meraki MX. Ele permite agendar a reinicialização do dispositivo automaticamente em um horário específico todos os dias.

Como Funciona
O programa utiliza a API do Cisco Meraki Dashboard para interagir com o dispositivo. Ele utiliza a biblioteca meraki, que fornece uma interface conveniente para se comunicar com a API do Meraki Dashboard.

Ao ser executado, o programa inicializa a sessão da API do Meraki usando sua chave de API. Em seguida, ele agenda a reinicialização do dispositivo MX utilizando a biblioteca schedule. Você pode configurar o horário agendado modificando o código.

Uma vez agendada, o programa é executado continuamente, verificando se é hora de reiniciar o dispositivo. Quando o horário agendado é alcançado, o programa envia um comando de reinicialização para o dispositivo MX através da API do Meraki.

O programa garante que o dispositivo seja reiniciado automaticamente todos os dias no horário especificado, sem intervenção manual.

Pré-requisitos
Para utilizar este programa, você precisará dos seguintes itens:

Python 3.x instalado no seu sistema
A biblioteca meraki instalada (utilize pip install meraki para instalá-la)
Uma chave de API do Cisco Meraki com as permissões adequadas
O número de série do dispositivo MX que você deseja reiniciar
Configuração
Antes de executar o programa, você precisa configurá-lo com seus detalhes específicos. Abra o arquivo api.py e substitua os valores de exemplo pelos seus próprios valores de chave de API e número de série do dispositivo MX.

Uso
Para utilizar o programa, siga os seguintes passos:

Abra um terminal ou prompt de comando.

Navegue até o diretório onde o arquivo api.py está localizado.

Execute o seguinte comando:

Copy code
python api.py
O programa será iniciado e verificará continuamente se é hora de reiniciar o dispositivo MX. Ele iniciará automaticamente o processo de reinicialização no horário especificado a cada dia.

Contribuição
Contribuições para este projeto são bem-vindas! Se você deseja contribuir, sinta-se à vontade para enviar uma solicitação de pull com suas alterações propostas.

Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

Por favor, observe que esta é uma descrição geral do programa. Certifique-se de personalizá-lo ainda mais para incluir quaisquer detalhes adicionais ou requisitos específicos da sua implementação ou ambiente.
