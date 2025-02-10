import csv

musicas_mais_tocadas = {ano: None for ano in range(2012, 2023)}

with open('spotify-2023.csv', mode='r', encoding='latin-1') as arquivo:
    leitor = csv.reader(arquivo)
    cabecalho = next(leitor)

    for linha in leitor:
        try:
            track_name = linha[0].strip()
            artist_name = linha[1].strip()
            released_year = int(linha[3].strip())
            streams = int(linha[8].strip())

            if 2012 <= released_year <= 2022:
                if ',' not in track_name and '"' not in track_name and ',' not in artist_name and '"' not in artist_name:
                    if (musicas_mais_tocadas[released_year] is None or
                        streams > musicas_mais_tocadas[released_year][3]):
                        musicas_mais_tocadas[released_year] = [track_name, artist_name, released_year, streams]
        except (ValueError, IndexError):
            continue

lista_final = [musicas_mais_tocadas[ano] for ano in range(2012, 2023) if musicas_mais_tocadas[ano] is not None]

for musica in lista_final:
    print(musica)