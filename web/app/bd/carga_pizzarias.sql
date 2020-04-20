
-- -- Produtos x CategoriasAssociados (LANCHES x Pizzaria Dom Juan)
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('X-Burguer', 'Pão, maionese, hambúrguer, queijo cheddar', '5,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='LANCHES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('X-Egg', 'Pão, maionese, hambúrguer, queijo cheddar, presunto e ovo', '6,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='LANCHES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('X-Salada', 'Pão, maionese, hambúrguer, queijo cheddar, presunto, alface e tomate', '5,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='LANCHES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('X-Bacon', 'Pão, maionese, hambúrguer, queijo cheddar, presunto, alface e tomate, bacon', '8,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='LANCHES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('X-Calabresa', 'Pão, maionese, hambúrguer, queijo cheddar, presunto, alface e tomate, calabresa',  '8,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='LANCHES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('X-Frango', 'Pão, maionese, hambúrguer, queijo cheddar, presunto, alface e tomate, filé de peito de frango',  '9,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='LANCHES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('X-Tudo', 'Pão, maionese, hambúrguer, queijo cheddar, presunto, alface e tomate, filé de peito de frango, bacon, calabresa e milho', '12,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='LANCHES'), NULL, 'Default'); 



-- -- Produtos x CategoriasAssociados (PORÇÕES x Pizzaria Dom Juan)
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Porção de batata', 'não informado', '13,50', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PORÇÕES'), NULL, 'Default');

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Porção de polenta',  'não informado', '13,50', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PORÇÕES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Porção de aipim',  'não informado', '13,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PORÇÕES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Porção de frango a passarinho', 'não informado',  '14,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PORÇÕES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Porção de anéis de cebola',  'não informado', '14,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PORÇÕES'), NULL, 'Default'); 

-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Porção de tiras de frango empanado', 'não informado', '14,00', 'UN', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PORÇÕES'), NULL, 'Default');

   
-- -- Produtos x CategoriasAssociados (PIZZAS x Pizzaria Dom Juan)
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Mussarela', 'Molho, mussarela, azeitona e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)    
--     VALUES('Alho e Óleo', 'Molho, mussarela, alho, óleo e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)    
--     VALUES('Napolitano', 'Molho, mussarela, tomate, parmesão e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Marguerita', 'Molho, mussarela, tomate, manjericão e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Milho', 'Molho, mussarela, milho e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Calabresa', 'Molho, mussarela, calabresa, cebola, azeitona e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Milho com Bacon', 'Molho, mussarela, milho, bacon e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Presunto', 'Molho, mussarela, presunto e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Toscana', 'Molho, mussarela, presunto, tomate e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Lombo', 'Molho, mussarela, lombo e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Catupiry', 'Molho, mussarela, catupiry e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Palmito', 'Molho, mussarela, palmito e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Bacon', 'Molho, mussarela, bacon e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Crocante I', 'Molho, mussarela, calabresa, batata-palha e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Crocante II', 'Molho, mussarela, bacon, batata-palha e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Frango', 'Molho, mussarela, frango e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Portuguesa', 'Molho, mussarela, presunto, cebola, azeitona, ovo e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Parmegiana', 'Molho, mussarela, presunto, molho, parmesão e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Americana', 'Molho, mussarela, tomate, bacon, pimentão, palmito e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Hot-Dog', 'Molho, mussarela, vina, milho, ervilha, batata-palha e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Tradicionais');
 
-- -- 
-- -- PIZZAS Especiais 
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Atum', 'Molho, mussarela, atum, cebola e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Brasileira', ' Molho, mussarela, bacon, calabresa, cheddar, azeitona e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Caipira', ' Molho, mussarela, frango, milho,bacon e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Romanesca', ' Molho, mussarela, frango, milho, tomate, palmito e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Peruana', ' Molho, mussarela, atun, ervilha, cebola e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Queijos', ' Molho, mussarela, catupiry, parmesão e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Frango com Catupiry/Cheddar', ' Molho, mussarela, frango, catupiry/cheddar e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Especial', ' Molho, mussarela, calabresa, milho, ovo e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Lombo com Bacon', ' Molho, mussarela, lombo, bacon, cheddar e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Lombo com Champignon', ' Molho, mussarela, lombo, champignon, catupiry e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Paulista', ' Molho, mussarela, milho, ervilha, palmito e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Baiana', ' Molho, mussarela, calabresa, palmito, ovo, pimenta calabresa e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Especiais');
-- -- 
-- -- PIZZAS Premium 
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('A Moda', 'Molho, mussarela, champignon, pepperone, azeitona e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('A Moda II', ' Molho, mussarela, calabresa, tomate, ovo, milho, ervilha e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('A Moda da Casa I', ' Molho, mussarela, calabresa, presunto, bacon, cheddar e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('A Moda da Casa II', ' Molho, mussarela, lombo, champignon, bacon, ovo, catupiry, azeitona e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Imperial', ' Molho, mussarela, frango, palmito, bacon, cream cheese e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Salame', ' Molho, mussarela, salame, cheddar e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Pepperone', ' Molho, mussarela, pepperone, cream cheese e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Strogonofe de Carne', ' Molho, mussarela, estrogonofe de carne, champignon, batata-palha e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Strogonofe de Frango', ' Molho, mussarela, estrogonofe de frango, champignon, batata-palha e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Queijos', ' Molho, mussarela, provolone, parmesão, catupiry e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Queijos', ' Molho, mussarela, provolone, parmesão, catupiry, gongorzola e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Queijos', ' Molho, mussarela, provolone, parmesão, catupiry, gongorzola, cheddar e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Queijos', ' Molho, mussarela, provolone, parmesão, catupiry, gongorzola, cheddar, cream cheese e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Florença', ' Molho, mussarela, calabresa, bacon, ovos, tomate, parmesão, manjericão e orégano', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Do Cliente', 'Até 5 ingredientes', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Premium');
-- --  
-- -- 
-- -- PIZZAS Doces 
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Banana', 'Creme de leite, mussarela, banana e canela', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Banana com Chocolate', 'Creme de leite, mussarela, banana, chocolate preto ou branco', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Morango', 'Creme de leite, mussarela', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Confet', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Ele e Ela', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Brigadeiro', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Dois Amores', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Sensação', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Floresta negra', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Beijinho', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Sonho de Valsa', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Prestígio', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Chocolate Preto', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');
-- INSERT INTO produto(descricao, resumo, valor, medida, logo, associado_categoria_id, dtregistro, tipo)
--     VALUES('Chocolate Branco', 'não informado', '0.00', 'FR', 'produtos/100x100.jpg', (SELECT associado_categorias.id FROM associado_categorias INNER JOIN associado ON associado.id = associado_id INNER JOIN categoria ON categoria.id = categoria_id WHERE associado.nomefantasia='Pizzaria Dom Juan' AND categoria.descricao='PIZZAS'), NULL, 'Doces');


--PRECOS POR PRODUTO E TAMANHO
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '34,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Mussarela')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '29,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Mussarela')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '23,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Mussarela')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '17,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Mussarela')));

INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '34,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Alho e Óleo')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '29,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Alho e Óleo')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '23,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Alho e Óleo')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '17,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Alho e Óleo')));

INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '34,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Napolitano')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '29,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Napolitano')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '23,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Napolitano')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '17,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Napolitano')));

INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '34,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Marguerita')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '29,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Marguerita')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '23,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Marguerita')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '17,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Marguerita')));

INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '34,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Milho')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '29,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Milho')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '23,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Milho')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '17,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Milho')));

INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '34,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Calabresa')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '29,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Calabresa')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '23,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Calabresa')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '17,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Calabresa')));

INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '34,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Milho com Bacon')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '29,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Milho com Bacon')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '23,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Milho com Bacon')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '17,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Milho com Bacon')));
    
-- Especiais
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '36,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Atum')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '32,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Atum')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '28,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Atum')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '22,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Atum')));

INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '36,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Brasileira')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '32,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Brasileira')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '28,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Brasileira')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '22,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Brasileira')));

INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '36,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Caipira')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '32,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Caipira')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '28,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Caipira')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '22,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Caipira')));

INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '36,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Romanesca')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '32,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Romanesca')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '28,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Romanesca')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '22,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Romanesca')));


INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('4', '36,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Peruana')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('3', '32,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Peruana')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('2', '28,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Peruana')));
INSERT INTO produto_tamanho(tamanho, valor, dtregistro, produto_id)
    VALUES('1', '22,90', NULL, (SELECT id FROM produto WHERE descricao IN ('Peruana')));
