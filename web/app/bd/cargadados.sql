DELETE FROM produto_tamanho;
DELETE FROM produto;        
DELETE FROM associado_categorias;
DELETE FROM associado;
DELETE FROM associado_usuario_tags;
DELETE FROM categoria;


-- Categoria (OK)
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (1, 'BEBIDAS', NULL, 'categorias/bebidas.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (2, 'BOLOS', NULL, 'categorias/bolos.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (3, 'DOCES', NULL, 'categorias/300x200.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (4, 'CACHORROS-QUENTES', NULL, 'categorias/hotdogs.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (5, 'HAMBURGUER', NULL, 'categorias/300x200.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (6, 'KITS FESTA', NULL, 'categorias/doces.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (7, 'LANCHES', NULL, 'categorias/lanches.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (8, 'PIZZAS', NULL, 'categorias/pizzas.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (9, 'PORÇÕES', NULL, 'categorias/porcoes.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (10, 'REFEIÇÕES', NULL, 'categorias/300x200.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (11, 'SOBREMESAS', NULL, 'categorias/sobremesas.jpg');
INSERT INTO categoria (id, descricao, dtregistro, logo)  VALUES (12, 'SALGADOS', NULL, 'categorias/300x200.jpg');

-- -- Associados
 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
	VALUES (1, 'Disponivel', '1@gmail.com', 'Art Ny', 'Ateliê de Doces', 'Doces, Bolos, Sobremesas', 'Seg a Sáb', '08:00', '23:00', 'S', '3,00', 'Fisica', 'Rua Chile', '67', NULL, 'Rebouças', NULL, NULL, NULL, NULL, 'associados/1.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
	VALUES (2, 'Disponivel', '2@gmail.com', 'Burger Time Torres', 'Delivery de hamburger artesanal', 'Lanches, Hamburger', 'Qua a Dom', '18:30', '23:30', 'N', '0,00', 'Juridica', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'associados/2.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
 	VALUES (3, 'Disponivel', '3@gmail.com', 'Dogão Tia Jú', '', 'Lanches, Cachorro Quente', 'Seg a Dom', '19:00', '00:00', 'S', '3,00', 'Juridica', 'Rua dorival Almir Zagonel', '101', NULL, 'Prado Velho', NULL, NULL, NULL, NULL, 'associados/3.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
        VALUES (4, 'Disponivel', '4@gmail.com', 'Dog Ostenta', '', 'Lanches, Cachorro Quente', 'Seg a Dom', '19:00', '00:00', 'N', '0,00', 'Juridica', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'associados/4.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
     	VALUES (5, 'Disponivel', '5@gmail.com', 'Gisa Doces', '', 'Doces, Bolos, Salgados', 'Seg a Sáb', '08:00', '20:00', 'X', '0,00', 'Juridica', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'associados/5.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
     	VALUES (6, 'Disponivel', '6@gmail.com', 'Beijoca', 'Ateliê de Doces', 'Doces, Bolos, Sobremesas', 'Seg a Sáb', '08:00', '21:00', 'S', '3,00', 'Juridica', 'Rua Chile', '67', NULL, 'Rebouças', NULL, NULL, NULL, NULL, 'associados/6.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
    	VALUES (7, 'Disponivel', '7@gmail.com', 'Irmãos P.D.J', '', 'Lanches, Porções, Refeições', 'Seg a Dom', '19:00', '00:00', 'N', '0,00', 'Juridica', 'Rua Pedro Costa Cunha', '37', NULL, 'Prado Velho', NULL, NULL, NULL, NULL, 'associados/500x300.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
    	VALUES (8, 'Disponivel', '8@gmail.com', 'Val Bebidas', '',  'Bebidas', 'Seg a Sex', '09:30', '20:30', 'S', '3,00', 'Juridica', 'Rua Manoel Martins de Abreu', '158', NULL, 'Prado Velho', NULL, NULL, NULL, NULL, 'associados/500x300.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
     	VALUES (9, 'Disponivel', '9@gmail.com', 'Rei dos Salgados', 'A melhor comida caseira da região.', 'Salgados, Refeições', 'Seg a Sex', '06:30', '18:30', 'X', '0,00', 'Juridica', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'associados/9.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
     	VALUES (10, 'Disponivel', '10@gmail.com', 'Lisa Salgados', '', 'Doces, Bolos, Salgados', 'Seg a Dom', '08:00', '20:00', 'X', '0,00', 'Juridica', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'associados/10.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
     	VALUES (11, 'Disponivel', '11@gmail.com', 'Feijoada da Dona Rosa', '', 'Refeições, Feijoada', 'Sáb', '11:30', '14:30', 'X', '0,00', 'Juridica', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'associados/500x300.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
     	VALUES (12, 'Disponivel', '12@gmail.com', 'Jeu Panquecas', '',  'Panquecas, Refeições', 'Seg a Sex', '18:00', '21:00', 'X', '0,00', 'Juridica', 'Rua Manoel Freire', '137', NULL, 'Prado Velho', NULL, NULL, NULL, NULL, 'associados/500x300.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
     	VALUES (13, 'Disponivel', '13@gmail.com', 'Confeitaria da Cris', '', 'Lanches, Hamburger, Porcões', 'Seg a Dom', '', '', 'N', '0,00', 'Juridica', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'associados/13.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
     	VALUES (14, 'Disponivel', '14@gmail.com', 'Eparry Pastel', '', 'Pastel, Bebidas', 'Ter a Sáb', '18:00', '00:00', 'X', '0,00', 'Juridica', 'Rua Manoel Martins de Abreu', '129', NULL, 'Prado Velho', NULL, NULL, NULL, NULL, 'associados/500x300.jpg');

 INSERT INTO associado (id, situacao, email, nomefantasia, resumo, categoria, funcionamentodias, funcionamentohorarioinicio, funcionamentohorariotermino, taxaentrega, valortaxaentrega, tipopessoa, logradouro, numero, complemento, bairro, cidade, estado, cep, dtregistro, logo) 
	VALUES (15, 'Disponivel', '15gmail.com', 'Pizzaria Dom Juan', '', 'Pizzas, Lanches', 'Seg a Dom', '19:00', '23:59', 'S', '2,50', 'Juridica', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'associados/500x300.jpg');

--categoriaxassociado
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(1, 2, 1,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(2, 3, 1,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(3, 11, 1,  '', '', NULL);

 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(5, 1, 2,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(6, 5, 2,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(7, 11, 2,  '', '', NULL);

 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(8, 1, 3,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(9, 4, 3,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(10, 7, 3,  '', '', NULL);

 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(11, 1, 4,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(12, 4, 4,  '', '', NULL);

 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(13, 2, 5,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(14, 3, 5,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(15, 6, 5,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(16, 12, 5,  '', '', NULL);

 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(17, 3, 6,  '', '', NULL);
 INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(18, 6, 6,  '', '', NULL);
 
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(19, 7, 7,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(20, 9, 7,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(21, 10, 7,  '', '', NULL);

INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(22, 1, 8,  '', '', NULL);

INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(23, 10, 9,  '', '', NULL);

INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(24, 2, 10,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(25, 3, 10,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(26, 6, 10,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(27, 12, 10,  '', '', NULL);

INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(28, 10, 11,  '', '', NULL);

INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(29, 10, 12,  '', '', NULL);

INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(30, 1, 13,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(31, 5, 13,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(32, 9, 13,  '', '', NULL);

INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(33, 1, 14,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(34, 12, 14,  '', '', NULL);


INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(35, 7, 15,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(36, 8, 15,  '', '', NULL);
INSERT INTO associado_categorias(id, categoria_id, associado_id, resumo, logo, dtregistro)
        VALUES(37, 9, 15,  '', '', NULL);


