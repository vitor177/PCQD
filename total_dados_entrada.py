from datetime import datetime, timedelta

def total_dados_entrada(arquivo):
    es = arquivo.split('/')[1].split('-')[0]
    nome_arquivo = arquivo.split('/')[1].split('.')[0]
    ano = int(arquivo.split('/')[1].split('-')[1])
    mes_n = int(arquivo.split('/')[1].split('-')[2].split('.')[0])


    # Obter o dia juliano referente
    data_inicio = datetime(ano, mes_n, 1)
    dia_juliano_ref = data_inicio.timetuple().tm_yday

    # Obter o último dia do mês
    if mes_n == 12:
        dia_final = 31
    else:
        dia_final = (datetime(ano, mes_n + 1, 1) - timedelta(days=1)).day

    mes_nomes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    mes = mes_nomes[mes_n - 1] 

    estacoes = {
        'RNES00': {
            'dfolder': '',
            'latitude': -5.8246,
            'longitude': -35.2258,
            'altitude': 1,
            'temp_min': 10.0,
            'temp_max': 40.7,
            'press_min': 915.7,
            'press_max': 1115.7,
            'prec_max': {
                '1': 80.7, '2': 99.8, '3': 200.8, '4': 240.5, '5': 221.8,
                '6': 348.8, '7': 254, '8': 118.7, '9': 54, '10': 20.6,
                '11': 22.5, '12': 29
            }
        },
        'RNES01': {
            'dfolder': '',
            'latitude': -5.706841,
            'longitude': -36.232853,
            'altitude': 1,
            'temp_min': 10.7,
            'temp_max': 43.1,
            'press_min': 914.6,
            'press_max': 1114.6,
            'prec_max': {
                '1': 82.6, '2': 102.6, '3': 171.5, '4': 169.8, '5': 81.7,
                '6': 38.7, '7': 21.8, '8': 9.3, '9': 1.7, '10': 5,
                '11': 4.6, '12': 24.1
            }
        },
        'RNES02': {
            'dfolder': '',
            'latitude': -5.296237,
            'longitude': -36.272845,
            'altitude': 1,
            'temp_min': 11.3,
            'temp_max': 43.2,
            'press_min': 914.6,
            'press_max': 1114.6,
            'prec_max': {
                '1': 82.6, '2': 102.6, '3': 171.5, '4': 169.8, '5': 81.7,
                '6': 38.7, '7': 21.8, '8': 9.3, '9': 1.7, '10': 5,
                '11': 4.6, '12': 24.1
            }
        },
        'RNES03': {
            'dfolder': '',
            'latitude': -6.144001,
            'longitude': -38.190438,
            'altitude': 1,
            'temp_min': 11.5,
            'temp_max': 46.1,
            'press_min': 918.7,
            'press_max': 1118.7,
            'prec_max': {
                '1': 99.3, '2': 117, '3': 172.3, '4': 212.7, '5': 102.6,
                '6': 49.4, '7': 31.2, '8': 22.2, '9': 2.1, '10': 0.9,
                '11': 3.2, '12': 16.7
            }
        },
        'RNES04': {
            'dfolder': '',
            'latitude': -6.228709,
            'longitude': -36.027581,
            'altitude': 1,
            'temp_min': 10.5,
            'temp_max': 42.2,
            'press_min': 914.6,
            'press_max': 1114.6,
            'prec_max': {
                '1': 82.6, '2': 102.6, '3': 171.5, '4': 169.8, '5': 81.7,
                '6': 38.7, '7': 21.8, '8': 9.3, '9': 1.7, '10': 5,
                '11': 4.6, '12': 24.1
            }
        },
        'RNES06': {
            'dfolder': '',
            'latitude': -5.176129,
            'longitude': -37.343413,
            'altitude': 1,
            'temp_min': 11.6,
            'temp_max': 44.6,
            'press_min': 914.80,
            'press_max': 1114.80,
            'prec_max': {
                '1': 69.3, '2': 130.1, '3': 169.2, '4': 179.6, '5': 109.5,
                '6': 49.4, '7': 39.9, '8': 11.1, '9': 5.9, '10': 3.4,
                '11': 3.2, '12': 17.3
            }
        },
        'SPES01': {
            'dfolder': '',
            'latitude': -21.9592,
            'longitude': -47.4531,
            'altitude': 1,
            'temp_min': 0.1,
            'temp_max': 38.9,
            'press_min': 920.9,
            'press_max': 1120.9,
            'prec_max': {
                '1': 303.8, '2': 221.1, '3': 186.7, '4': 85.4, '5': 66.8,
                '6': 32.1, '7': 30.6, '8': 34.4, '9': 67.1, '10': 120.6,
                '11': 155.1, '12': 254.6
            }
        },
        'PBES01': {
            'dfolder': '',
            'latitude': -6.8372,
            'longitude': -38.2934,
            'altitude': 1,
            'temp_min': 11.3,
            'temp_max': 45.4,
            'press_min': 914.2,
            'press_max': 1114.2,
            'prec_max': {
                '1': 107.3, '2': 221, '3': 237, '4': 216.3, '5': 87.4,
                '6': 36.2, '7': 23.1, '8': 4, '9': 7.5, '10': 14.7,
                '11': 13.7, '12': 37.2
            }
        },
        'APES02': {
            'dfolder': '',
            'latitude': 0.69729,
            'longitude': -51.38915,
            'altitude': 1,
            'temp_min': 12.3,
            'temp_max': 44.4,
            'press_min': 912.3,
            'press_max': 1112.3,
            'prec_max': {
                '1': 235.4, '2': 208.4, '3': 315.3, '4': 296.6, '5': 295.8,
                '6': 201, '7': 173.7, '8': 132.7, '9': 82.2, '10': 72.9,
                '11': 86, '12': 122.1
            }
        }
    }

    if es in estacoes:
        latitude = estacoes[es]['latitude']
        longitude = estacoes[es]['longitude']
        altitude = estacoes[es]['altitude']
        temp_min = estacoes[es]['temp_min']
        temp_max = estacoes[es]['temp_max']
        prec_max = estacoes[es]['prec_max'].get(str(mes_n))
        press_min = estacoes[es]['press_min']
        press_max = estacoes[es]['press_max']
        dfolder = estacoes[es]['dfolder']

    return es, nome_arquivo, ano, mes, dia_juliano_ref, dia_final, latitude, longitude, altitude, temp_min, temp_max, prec_max, press_min, press_max, dfolder
