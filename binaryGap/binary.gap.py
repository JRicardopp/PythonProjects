
def binary_gap(decimal):
    if decimal <= 0:
        return "0"
    
    binario = ""

    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2) 
        binario = str(residuo) + binario
        
    return binario
  
        
def max_zeros(binario):
    maxm = -1
    cnt = 0
   
    while(binario):
        
        if(not(binario & 1)):
            cnt += 1
            binario >>= 1
            maxm = max(maxm,cnt)
        else:
            maxm = max(maxm,cnt)
            cnt = 0
            binario >>= 1
   
    return maxm


if __name__ == '__main__':
	decimal = int(input('Escribe un entero: ')) 
	binario = binary_gap(decimal) 
	print(f'El numero {decimal} en binario es {binario}')       
	binario = int(binario)
	repre_binary = max_zeros(binario)
	print(f'La representacion binaria de {binario} es {repre_binary}')
