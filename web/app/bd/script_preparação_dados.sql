-- Identifica DOI Duplicado
-- SELECT id, doi, situacao
--     FROM Referencia
--     WHERE doi in(SELECT DISTINCT DOI
--                     FROM Referencia
--                     GROUP BY doi    
--                     HAVING Count(doi)>1)  
--      AND situacao = 'Pendente'               
--     ORDER BY DOI

-- Localiza Dados Faltantes
-- UPDATE Referencia SET situacao = 'Dados Incompletos' WHERE id in (
-- SELECT id, doi, situacao, titulo, autores, resumo
--     FROM Referencia
--     WHERE (titulo = '' or autores = '' or resumo='' or doi='')
--      AND situacao = 'Dados Incompletos'               
--     ORDER BY DOI

-- Classifica quanto a idade do artigo
-- SELECT id, doi, ano, situacao, titulo, autores, resumo
--     FROM Referencia
--     WHERE situacao = 'Pendente'               
--      AND ano<=2000
--    ORDER BY ano

