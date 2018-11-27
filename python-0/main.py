def os10MaioresEstadosDoBrasil():

    estados = {
    'Acre' : 164122.2,
    'Alagoas' : 27767.7	,
    'Amapá' : 142814.6,
    'Amazonas' : 1570745.7,
    'Bahia' : 564692.7,
    'Ceará' : 148825.6,
    'Distrito Federal' : 5822.1,
    'Espírito Santo' : 46077.5,
    'Goiás' : 340086.7,
    'Maranhão' : 331983.3,
    'Mato Grosso' : 903357.9,
    'Mato Grosso do Sul' : 357125.0 ,
    'Minas Gerais' : 586528.3,
    'Pará' : 1247689.5,
    'Paraíba' : 56439.8,
    'Paraná' : 199314.9,
    'Pernambuco' : 98311.6,
    'Piauí' : 251529.2,
    'Rio de Janeiro' : 43696.1,
    'Rio Grande do Norte' : 52796.8,
    'Rio Grande do Sul' : 281748.5,
    'Rondônia' : 237576.2,
    'Roraima' : 224299.0,
    'Santa Catarina' : 95346.2,
    'São Paulo' : 248209.4,
    'Sergipe' : 21910.3,
    'Tocantins' : 277620.9
    }

    estados_sort_by_value =  sorted(estados, key=estados.__getitem__, reverse= True)
    #print(estados_sort_by_value[:10])
    return estados_sort_by_value[:10]
    raise NotImplementedError() 

#if __name__ == "__main__":
#   os10MaioresEstadosDoBrasil()