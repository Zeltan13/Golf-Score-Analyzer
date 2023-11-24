#Daftar Deklarasi Fungsi
def pemain_golf(filename):
    openfile = open(filename,"r")
    par_number = 5
    dict_score = {
        'QD': 4,
        'TP': 3,
        'TR': 3,
        'DB': 2,
        'BG': 1,
        'BR': -1,
        'EG': -2,
        'AL': -3,
        'CN': -4,
        'ACE': -4
    }
    list_pemain = [] 
    
    textline = openfile.readline().replace("\n", "")
    
    while textline != "":
        words = textline.split(' ')
        player = {} # dict
        player = {'nama': words[0]}
        for index in range(len(words)):
            if index not in [0]:
                if words[index] == 'PAR':
                    player['hole' + str(index)] = par_number
                else:
                    player['hole' + str(index)] = par_number + dict_score[words[index]]
        list_pemain.append(player)
        textline = openfile.readline().replace("\n","")    
    openfile.close()
    return list_pemain


def pemenang(_list_pemain):
    list_score = {}
    for pemain in _list_pemain:
        nama_pemain = ''
        score_pemain = 0 
        for key, value in pemain.items():
            if key == 'nama':
                nama_pemain = value
            else:
                score_pemain += value
        list_score[nama_pemain] = score_pemain
    x = 0
    nama_pemenang = ''
    no_urut_pemenang = 0
    no_urut = 0
    for nama, score in list_score.items():
        no_urut += 1
        if x == 0 or score < x:
            x = score
            nama_pemenang = nama
            no_urut_pemenang = no_urut
    return no_urut_pemenang, nama_pemenang

def rerata(_list_pemain):
    list1 = []
    for pemain in _list_pemain:
        score_pemain = 0
        for key, value in pemain.items():
            if key != 'nama':
                score_pemain += value
        list1.append(score_pemain)
    jumlah = 0 
    for score in list1:
        jumlah += score
    return jumlah/len(list1)

#Main Program
nama_file = "TUBES.txt"
list_pemain = pemain_golf(nama_file)

print(list_pemain)

no_urut_pemenang, nama_pemenang = pemenang(list_pemain)
print('Pemenang:',nama_pemenang, 'dengan nomor urut', str(no_urut_pemenang))

print('Rerata = ' + str(rerata(list_pemain)))



