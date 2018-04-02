# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
#######################
#myconf = AppConfig(reload=True)
#######################

from gluon.tools import Auth
#######################
#auth = Auth(db)
#auth.define_tables(username=False, signature=False)
#######################
# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
            pool_size=configuration.get('db.pool_size'),
            migrate_enabled=configuration.get('db.migrate'),
            check_reserved=['all'])

else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configure.get('heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)


## CREATE PRODUTOS ##
Produtos = db.define_table('produtos',
Field('fabricante', 'string', label='Fabricante'),
Field('equipamento', 'string', label='Equipamento'),
Field('part_number', 'integer', label='Part Number'),
Field('expiracao', 'datetime', label='Data de Expiração'),
Field('serial_number', 'integer', label='Serial Number'),
Field('armazenamentos', 'list:reference armazenamentos', label='Local de Armazenamento'),
Field('data_cadastro', 'datetime', label='Data de Cadastro'),
Field('custo_entrada', 'integer', label='Custo de Entrada'),
Field('foto', 'upload', label='Foto'),
Field('usuario_entrada', 'reference auth_user', label='Usuário de Entrada')
)

## CREATE ARMAZENAMENTOS ##
Armazenamentos = db.define_table('armazenamentos',
Field('nome', 'string', label='Nome do Local')
)

## CREATE ITEMS ESTOQUE ##
ItemsEstoque = db.define_table('items_estoque',
Field('produto', 'reference produtos', label='Produto'),
Field('quantidade', 'integer', label='Quantidade'),
Field('preco', 'float', label='Preço')
)

## CREATE CLIENTE ##
Clientes = db.define_table('clientes',
Field('razao_social', 'string', label='Razão Social'),
Field('nome_fantasia', 'string', label ='Nome Fantasia'),
Field('cnpj', 'integer', label='CNPJ'),
Field('telefone', 'integer', label='Telefone/Celular'),
Field('email', 'string', label='E-mail'),
Field('logradouro', 'string', label='Logradouro'),
Field('numero', 'float', label='Número'),
Field('complemento', 'string', label='Complemento'),
Field('bairro', 'string', label='Bairro'),
Field('cidade', 'string', label='Cidade'),
Field('estado', 'string', label='Estado'),
Field('pais', 'string', label='País')
)

## CREATE TIPO EMBARCACAO ##
TipoEmbarcacao = db.define_table('tipo_embarcacao',
Field('nome', 'string', label='Tipo de Embarcação')
)

## CREATE EMBARCACAOES ##
Embarcacoes = db.define_table('embarcacoes',
Field('nome', 'string', label='Nome da Embarcação'),
Field('tipo', 'list:reference tipo_embarcacao', label='Tipo de Embarcação'),
Field('clientes', 'list:reference clientes', label='Cliente')
)

## CREATE TIPOSSAIDA ##
TiposSaida = db.define_table('tipos_saida',
Field('nome', 'string', label='Tipo de Saída')
)

## CREATE SAIDA ##
Saida = db.define_table('saidas',
Field('produtos', 'list:reference produtos', label='Produto'),
Field('usuario_saida', 'reference auth_user', label='Usuário de Saída'),
Field('cliente', 'list:reference clientes', label='Cliente'),
Field('embarcacoes', 'list:reference embarcacaoes', label='Embarcação'),
Field('tipos_saida', 'list:reference tipos_saida', label='Tipo de Saída'),
Field('data_saida', 'datetime', label='Data de Saída'),
Field('data_devolucao', 'datetime', label='Data de Devolução')
)
