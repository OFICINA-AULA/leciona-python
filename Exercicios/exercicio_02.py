
def mesExtensoV1(data: str):
    dia,mes,ano = data.split('/')  
    
    match mes:
        case '01':
            mes = 'Janeiro'
        case '02':
            mes = 'Fevereiro'
        case '03':
            mes = 'Março'
        case '04':
            mes = 'Abril'
        case '05':
            mes = 'Maio'
        case '06':
            mes = 'Junho'
        case '07':
            mes = 'Julho'
        case '08':
            mes = 'Agosto'
        case '09':
            mes = 'Setembro'
        case '10':
            mes = 'Outubro'
        case '11':
            mes = 'Novembro'
        case '12':
            mes = 'Dezembro'
    
    return dia,mes,ano
            

def mesExtensoV2(data: str):
    dia,mes,ano = data.split('/')
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    chaves =1,2,3,4,5,6,7,8,9,10,11,12   
     
    dicMeses = {chaves[i]:meses[i] for i in range(len(meses))}  
    mes = dicMeses[int(mes)]
    return dia,mes,ano
    
        
if __name__ == '__main__':
    dia,mes,ano = mesExtensoV1('23/11/2024')
    dia,mes,ano = mesExtensoV2('23/02/2024')
    print(f'{dia} de {mes} de {ano}')