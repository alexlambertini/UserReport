cep_destino = input ("Qual seu cep? " )
peso = input ("Peso ")
x = input ("Comprimento ")
y = input ("Largura ")
z = input ("Altura ")

def calculaFreteW21(codigo, peso, x, y, z, cep_destino):
    import http.client as httplib
    import urllib
    import re
    from xml.dom.minidom import parse, parseString

    #codifica os parametros para serem inclusos na url
    params = urllib.urlencode({'cod': codigo,
    'cep': cep_destino,
    'peso': peso,
    'comprimento': x,
    'largura': y,
    'altura': z,
    'servico':'3'})

    #inicia a conexao com o servidor e envia os dados via GET
    conn = httplib.HTTPConnection("frete.w21studio.com")
    conn.request("GET", "/calFrete.xml?"+params)

    #obtem a resposta do servidor
    response = conn.getresponse()

    #transforma a resposta (pagina XML) em DOM
    dom = parseString( response.read() )
    conn.close()

    #recupera os dados necessarios da folha xml
    values = {'status':'', 'valor_sedex':'', 'valor_pac':''}
    for key in values.keys():
        try:
            values[key] = dom.getElementsByTagName(key)[0].childNodes[0].nodeValue
        except:
            pass

    if values['status'] != 'OK':
        raise Exception( values['status'] )

    return {'pac': values['valor_pac'], 'sedex': values['valor_sedex']}

 

 
