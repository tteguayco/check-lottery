import requests
import json

numbers = [
    14530,
    39400,
    27341,
    35491,
    35742,
    45872,
    20943,
    43594,
    19155,
    94025,
    10446,
    11837,
    31457,
    35918,
    36798,
    34689,
    32169
]

endpoint = 'https://api.elpais.com/ws/LoteriaNavidadPremiados'
status_flag = 1

def get_status_msg(code):
    if code == 0:
        return 'El sorteo no ha comenzado todavía.'
    elif code == 1:
        return 'El sorteo se está llevando a cabo.'
    elif code == 2:
        return 'El sorteo ha finalizado recientemente.'
    elif code == 3:
        return 'El sorteo ha finalizado y existe ya un listado oficial en PDF.'
    elif code == 4:
        return 'El sorteo ha terminado y los resultados se basan en la lista oficial.'
    else:
        return 'Sin información sobre el estado del sorteo.'

print('Comprobación de los {} números insertados:'.format(len(numbers)))

for i, number in enumerate(numbers):
    url = endpoint + '?s=' + str(status_flag) + '&n=' + str(number)
    response = requests.get(url).content.decode()
    response = response.replace('busqueda=', '')
    response_json = json.loads(response)
    prize = response_json['premio']
    status_msg_code = response_json['status']
    
    if prize is 'PREMIO_AL_DECIMO':
        prize = 'PREMIADO'

    if (i == 0):
        status_msg = get_status_msg(status_msg_code)
        print('"' + status_msg + '"')

    print('Número ' + str(number) + ': ' + str(prize))