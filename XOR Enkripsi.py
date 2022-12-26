def generateKey(data, key): 
    key = list(key) 
    if len(data) == len(key): 
        return(key) 
    else: 
        for i in range(len(data) -len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key))

def encryptXOR(data, key):
    encrypt = ""
    for i in data:
        for j in key:
            encrypt += chr(ord(i)^ord(j))
    hasil = ("Chipertext dari",data,"yaitu : ", encrypt)
    return hasil

file_mentah = input('Masukan file yang akan dienkripsi : ')
key = input('Masukan key : ')
hasil_enkripsi = 'enkripsi.txt'
file_data = open(file_mentah, 'r')
data = file_data.read()

if file_data == None:
    print('Berkas tidak ditemukan')
else:
    file_enkripsi = open(hasil_enkripsi,'w+')
    key = generateKey(data,key)
    file_enkripsi.write(str(encryptXOR(data, key)))

    file_data.close()
    file_enkripsi.close()