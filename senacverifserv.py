from principal import BuscaSenac

servico = BuscaSenac()
opt_notif, opt_email = servico.ler_stserv() # Esta função contém o código comentado abaixo.

# opt_notif = True
# opt_email = False
# try:
#     textoopts = open('opts', 'r')
#     opts = textoopts.read()
#     opts = opts.split('.')
#     opt_notif = bool(int(opts[0]))
#     opt_email = bool(int(opts[1]))
#     textoopts.close()
# except FileNotFoundError:
#     textoopts = open('opts', 'w+')
#     if opt_notif == True:
#         opt_notif = 1
#     else:
#         opt_notif = 0
#     if opt_email == True:
#         opt_email = 1
#     else:
#         opt_email = 0
#     textoopts.write(f'{opt_notif}.{opt_email}')
#     textoopts.close()

servico.verificar_novidades(servico=True,notificar=opt_notif, email=opt_email)