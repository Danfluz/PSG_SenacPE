import os
import requests
from bs4 import BeautifulSoup
import wget
import pdfplumber
import smtplib
import email.message
import win10toast

class BuscaSenac:

    email = 'danilofluz@recife.pe.senac.br'
    notificacao = win10toast.ToastNotifier()

    try:
        content = requests.get('https://intranet.pe.senac.br/dr/nova/psgnet/Downloads.aspx').content
        site = BeautifulSoup(content, 'html.parser')
        opcoes = site.find_all('option')
        opcoes.remove(opcoes[0])
    except:
        opcoes = ['Não foi possível recuperar os editais']
    provedor = '@gmail.com'
    def __init__(self):
        self.lista_cursos1 = None
        self.lista_cursos2 = None
        self.lista_cursos3 = None
        self.lista_cursos4 = None
        self.lista_cursos5 = None
        self.lista_cursos6 = None
        self.lista_cursos7 = None
        self.lista_cursos8 = None
        self.lista_cursos9 = None
        self.lista_cursos10 = None

    def enviar_email(self, mensagem):
        msg = email.message.Message()
        msg['Subject'] = 'Assunto'
        msg['From'] = 'contafalsaparajogarfora1123'+provedor
        msg['To'] = self.email
        senha = 'zruucbxmjfpiwzgk'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(mensagem)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], senha)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    def verificar_novidades(self, tag_option=None, email=False,printi=False, servico=False, notificar=False):
        tag_option = self.opcoes
        try:
            cursosmem = open('cursosmem', 'r')
            if str(tag_option) != cursosmem.read():
                if printi == True:
                    print('** Há novos editais desde sua última visita! **')
                if email == True:
                    self.enviar_email('Saíram novos editais no Programa de Gratuidade do Senac!\nSe inscreva em: etc etc etc (colocar o link)')
                if notificar == True:
                    self.notificacao.show_toast('Programa de Gratuidade do Senac','Existem novos editais no Programa de Gratuidade do Senac!','img/senacico.ico',duration=10)
                if servico == True:
                    cursosmem.close()
                    cursosmem = open('cursosmem', 'w+')
                    cursosmem.write(str(tag_option))
                    return True
                else:
                    return '** Há novos editais desde sua última visita! **'
                # Enviando email com o texto que a gente quiser

            else:
                if printi == True:
                    print('Não há novos editais desde sua última visita.')
                elif servico == True:
                    cursosmem.close()
                    cursosmem = open('cursosmem', 'w+')
                    cursosmem.write(str(tag_option))
                    return False
                else:
                    return 'Não há novos editais desde sua última visita.'
            cursosmem.close()
        except FileNotFoundError:
            cursosmem = open('cursosmem', 'w+')
            cursosmem.write(str(tag_option))
            pass


    def baixar_editais(self, tag_option=None, printi=False, index=None):
        baixado = False
        tag_option = self.opcoes
        for opcao in tag_option:
            try:
                if index == None:
                    pdf = pdfplumber.open(f'{opcao.text}.pdf')
                    pdf.close()
                else:
                    if opcao == tag_option[index]:
                        pdf = pdfplumber.open(f'{opcao.text}.pdf')
                        pdf.close()
                    else:
                        continue
            except FileNotFoundError:
                if index == None:
                    wget.download(f'http://intranet.pe.senac.br/dr/intranet.net/psgnet/editais/{opcao.text}.pdf')
                    if printi == True:
                        print(f'Baixou {opcao.text}')
                    baixado = True
                else:
                    if opcao == tag_option[index]:
                        wget.download(f'http://intranet.pe.senac.br/dr/intranet.net/psgnet/editais/{opcao.text}.pdf')
                        if printi == True:
                            print(f'Baixou {opcao.text}')
                        baixado = True
                    else:
                        continue
        if printi == True and baixado == True:
            print('Editais baixados.')

    def ler_editais(self, tag_option=None, printi=False, completo=False,index=None):
        tag_option = self.opcoes
        countcursos = 1
        todos_cursos = set()
        all_cursos = []
        for opcao in tag_option:
            cursos = []
            try:
                if index==None:
                    pdf = pdfplumber.open(f'{opcao.text}.pdf')
                else:
                    if opcao == tag_option[index]:
                        pdf = pdfplumber.open(f'{opcao.text}.pdf')
                    else:
                        continue
            except FileNotFoundError:
                if printi == True:
                    print(f'Erro. Há editais não baixados.')
                return 'Não encontrado'

            for pagina in pdf.pages:
                if 'Descrição dos Cursos' in pagina.extract_text():
                    if 'Pré-requisitos e Documentações' in pagina.extract_text():
                        tabela = pagina.extract_tables()[1]
                    else:
                        tabela = pagina.extract_table()
                    for item in tabela:
                        if item[0] != None and item[0] != '' and item[0] != 'Curso':
                            todos_cursos.add(item[0])
                            cursos.append(item[0])

            # Verificação de cursos abertos
            if len(cursos) == 0:
                cursos = ['Não foi possível verificar os cursos']
            elif len(cursos) > 3:
                cursos = cursos[0:4]
            else:
                pass
            all_cursos.append((countcursos, opcao.text, cursos))
            if printi == True:
                print(opcao.text, f'(Cursos: {cursos}...)')
            countcursos += 1
        if completo == False:
            return all_cursos
        else:
            return list(todos_cursos)

    def caminho_pdf(self, index=None):
        for opcao in self.opcoes:
            try:
                if index == None:
                    return fr'{os.getcwd()}\{opcao.text}.pdf'
                else:
                    if opcao == self.opcoes[index]:
                        return fr'{os.getcwd()}\{opcao.text}.pdf'
                    else:
                        continue
            except FileNotFoundError:
                print('Arquivo não existe.')
                continue