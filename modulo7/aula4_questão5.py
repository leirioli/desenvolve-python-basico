with open('meus_livros.csv.', 'w', encoding= 'utf-8') as livros:
    livros.write("Título,Autor,Ano de publicação,Número de páginas\n")
    livros.write("1984,George Orwell,1949,328\n")
    livros.write("Cem Anos de Solidão,Gabriel García Márquez,1967,448\n")
    livros.write("O Pequeno Príncipe,Antoine de Saint-Exupéry,1943,96\n")
    livros.write("Orgulho e Preconceito,Jane Austen,1813,432\n")
    livros.write("O Senhor dos Anéis,J.R.R. Tolkien,1954,1178\n")
    livros.write("A Revolução dos Bichos,George Orwell,1945,152\n")
    livros.write("O Alquimista,Paulo Coelho,1988,208\n")
    livros.write("Crime e Castigo,Fiódor Dostoiévski,1866,544\n")
    livros.write("A Menina que Roubava Livros,Markus Zusak,2005,480\n")
    livros.write("O Nome do Vento,Patrick Rothfuss,2007,662\n")

print("Arquivo 'meus_livros.csv' criado com sucesso!")