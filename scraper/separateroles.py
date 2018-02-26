import glob
import os


def parsenames(string):
    nomes = string.split(",")
    last = nomes.pop(-1)
    toadd = last.split(" e ")
    nomes = nomes + toadd
    return nomes


path = '/home/erick/Dropbox/erick/carnavalmanager/data'

autores = set()
carnavalescos = set()
presidentes = set()
diretores = set()
harmonia = set()
mestresalas = set()
portbandeiras = set()
coreografos = set()
bateria = set()

samba_autores = set()
puxadores = set()

for filename in glob.glob(os.path.join(path, '*.txt')):

    f = open(filename, 'r')

    lines = f.readlines()
    for line in lines:
        if line.startswith("Autor(es) do"):
            toadd = parsenames(lines[lines.index(line) + 1])
            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            autores.update(toadd)

        if line.startswith("Carnavalesc"):
            toadd = parsenames(lines[lines.index(line) + 1])
            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            carnavalescos.update(toadd)

        if line.startswith("Presid"):
            toadd = parsenames(lines[lines.index(line) + 1])
            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            presidentes.update(toadd)

        if line.startswith("Diretor de C"):
            toadd = parsenames(lines[lines.index(line) + 1])
            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            diretores.update(toadd)

        if line.startswith("Diretor de H"):
            toadd = parsenames(lines[lines.index(line) + 1])
            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            harmonia.update(toadd)

        if line.startswith("1º Casal de Me") or line.startswith("2º Casal de Mes"):
            toadd = parsenames(lines[lines.index(line) + 1])
            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            if len(toadd) > 1:
                mestresalas.add(toadd[1])
                portbandeiras.add(toadd[0])

        if line.startswith("Coreógra"):
            toadd = parsenames(lines[lines.index(line) + 1])
            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            coreografos.update(toadd)

        if line.startswith("Bateri"):

            toadd = parsenames(lines[lines.index(line) + 1])

            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            check = toadd[0].split("sob o comando de ")
            if len(check) > 1:
                toadd[0] = check[1]
            else:
                if "omponentes" in toadd[0]:
                    toadd[0] = ''
            bateria.update(toadd)

        if line == 'Autor(es)\n':
            toadd = parsenames(lines[lines.index(line) + 1])
            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            samba_autores.update(toadd)

        if line.startswith("Puxador"):
            toadd = parsenames(lines[lines.index(line) + 1])
            for i in range(len(toadd)):
                toadd[i] = toadd[i].strip(' \n')
            puxadores.update(toadd)

    f.close()

autores = sorted(autores)
carnavalescos = sorted(carnavalescos)
presidentes = sorted(presidentes)
diretores = sorted(diretores)
harmonia = sorted(harmonia)
mestresalas = sorted(mestresalas)
portbandeiras = sorted(portbandeiras)
coreografos = sorted(coreografos)
bateria = sorted(bateria)

samba_autores = sorted(samba_autores)
puxadores = sorted(puxadores)
f = open("/home/erick/Dropbox/erick/carnavalmanager/data/autores.txt", 'w')
for item in autores:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/carnavalescos.txt", 'w')
for item in carnavalescos:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/presidentes.txt", 'w')
for item in presidentes:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/diretores.txt", 'w')
for item in diretores:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/harmonia.txt", 'w')
for item in harmonia:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/mestresalas.txt", 'w')
for item in mestresalas:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/portbandeiras.txt", 'w')
for item in portbandeiras:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/coreografos.txt", 'w')
for item in coreografos:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/bateria.txt", 'w')
for item in bateria:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/samba_autores.txt", 'w')
for item in samba_autores:
    f.write(item + '\n')
f.close()

f = open("/home/erick/Dropbox/erick/carnavalmanager/data/puxadores.txt", 'w')
for item in puxadores:
    f.write(item + '\n')
f.close()

