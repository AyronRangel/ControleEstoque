# -*- CODING: UTF-8 -*-

#Validador de Produtos
Produtos.fabricante.requires = IS_NOT_EMPTY()
Produtos.equipamento.requires = [IS_NOT_EMPTY(),
                                 IS_NOT_IN_DB(db, 'produtos.equipamento')]
Produtos.part_number.requires = IS_NOT_EMPTY()
Produtos.expiracao.requires = IS_DATETIME(format='%d/%m/%Y')
Produtos.serial_number.requires = IS_NOT_EMPTY()
Produtos.armazenamentos.requires = IS_IN_DB(db, 'armazenamentos.id', '%(nome)s')
Produtos.data_cadastro.requires = IS_DATETIME(format='%d/%m/%Y')
Produtos.custo_entrada.requires = IS_NOT_EMPTY()
Produtos.foto.requires = IS_EMPTY_OR(IS_IMAGE())
Produtos.usuario_entrada.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s')


#Validador do Armazenamentos
Armazenamentos.nome.requires = [IS_NOT_EMPTY(),
                                 IS_NOT_IN_DB(db, 'armazenamentos.nome')]

#Validador de ItemsEstoque
ItemsEstoque.produto.requires = IS_IN_DB(db, 'produtos.id', '%(equipamento)s', _and=IS_NOT_IN_DB(db, 'items_estoque.produto'))
ItemsEstoque.quantidade.requires = IS_NOT_EMPTY()
ItemsEstoque.preco.requires = IS_NOT_EMPTY()


#Validador de Clientes
Clientes.razao_social.requires = [IS_NOT_EMPTY(),
                                 IS_NOT_IN_DB(db, 'clientes.razao_social')]
Clientes.nome_fantasia.requires = IS_NOT_EMPTY()
Clientes.cnpj.requires = [IS_NOT_EMPTY(),
                                 IS_NOT_IN_DB(db, 'clientes.cnpf')]
Clientes.telefone.requires = IS_NOT_EMPTY()
Clientes.email.requires = IS_NOT_EMPTY()
Clientes.logradouro.requires = IS_NOT_EMPTY()
Clientes.numero.requires = IS_NOT_EMPTY()
Clientes.bairro.requires = IS_NOT_EMPTY()
Clientes.cidade.requires = IS_NOT_EMPTY()
Clientes.estado.requires = IS_NOT_EMPTY()
Clientes.pais.requires = IS_NOT_EMPTY()


#Validador de Tipo Embarcacao
TipoEmbarcacao.nome.requires = [IS_NOT_EMPTY(),
                                 IS_NOT_IN_DB(db, 'tipo_embarcacao.nome')]


#Validador de Embarcacoes
Embarcacoes.nome.requires = [IS_NOT_EMPTY(),
                                 IS_NOT_IN_DB(db, 'embarcacao.nome')]
Embarcacoes.tipo.requires = IS_IN_DB(db, 'tipo_embarcacao.id', '%(nome)s')
Embarcacoes.clientes.requires = IS_IN_DB(db, 'clientes.id', '%(razao_social)s')


#Validador de TiposSaidas
TiposSaida.nome.require = IS_NOT_EMPTY()


#Validador Saida
Saida.produtos.requires =  IS_NOT_IN_DB(db, 'produtos.id', '%(equipamento)s')
Saida.usuario_saida.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s')
Saida.cliente.requires = IS_NOT_IN_DB(db, 'clientes.id', '%(razao_social)s')
Saida.embarcacoes.requires = IS_NOT_IN_DB(db, 'embarcacaoes.id', '%(nome)s')
Saida.tipos_saida.requires = IS_NOT_IN_DB(db, 'tipos_saida.id', '%(nome)s')
Saida.data_saida.requires = IS_DATETIME(format='%d/%m/%Y')
Saida.data_devolucao.requires = IS_DATETIME(format='%d/%m/%Y')

