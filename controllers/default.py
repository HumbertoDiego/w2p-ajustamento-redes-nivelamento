# -*- coding: utf-8 -*-

def index():
    return locals()

def ajunivgeo():
    rows = db(db.successcount).select() # acessa o banco de dadose seleciona o valor de sucessos
    sucessos=int(rows[0].contador)
    return locals()

def executar():
    import NivParamet
    import os, time
    form = SQLFORM.factory(Field('arquivo','upload', uploadfolder=os.path.join(request.folder,'uploads'),
                                 requires=[IS_NOT_EMPTY(error_message='Sem arquivo !'),IS_LENGTH(1048576, 0)]),
                          Field('dp', requires = IS_FLOAT_IN_RANGE(0.0001, 100, dot=".", error_message='0.0001< X <100 !'),
                                label='Desvio Padrão = Xmm*RAIZ(dist[Km])', default = 1,
                                widget=SQLFORM.widgets.autocomplete(request, db.dp.X, min_length=0)),
                           Field('automatico', 'boolean',default = True, label='Desvio Padrão automático'),
                           Field('dpinformado', 'boolean',default = False, label='Desvio padrão(m) informado na coluna das distâncias'),
                           submit_button = 'Enviar'
                          )
    form.element('input[name=dp]')['_style']='width:100px'
    rows = db(db.successcount).select() # acessa o banco de dados e seleciona o valor de sucessos
    sucessos=int(rows[0].contador)
    dicionariofinal = dict(form=form ,filename= form.vars.file, erro=False, sucessos=sucessos)
#     try:
    if form.process().accepted:
        ini=time.time()
        session.file = form.vars.arquivo
        dicionariofinal['filename'] = form.vars.arquivo
        X = form.vars.dp
        auto = form.vars.automatico
        dp_na_4col = form.vars.dpinformado
        filepath = os.path.join(request.folder, 'uploads') + '/' + str(session.file)
        print "1"
        dicionario = NivParamet.parametrico(filepath, X, auto, dp_na_4col).copy()
        print "2"
        dicionariofinal.update(dicionario)
        os.remove(filepath)
        # Contador de sucessos - acessa o banco de dados e incrementa o valor de sucessos
        novovalor= int(rows[0].contador)+1
        db(db.successcount).update(contador=novovalor)
        dicionariofinal['sucessos'] = novovalor
        print "tempo dentro do try:",time.time()-ini
#     except:
# #         ini=time.time()
# #         time.sleep(4) # dorme por 4 segundos
#         os.remove(filepath)
#         dicionario = dict(erro=True)
#         dicionariofinal.update(dicionario)
#         print "tempo dentro do erro:",time.time()-ini
    return dicionariofinal

def exemplos():
    rows = db(db.successcount).select() # acessa o banco de dados e seleciona o valor de sucessos
    sucessos=int(rows[0].contador)
    return locals()

def downloads():
    rows = db(db.successcount).select() # acessa o banco de dados e seleciona o valor de sucessos
    sucessos=int(rows[0].contador)
    return locals()

def refer():
    rows = db(db.successcount).select() # acessa o banco de dados e seleciona o valor de sucessos
    sucessos=int(rows[0].contador)
    return locals()
