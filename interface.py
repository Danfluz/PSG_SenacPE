import os
import PySimpleGUI as sg
from principal import BuscaSenac
import webbrowser

"""
Implementar funcionalidade de add usuário (email) - CONCLUÍDO 1.0
Implementar funcionalidade de notificação por email - CONCLUÍDO 1.1
Implementar funcionalidade de verificar inscrições abertas - PENDENTE
"""

acao = BuscaSenac()
#Tema inicial
try:
    configtxt = open('th')
    cnf = configtxt.read()
    if cnf == 'th2':
        lay_n = 2
    else:
        lay_n = 1
    configtxt.close()
except FileNotFoundError:
    lay_n = 1

mudoutema = False
mudoufixo = False
janopen = False
configopen = False
segspadrao = 5
reset_opcoes = False
try:
    file = open('serv','r')
    numerobol = int(file.read())
    if bool(numerobol) == True:
        verificacao_automatica = True
    else:
        verificacao_automatica = False
    file.close()
except FileNotFoundError:
    verificacao_automatica = False
def tinicial():
    sg.theme('Reddit')
    layout = [
        [sg.Text('', size=(30,1),background_color='#ffffff'), sg.Image('img/senac.png',subsample=1,background_color='#ffffff'),sg.T('',size=(20,1),background_color='#ffffff'),sg.Button('',image_filename='img/pincel1b.png',auto_size_button=True,button_color='#EA951E',key='mudartema'),sg.Button('',image_filename='img/conf1b.png',button_color='#EA951E',key='config',image_size=(25,20),auto_size_button=True)],
        # [sg.Text('', size=(30,1),background_color='#ffffff'), sg.Image('img/senac.png',subsample=1,background_color='#ffffff'),sg.T('',size=(20,1),background_color='#ffffff'),sg.Button('',image_filename='img/pincel1b.png',auto_size_button=True,button_color='#EA951E',key='mudartema')],
        [sg.Text('', size=(18,1),background_color='#ffffff'), sg.Text('Programa Senac de Gratuidade',text_color='#1a1a1b',font='Arial 14 bold',background_color='#ffffff')],
        [sg.Text('',size=(29,1),background_color='#ffffff'), sg.Text('',font='Arial 8',background_color='#ffffff',text_color='#1a1a1b'), sg.Text('',background_color='#ffffff')],
        [sg.Text('\nClique para verificar os editais recentes:',font='Arial 10',text_color='#1a1a1b',size=(30,3),background_color='#ffffff'), sg.Button('Verificar',button_color=('#0079d3'))],
        [sg.Text('Editais:',font='Arial 11 bold',background_color='#ffffff',text_color='#1a1a1b')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital1',size=(40,1)),sg.Button('Cursos',visible=False,key='ver1',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf1',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital2',size=(40,1)),sg.Button('Cursos',visible=False,key='ver2',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf2',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital3',size=(40,1)),sg.Button('Cursos',visible=False,key='ver3',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf3',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital4',size=(40,1)),sg.Button('Cursos',visible=False,key='ver4',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf4',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital5',size=(40,1)),sg.Button('Cursos',visible=False,key='ver5',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf5',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital6',size=(40,1)),sg.Button('Cursos',visible=False,key='ver6',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf6',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital7',size=(40,1)),sg.Button('Cursos',visible=False,key='ver7',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf7',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital8',size=(40,1)),sg.Button('Cursos',visible=False,key='ver8',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf8',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital9',size=(40,1)),sg.Button('Cursos',visible=False,key='ver9',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf9',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff'),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='edital10',size=(40,1)),sg.Button('Cursos',visible=False,key='ver10',button_color='#0079d3'),sg.Button('Abrir Edital',visible=False,key='pdf10',button_color='#0079d3')],
        [sg.Text('',background_color='#ffffff',size=(20,3)),sg.Text('',background_color='#ffffff',text_color='#1a1a1b',key='status')],
    ]

    return sg.Window('PSG', layout=layout, finalize=True, size=(630,600),icon='img/senacico.ico')

def tinicial2():
    sg.theme('DarkBlue16')
    layout = [
        [sg.Text('', size=(30,1),background_color='#1c44ac'), sg.Image('img/senac2.png',subsample=1,background_color='#1c44ac'),sg.T('',size=(20,1),background_color='#1c44ac'),sg.Button('',image_filename='img/pincel1b.png',auto_size_button=True,button_color='#1c44ac',key='mudartema'),sg.Button('',image_filename='img/conf1b.png',button_color='#1c44ac',key='config',image_size=(25,20),auto_size_button=True)],
        [sg.Text('', size=(18,1),background_color='#1c44ac'), sg.Text('Programa Senac de Gratuidade',font='Arial 14 bold',background_color='#1c44ac',text_color='white')],
        [sg.Text('',size=(29,1),background_color='#1c44ac'), sg.Text('',background_color='#1c44ac',font='Arial 8',text_color='white'), sg.Text('',background_color='#1c44ac',text_color='white')],
        [sg.Text('\nClique para verificar os editais recentes:',font='Arial 10',size=(30,3),background_color='#1c44ac',text_color='white'), sg.Button('Verificar',button_color=('white','#0079d3'))],
        [sg.Text('Editais:',font='Arial 11 bold',background_color='#1c44ac',text_color='white')],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital1',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver1',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf1',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital2',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver2',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf2',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital3',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver3',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf3',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital4',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver4',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf4',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital5',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver5',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf5',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital6',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver6',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf6',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital7',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver7',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf7',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital8',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver8',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf8',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital9',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver9',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf9',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac'),sg.Text('',text_color='white',key='edital10',size=(40,1),background_color='#1c44ac'),sg.Button('Cursos',visible=False,key='ver10',button_color=('white','#0079d3')),sg.Button('Abrir Edital',visible=False,key='pdf10',button_color=('white','#0079d3'))],
        [sg.Text('',background_color='#1c44ac',size=(20,3)),sg.Text('',text_color='white',size=(40,1),background_color='#1c44ac',key='status')],
    ]
    return sg.Window('PSG', layout=layout, finalize=True, size=(630,600),icon='img/senacico.ico')

# for arq in os.listdir(os.getcwd()):
#     if arq == 'cursosmem':
#         # Aqui eu queria já deixar os nomes pré-carregados, mas não sei se vai ser ágil.

def tconfig(desativado=True,ativado=False, opt_notif='Não', opt_email='Não', eml=''):
    sg.theme('Reddit')
    if ativado == True:
        visible = True
    else:
        visible = False
    layout = [
        [sg.Text('', size=(30,1),background_color='#ffffff'), sg.Image('img/senac.png',subsample=1,background_color='#ffffff')],
        [sg.Text('', size=(27,1),background_color='#ffffff'), sg.Text('Configurações',text_color='#1a1a1b',font='Arial 14 bold',background_color='#ffffff')],
        [sg.Text('', size=(29,1),background_color='#ffffff'), sg.T('Ver. 1.1b por Dan F Luz',font='Arial 8',background_color='#ffffff',text_color='black')],
        [sg.Text('', size=(30,1),background_color='#ffffff')],
        [sg.Text('', size=(15,1),background_color='#ffffff'),sg.T('Verificação automática',size=(23,1),background_color='#ffffff',text_color='black'),sg.Button('Desativado',visible=desativado,key='desativado',button_color='red'),sg.Button('Ativado',visible=ativado,key='ativado',button_color='green')],
        [sg.Text('', size=(15,1),background_color='#ffffff'),sg.T('Notificações push (Windows)',size=(23,1),background_color='#ffffff',text_color='black',visible=visible,key='pushtext'),sg.Combo(['Sim','Não'],[opt_notif],text_color='black',background_color='white',key='notif_push',size=(12),visible=visible,readonly=True)],
        [sg.Text('', size=(15,1),background_color='#ffffff'),sg.T('Notificar por email',size=(23,1),background_color='#ffffff',text_color='black',visible=visible,key='emailtext'),sg.Combo(['Sim','Não'],[opt_email],text_color='black',background_color='white',key='notif_email',size=(12),visible=visible,readonly=True)],
        [sg.Text('', size=(15,1),background_color='#ffffff'),sg.T('Email para notificações',size=(23,1),background_color='#ffffff',text_color='black',visible=visible,key='emaildesc'),sg.Input(eml,text_color='black',background_color='white',key='emailcampo',size=(30),visible=visible)],
        [sg.Text('', size=(30,1),background_color='#ffffff')],
        [sg.Text('', size=(30,1),background_color='#ffffff')],
        [sg.Text('', size=(35,1),background_color='#ffffff'),sg.B('OK',key='Voltar')],
        [sg.Text('', size=(30, 1), background_color='#ffffff')],
        [sg.Text('', size=(30, 1), background_color='#ffffff')],
        [sg.Text('', size=(30, 1), background_color='#ffffff')],
        [sg.Text('', size=(30, 1), background_color='#ffffff')],
        [sg.Text('', size=(30, 1), background_color='#ffffff')],
        [sg.Text('', size=(30, 1), background_color='#ffffff')],
        [sg.Text('', size=(30, 1), background_color='#ffffff')],
        [sg.Text('', size=(62, 1), background_color='#ffffff'), sg.B('Resetar', key='Resetar', button_color=('black','white'),mouseover_colors='lightgray')],
    ]

    return sg.Window('PSG', layout=layout, finalize=True, size=(630,600),background_color='#ffffff',icon='img/senacico.ico')

# Checagem de segurança
contador = 0
for arqpdf in os.listdir(os.getcwd()):
    if arqpdf.endswith('.pdf'):
        contador +=1
if contador > 8:
    segurança = True
else:
    segurança = False

if lay_n == 1:
    janela = tinicial()
else:
    janela = tinicial2()

while True:
    event, value = janela.read()

    if configopen == True:
        if event == 'desativado': # Isso ativa tudo (os nomes são invertidos)
            verificacao_automatica = True
            janela['desativado'].update(visible=False)
            janela['ativado'].update(visible=True)
            janela['emailtext'].update(visible=True)
            janela['pushtext'].update(visible=True)
            janela['notif_push'].update(visible=True)
            janela['notif_email'].update(visible=True)
            janela['emaildesc'].update(visible=True)
            janela['emailcampo'].update(visible=True)
            janela.refresh()
            acao.statusservico(True)
        if event == 'ativado': # Isso desativa tudo
            verificacao_automatica = False
            janela['ativado'].update(visible=False)
            janela['desativado'].update(visible=True)
            janela['emailtext'].update(visible=False)
            janela['pushtext'].update(visible=False)
            janela['notif_push'].update(visible=False)
            janela['notif_email'].update(visible=False)
            janela['emaildesc'].update(visible=False)
            janela['emailcampo'].update(visible=False)
            janela.refresh()
            acao.statusservico(False)
        if event == 'Voltar': # O botão de ok
            if '@' in value['emailcampo']:
                acao.email = value['emailcampo']
                eml = open('eml','w+')
                eml.write(acao.email)
                eml.close()
            caminhoserv = os.getcwd()
            if verificacao_automatica == True:
                os.system(fr'schtasks /create /sc hourly /mo 1 /tn "VERIF-PSG-SENAC" /f /tr "{caminhoserv}\senacverifserv.bat" /st 00:00')
                serv = open('senacverifserv.bat', 'w+')
                caminho = os.getcwd()
                texto = f'@echo off\ncd {caminho}\nSTART {caminho}\senacverifserv.exe'
                serv.write(texto)
                serv.close()
            else:
                os.system('schtasks /delete /tn "VERIF-PSG-SENAC" /f')
            # Definindo opcoes no arquivo de configuração
            textoopts = open('opts', 'w+')
            if value['notif_push'] == 'Sim':
                opt_notif = 1
            else:
                opt_notif = 0
            if value['notif_email'] == 'Sim':
                opt_email = 1
            else:
                opt_email = 0
            textoopts.write(f'{opt_notif}.{opt_email}')
            textoopts.close()

    if event == sg.WIN_CLOSED:
        if reset_opcoes == True:
            acao.opcoes = ''

        cursosmem = open('cursosmem', 'w+')
        cursosmem.write(str(acao.opcoes))
        cursosmem.close()
        break

    if event == 'Resetar':
        reset_opcoes = True

    if event == 'Verificar':
        if segurança == True:
            # sg.popup_auto_close('Verificando...', auto_close_duration=3,non_blocking=True,no_titlebar=True,keep_on_top=True,background_color='darkorange')
            sg.popup_no_buttons('Verificando...', auto_close_duration=5,non_blocking=True,no_titlebar=True,keep_on_top=True,background_color='lightblue',auto_close=True,text_color='black')
        if segurança == False:
            sg.popup_no_buttons('Isso pode levar até 10 minutos dependendo\n\tda conexão entre você e o Senac.\n\t\t\tAguarde...', auto_close_duration=20, non_blocking=True, no_titlebar=True,
                                keep_on_top=False, background_color='lightblue', auto_close=True,text_color='black')

        try:
            acao.baixar_editais(index=0)
            janela['edital1'].update(acao.ler_editais(index=0)[0][1])
            janela['ver1'].update(visible=True)
            janela['pdf1'].update(visible=True)
        except:
            janela['edital1'].update('Não foi possível obter este edital.')
        janela.refresh()
        try:
            acao.baixar_editais(index=1)
            janela['edital2'].update(acao.ler_editais(index=1)[0][1])
            janela['ver2'].update(visible=True)
            janela['pdf2'].update(visible=True)
        except:
            janela['edital2'].update('Não foi possível obter este edital.')
        janela.refresh()
        try:
            acao.baixar_editais(index=2)
            janela['edital3'].update(acao.ler_editais(index=2)[0][1])
            janela['ver3'].update(visible=True)
            janela['pdf3'].update(visible=True)
        except:
            janela['edital3'].update('Não foi possível obter este edital.')
        janela.refresh()
        try:
            acao.baixar_editais(index=3)
            janela['edital4'].update(acao.ler_editais(index=3)[0][1])
            janela['ver4'].update(visible=True)
            janela['pdf4'].update(visible=True)
        except:
            janela['edital4'].update('Não foi possível obter este edital.')
        janela.refresh()
        try:
            acao.baixar_editais(index=4)
            janela['edital5'].update(acao.ler_editais(index=4)[0][1])
            janela['ver5'].update(visible=True)
            janela['pdf5'].update(visible=True)
        except:
            janela['edital5'].update('Não foi possível obter este edital.')
        janela.refresh()
        try:
            acao.baixar_editais(index=5)
            janela['edital6'].update(acao.ler_editais(index=5)[0][1])
            janela['ver6'].update(visible=True)
            janela['pdf6'].update(visible=True)
        except:
            janela['edital6'].update('Não foi possível obter este edital.')
        janela.refresh()
        try:
            acao.baixar_editais(index=6)
            janela['edital7'].update(acao.ler_editais(index=6)[0][1])
            janela['ver7'].update(visible=True)
            janela['pdf7'].update(visible=True)
        except:
            janela['edital7'].update('Não foi possível obter este edital.')
        janela.refresh()
        try:
            acao.baixar_editais(index=7)
            janela['edital8'].update(acao.ler_editais(index=7)[0][1])
            janela['ver8'].update(visible=True)
            janela['pdf8'].update(visible=True)
        except:
            janela['edital8'].update('Não foi possível obter este edital.')
        janela.refresh()
        try:
            acao.baixar_editais(index=8)
            janela['edital9'].update(acao.ler_editais(index=8)[0][1])
            janela['ver9'].update(visible=True)
            janela['pdf9'].update(visible=True)
        except:
            janela['edital9'].update('Não foi possível obter este edital.')
        janela.refresh()
        try:
            acao.baixar_editais(index=9)
            janela['edital10'].update(acao.ler_editais(index=9)[0][1])
            janela['ver10'].update(visible=True)
            janela['pdf10'].update(visible=True)
        except:
            janela['edital1'].update('Não foi possível obter este edital.')
        janela.refresh()
        janela.force_focus()
        janela['status'].update(acao.verificar_novidades())

    if event == 'ver1':
        if acao.lista_cursos1 == None:
            acao.lista_cursos1 = acao.ler_editais(index=0)[0][2]
            acao.lista_cursos1.insert(0,'')
            acao.lista_cursos1 = '\n• '.join(acao.lista_cursos1)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos1}',relative_location=(100,5),title='Cursos',icon='img/senacico.ico')
    if event == 'pdf1':
        webbrowser.open(acao.caminho_pdf(index=0))

    if event == 'ver2':
        if acao.lista_cursos2 == None:
            acao.lista_cursos2 = acao.ler_editais(index=1)[0][2]
            acao.lista_cursos2.insert(0, '')
            acao.lista_cursos2 = '\n• '.join(acao.lista_cursos2)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos2}', relative_location=(100, 5), title='Cursos',icon='img/senacico.ico')
    if event == 'pdf2':
        webbrowser.open(acao.caminho_pdf(index=1))

    if event == 'ver3':
        if acao.lista_cursos3 == None:
            acao.lista_cursos3 = acao.ler_editais(index=2)[0][2]
            acao.lista_cursos3.insert(0, '')
            acao.lista_cursos3 = '\n• '.join(acao.lista_cursos3)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos3}', relative_location=(100, 5), title='Cursos',icon='img/senacico.ico')
    if event == 'pdf3':
        webbrowser.open(acao.caminho_pdf(index=2))

    if event == 'ver4':
        if acao.lista_cursos4 == None:
            acao.lista_cursos4 = acao.ler_editais(index=3)[0][2]
            acao.lista_cursos4.insert(0, '')
            acao.lista_cursos4 = '\n• '.join(acao.lista_cursos4)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos4}', relative_location=(100, 5), title='Cursos',icon='img/senacico.ico')
    if event == 'pdf4':
        webbrowser.open(acao.caminho_pdf(index=3))

    if event == 'ver5':
        if acao.lista_cursos5 == None:
            acao.lista_cursos5 = acao.ler_editais(index=4)[0][2]
            acao.lista_cursos5.insert(0, '')
            acao.lista_cursos5 = '\n• '.join(acao.lista_cursos5)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos5}', relative_location=(100, 5), title='Cursos',icon='img/senacico.ico')
    if event == 'pdf5':
        webbrowser.open(acao.caminho_pdf(index=4))

    if event == 'ver6':
        if acao.lista_cursos6 == None:
            acao.lista_cursos6 = acao.ler_editais(index=5)[0][2]
            acao.lista_cursos6.insert(0, '')
            acao.lista_cursos6 = '\n• '.join(acao.lista_cursos6)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos6}', relative_location=(100, 5), title='Cursos',icon='img/senacico.ico')
    if event == 'pdf6':
        webbrowser.open(acao.caminho_pdf(index=5))

    if event == 'ver7':
        if acao.lista_cursos7 == None:
            acao.lista_cursos7 = acao.ler_editais(index=6)[0][2]
            acao.lista_cursos7.insert(0, '')
            acao.lista_cursos7 = '\n• '.join(acao.lista_cursos7)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos7}', relative_location=(100, 5), title='Cursos',icon='img/senacico.ico')
    if event == 'pdf7':
        webbrowser.open(acao.caminho_pdf(index=6))

    if event == 'ver8':
        if acao.lista_cursos8 == None:
            acao.lista_cursos8 = acao.ler_editais(index=7)[0][2]
            acao.lista_cursos8.insert(0, '')
            acao.lista_cursos8 = '\n• '.join(acao.lista_cursos8)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos8}', relative_location=(100, 5), title='Cursos',icon='img/senacico.ico')
    if event == 'pdf8':
        webbrowser.open(acao.caminho_pdf(index=7))

    if event == 'ver9':
        if acao.lista_cursos9 == None:
            acao.lista_cursos9 = acao.ler_editais(index=8)[0][2]
            acao.lista_cursos9.insert(0, '')
            acao.lista_cursos9 = '\n• '.join(acao.lista_cursos9)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos9}', relative_location=(100, 5), title='Cursos',icon='img/senacico.ico')
    if event == 'pdf9':
        webbrowser.open(acao.caminho_pdf(index=8))

    if event == 'ver10':
        if acao.lista_cursos10 == None:
            acao.lista_cursos10 = acao.ler_editais(index=9)[0][2]
            acao.lista_cursos10.insert(0, '')
            acao.lista_cursos10 = '\n• '.join(acao.lista_cursos10)
        sg.popup(f'\t\tCursos:\n{acao.lista_cursos10}', relative_location=(100, 5), title='Cursos',icon='img/senacico.ico')
    if event == 'pdf10':
        webbrowser.open(acao.caminho_pdf(index=9))

    if event == 'mudartema':
        try:
            configtxt = open('th', 'r').read()
            if configtxt == 'th2':
                janela.close()
                janela = tinicial()
                configtxt = open('th', 'w+')
                mudoutema = True
                configtxt.write('th1')
                configtxt.close()
            elif configtxt == 'th1':
                janela.close()
                mudoutema = True
                janela = tinicial2()
                configtxt = open('th', 'w+')
                configtxt.write('th2')
                configtxt.close()
            else:
                os.remove(configtxt)
        except FileNotFoundError:
            janela.close()
            mudoutema = True
            janela = tinicial2()
            configtxt = open('th', 'w+')
            configtxt.write('th2')
            configtxt.close()

    if event == 'config':
        try:
            eml1 = open('eml','r')
            eml = eml1.read()
            eml1.close()
        except:
            pass
        opt_notif, opt_email = acao.ler_stserv()
        if opt_notif == True:
            opt_notif = 'Sim'
        else:
            opt_notif = 'Não'
        if opt_email == True:
            opt_email = 'Sim'
        else:
            opt_email = 'Não'

        janela1 = janela
        janela1.hide()
        if janopen != True:
            if verificacao_automatica == True:
                janela2 = tconfig(desativado=False, ativado=True, opt_notif=opt_notif, opt_email=opt_email, eml=eml)
            else:
                janela2 = tconfig(desativado=True, ativado=False, opt_notif=opt_notif, opt_email=opt_email, eml=eml)
        janela = janela2
        janela.un_hide()
        janopen = True
        configopen = True
    if event == 'Voltar':
        janela2 = janela
        janela2.hide()
        janela = janela1
        janela.un_hide()
        configopen = False




janela.close()
#limpeza de tmps
for file in os.listdir(os.getcwd()):
    if file.endswith('.tmp'):
        os.remove(file)