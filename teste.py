serv = open('senacverifserv.bat','w+')
caminho = os.getcwd()
texto = fr'cd {caminho}\nSTART {caminho}\senacverifserv.exe'
serv.write(texto)
serv.close()