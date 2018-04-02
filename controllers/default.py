# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

######## CREATE #########

## CREATE NOVO PRODUTO ##
def cadastrar_produto():
    form = SQLFORM(Produtos)
    if form.process().accepted:
        session.flash = 'Novo produto cadastrado: %s' % form.vars.equipamento
        redirect(URL('cadastrar_produto'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    #else:
        #response.flash = 'Favor, preencha o formulráio!'

    return dict(form = form)

## CREATE NOVO AMARZENAMENTO ##
def cadastrar_local_armazenamento():
    form = SQLFORM(Armazenamentos)
    if form.process().accepted:
        session.flash = 'Local %s cadastrado com sucesso!' % form.vars.nome
        redirect(URL('cadastrar_local_armazenamento'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form = form)

## CREATE NOVO ITEMS ESTOQUE ##
def cadastrar_estoque():
    form = SQLFORM(ItemsEstoque)
    if form.process().accepted:
        session.flash = 'Produto adicionado no estoque com sucesso!'
        redirect(URL('cadastrar_estoque'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form = form)

## CREATE NOVO CLIENTE ##
def cadastrar_cliente():
    form = SQLFORM(Clientes)
    if form.process().accepted:
        session.flash = 'Cliente %s cadastrado com sucesso!' % form.vars.razao_social
        redirect(URL('cadastrar_cliente'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## CREATE NOVO TIPO_EMBARCACAO ##
def cadastrar_tipo_embarcacao():
    form = SQLFORM(TipoEmbarcacao)
    if form.process().accepted:
        session.flash = 'Tipo de embarcação cadastrado com sucesso: $' % form.vars.nome
        redirect(URL('cadastrar_tipo_embarcacao'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## CREATE NOVO EMBARCACAO ##
def cadastrar_embarcacao():
    form = SQLFORM(Embarcacoes)
    if form.process().accepted:
        session.flash = 'Embarcação cadastrado com sucesso: $' % form.vars.nome
        redirect(URL('cadastrar_embarcacao'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## CREATE NOVO TIPO SAIDA ##
def cadastrar_tipo_saida():
    form = SQLFORM(TiposSaida)
    if form.process().accepted:
        session.flash = 'Tipo de saída cadastrado com sucesso: $' % form.vars.nome
        redirect(URL('cadastrar_tipo_saida'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## CREATE SAIDA ##
def cadastrar_saida():
    form = SQLFORM(Saida)
    if form.process().accepted:
        session.flash = 'Feito a Saída do produto com sucesso!'
        redirect(URL('cadastrar_saida'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)



######## READ #########

## READ PRODUTOS ##
def produtos():
    grid = SQLFORM.grid(Produtos)
    return dict(grid=grid)
    #if request.vars.produtos:
        #produtos = db(Produtos.equipamento == request.vars.produto).select()
    #else:
        #produtos = db(Produtos).select()
    #return dict(Produtos=produtos)


## READ LOCAL ARMAZENAMENTO ##
def local_armazenamento():
    grid = SQLFORM.grid(Armazenamentos)
    return dict(grid=grid)


## READ ESTOQUE ##
def estoque():
    estoque = db(ItemsEstoque).select()
    return dict(estoque=estoque)


## READ CLIENTE ##
def clientes():
    grid = SQLFORM.grid(Clientes)
    return dict(grid=grid)


## READ TIPO EMBARCACAO ##
def tipo_embarcacao():
    grid = SQLFORM.grid(TipoEmbarcacao)
    return dict(grid=grid)

## READ EMBARCACOES ##
def embarcacoes():
    grid = SQLFORM.grid(Embarcacoes)
    return dict(grid=grid)

## READ TIPO SAIDA ##
def tipo_saida():
    grid = SQLFORM.grid(TiposSaida)
    return dict(grid=grid)


## READ SAIDA ##
def saida():
    saida = db(Saida).select()
    return dict(saida=saida)


######## UPDATE #########

## EDITAR PRODUTO ##
def editar_produto():
    form = SQLFORM(Produtos, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Produto atualizado: %s' % form.vars.equipamento
        redirect(URL('produtos'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## EDITAR AMARZENAMENTO ##
def editar_produto():
    form = SQLFORM(Armazenamentos, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Local do Armanzenamento atualizado: %s' % form.vars.nome
        redirect(URL('local_armazenamento'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## ALTERAR ESTOQUE ##
def alterar_estoque():
    form = SQLFORM(ItemsEstoque, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Estoque atualizado!'
        redirect(URL('estoque'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## ALTERAR CLIENTE ##
def atualizar_cliente():
    form = SQLFORM(Clientes, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Dados do Cliente atualizado!'
        redirect(URL('clientes'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## ALTERAR TIPO EMBARCACAO ##
def alterar_tipo_embarcacao():
    form = SQLFORM(TipoEmbarcacao, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Dados do Tipo da Embarcação atualizado!'
        redirect(URL('tipo_embarcacao'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## ALTERAR EMBARCACAO ##
def alterar_embarcacao():
    form = SQLFORM(Embarcacoes, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Dados da Emcadastrar_tipo_saidabarcação atualizado!'
        redirect(URL('embarcacoes'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## ALTERAR TIPO SAIDA ##
def alterar_tipo_saida():
    form = SQLFORM(TiposSaida, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Dados do Tipo da Saída atualizado!'
        redirect(URL('tipo_saida'))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

## ALTERAR SAIDA ##
#def atualizr_saida():
#    form = SQLFORM(Saida, request.args(0, cast=int))
#    if form.process().accepted:
#        session.flash = 'Saída atualizada!'
#        redirect(URL('saida'))
#    elif form.errors:
#        response.flash = 'Erros no formulário!'

#    return dict(form=form)


######## DELETE #########

## DELETAR PRODUTO ##
def deletar_produto():
    db(Produtos.id==request.args(0, cast=int)).delete()
    session.flash = 'Produto %s apagado com sucesso!' % form.vars.equipamento
    redirect(URL('produtos'))


## DELETAR LOCAL ARMAZENAMENTO ##
def deletar_local_armazenamento():
    db(Armazenamentos.id==request.args(0, cast=int)).delete()
    session.flash = 'Local %s apagado com sucesso!' % form.vars.nome
    redirect(URL('armazenamento'))


## DELETAR ITEM ESTOQUE ##
def deletar_item_estoque():
    db(ItemsEstoque.id == request.args(0, cast=int)).delete()
    session.flash = '%s do Estoque apagado com sucesso!' % form.vars.produto
    redirect(URL('estoque'))


## DELETAR CLIENTE ##
def deletar_cliente():
    db(Clientes.id == request.args(0, cast=int)).delete()
    session.flash = 'Cliente %s apagado com sucesso!' % form.vars.razao_social
    redirect(URL('clientes'))


## DELETAR TIPO EMBARCACAO ##
def deletar_tipo_embarcacao():
    db(TipoEmbarcacao.id == request.args(0, cast=int)).delete()
    session.flash = '%s apagado com sucesso!' % form.vars.nome
    redirect(URL('tipo_embarcacao'))


## DELETAR EMBRACACAO ##
def deletar_embarcacao():
    db(Embarcacoes.id == request.args(0, cast=int)).delete()
    session.flash = '%s apagado com sucesso!' % form.vars.nome
    redirect(URL('embarcacoes'))


## DELETAR TIPO_SAIDA ##
def deletar_tipo_saida():
    db(TiposSaida.id == request.args(0, cast=int)).delete()
    session.flash = '%s apagado com sucesso!' % form.vars.nome
    redirect(URL('tipo_saida'))


## DELETAR SAIDA ##
