# Estatísticas do Campeonato Brasileiro de 2023
Esse é um estudo de desempenho das equipes do campeonato brasileiro.

## Introdução
A dualidade entre desempenho e resultado é um conceito fundamental no mundo do esporte, principalmente o futebol. Ela reflete a distinção entre a forma como uma equipe joga (desempenho) e o resultado final do jogo (resultado). Essa dualidade é importante porque o desempenho e o resultado nem sempre estão alinhados, o que pode levar a análises e debates complexos sobre o valor real de uma equipe, um jogador ou de uma comissão técnica.

Vamos explorar essa dualidade em relação a uma partida de futebol:

Desempenho:
O desempenho se refere à maneira como uma equipe joga durante uma partida. Isso envolve aspectos como a qualidade do passe, a posse de bola, a movimentação tática, a criação de oportunidades de gol (grandes chances) e gols esperados (xG).
Mesmo que o resultado seja uma derrota, um bom desempenho pode ser elogiado (embora dificilmente aconteça).

Resultado:
O resultado é o marcador final da partida, que determina quem venceu, perdeu ou empatou.
O resultado é, em última análise, o que importa em termos de classificação em uma competição e é o que os torcedores frequentemente lembram. É comum dizer que "o que importa é vencer".

## Metodologia do estudo


Para medir o desempenho dos times no Campeonato Brasileiro, proponho dois métodos alternativos para contabilizar vitórias/empates/derroas para cada equipe:
- Comparação entre grandes chances criadas por ambas equipes durante o jogo. Exemplo, jogo da 26ª rodada: Palmeiras x Santos. Resultado final: Palmeiras 1 x 2 Santos. Resultado final por grandes chances criadas: Palmeiras 4 x 4 Santos. Nesse caso, o resultado por desempenho seria um empate, mesmo que o resultado real tenha sido diferente.
- Comparação entre gols esperados (xG) por ambas equipes durante um jogo. Exemplo, jogo da 1ª rodada: Botafogo x São Paulo. Resultado final: Botafogo 2 x 1 São Paulo. Resultado final por gols esperados (xG): Botafogo 0.89 x 2.03 São Paulo. Nesse caso, o resultado por desempenho seria uma vitória do São Paulo, ainda que o resultado real tenha sido oposto (vitória do Botafogo). Detalhe: nesse critério, só considero algo diferente de empate quando a diferença de gols esperados (xG) entre as equipes seja maior que 0,5.

## Coleta e tratamento de dados
Os dados foram coletados via API do site SofaScore, e seguiu o fluxo abaixo:
### Passo 1: Identificação dos Jogos da Rodada
Inicialmente, é realizada uma solicitação à API para identificar os jogos realizados em uma rodada específica do campeonato. Para cada rodada, a resposta da API contém os IDs dos jogos daquela rodada.
### Passo 2: Solicitações Assíncronas para Dados Estatísticos
Em seguida, são iniciadas 10 solicitações assíncronas para obter os dados estatísticos de cada jogo da rodada. Isso permite que o projeto seja eficiente e não espere cada solicitação terminar antes de iniciar a próxima. Cada solicitação busca informações detalhadas sobre gols marcados, grandes chances criadas e gols esperados (xG).
### Passo 3: Tratamento dos Dados de Cada Jogo
Com os dados estatísticos em mãos, o sistema realiza o tratamento dos dados de cada jogo da rodada. Essa etapa envolve a análise e o processamento dos dados brutos para calcular o desempenho de cada equipe, baseada nas propostas descritas na metodologia (grandes chances e gols esperados).
### Passo 4: Contabilização de Resultados por Desempenho
Aqui é realizada a contabilização de resultados por desempenho da rodada. Isso determinará quem ganhou/perdeu/empatou na rodada, bem como seus respectivos gols esperados pró/contra, saldo de grandes chances criadas etc.
### Passo 5: Repetição do Ciclo para Cada Rodada
O processo é repetido para cada rodada do campeonato. Isso garante que o sistema analise o desempenho de todas as equipes em todas as rodadas.



# Classificação por grandes chances criadas
## Rodada 26

|   Classificação | Time         |   Vitórias |   Empates |   Derrotas |   Gols_pro |   Gols_contra |   Saldo_gc |   Pontos |   Jogos |
|---------:|:-------------|-----------:|---------:|-----------:|------------:|--------------:|----------:|--------:|--------:|
|         1 | <img src="https://api.sofascore.app/api/v1/team/1963/image" width="20" height="20">Palmeiras    |         18 |        5 |          3 |          70 |           39  |        31 |      59 |     26 |
|         2 | <img src="https://api.sofascore.app/api/v1/team/1967/image" width="20" height="20">Athletico    |         17 |        2 |          7 |          63 |           35  |        28 |      53 |     26 |
|         3 | <img src="https://api.sofascore.app/api/v1/team/2020/image" width="20" height="20">Fortaleza    |         15 |        2 |          9 |          63 |           45  |        18 |      47 |     26 |
|         4 | <img src="https://api.sofascore.app/api/v1/team/1999/image" width="20" height="20">RB Bragantino|         13 |        4 |          9 |          54 |           47  |         7 |      43 |     26 |
|         5 | <img src="https://api.sofascore.app/api/v1/team/1981/image" width="20" height="20">São Paulo     |         11 |       10 |          5 |          52 |           35  |        17 |      43 |     26 |
|         6 | <img src="https://api.sofascore.app/api/v1/team/5926/image" width="20" height="20">Grêmio       |         13 |        3 |         10 |          65 |           63  |         2 |      42 |     26 |
|         7 | <img src="https://api.sofascore.app/api/v1/team/1974/image" width="20" height="20">Vasco        |         12 |        5 |          9 |          52 |           40  |        12 |      41 |     26 |
|         8 | <img src="https://api.sofascore.app/api/v1/team/1977/image" width="20" height="20">Atlético-MG  |         12 |        4 |         10 |          48 |           42  |         6 |      40 |     26 |
|         9 | <img src="https://api.sofascore.app/api/v1/team/5981/image" width="20" height="20">Flamengo     |         11 |        6 |          9 |          66 |           47  |        19 |      39 |     26 |
|        10 | <img src="https://api.sofascore.app/api/v1/team/1957/image" width="20" height="20">Corinthians   |         11 |        5 |         10 |          33 |           38  |        -5 |      38 |     26 |
|        11 |<img src="https://api.sofascore.app/api/v1/team/1958/image" width="20" height="20"> Botafogo     |          9 |        8 |          9 |          56 |           56  |         0 |      35 |     26 |
|        12 | <img src="https://api.sofascore.app/api/v1/team/1961/image" width="20" height="20">Fluminense   |          9 |        8 |          9 |          48 |           52  |        -4 |      35 |     26 |
|        13 | <img src="https://api.sofascore.app/api/v1/team/1954/image" width="20" height="20">Cruzeiro     |          9 |        6 |         11 |          48 |           44  |         4 |      33 |     26 |
|        14 | <img src="https://api.sofascore.app/api/v1/team/49202/image" width="20" height="20">Cuiabá       |          9 |        6 |         11 |          34 |           43  |       -9 |      33 |     26 |
|        15 | <img src="https://api.sofascore.app/api/v1/team/1968/image" width="20" height="20">Santos       |          8 |        5 |         13 |          45 |           60  |       -15 |      29 |     26 |
|        16 | <img src="https://api.sofascore.app/api/v1/team/1955/image" width="20" height="20">Bahia        |          8 |        4 |         14 |          57 |           73  |       -16 |      28 |     26 |
|        17 | <img src="https://api.sofascore.app/api/v1/team/1960/image" width="20" height="20">Goiás        |          8 |        2 |         16 |          37 |           49  |       -12 |      26 |     26 |
|        18 | <img src="https://api.sofascore.app/api/v1/team/1982/image" width="20" height="20">Coritiba     |          6 |        6 |         14 |          34 |           70  |       -36 |      24 |     26 |
|        19 | <img src="https://api.sofascore.app/api/v1/team/1966/image" width="20" height="20">Internacional |          6 |        5 |         15 |          35 |           54  |       -19 |      23 |     26 |
|        20 | <img src="https://api.sofascore.app/api/v1/team/1973/image" width="20" height="20">América-MG   |          6 |        2 |         18 |          40 |           68  |       -28 |      20 |     26 |

# Classificação por gols esperados (xG)
## Rodada 26

|   Classificação | Time                    |   Vitórias |   Empates |   Derrotas |   Gols_pro |   Gols_contra |   Saldo_xg |   Pontos |   Jogos |
|--------------:|:------------------------|-----------:|---------:|-----------:|------------:|--------------:|-----------:|--------:|--------:|
|             1 | <img src="https://api.sofascore.app/api/v1/team/1963/image" width="20" height="20"> Palmeiras      |        14 |        7 |          5 |       38.80 |         27.82 |      10.98 |      49 |     26 |
|             2 | <img src="https://api.sofascore.app/api/v1/team/1981/image" width="20" height="20"> São Paulo      |        13 |        6 |          7 |       36.75 |         27.53 |       9.22 |      45 |     26 |
|             3 | <img src="https://api.sofascore.app/api/v1/team/1999/image" width="20" height="20"> RB Bragantino  |        11 |        9 |          6 |       38.37 |         29.73 |       8.64 |      42 |     26 |
|             4 | <img src="https://api.sofascore.app/api/v1/team/1967/image" width="20" height="20"> Athletico      |        10 |       11 |          5 |       38.00 |         29.77 |       8.23 |      41 |     26 |
|             5 | <img src="https://api.sofascore.app/api/v1/team/2020/image" width="20" height="20"> Fortaleza      |         9 |       14 |          3 |       40.04 |         29.22 |      10.82 |      41 |     26 |
|             6 | <img src="https://api.sofascore.app/api/v1/team/1954/image" width="20" height="20"> Cruzeiro       |        11 |        6 |          9 |       32.59 |         31.47 |       1.12 |      39 |     26 |
|             7 | <img src="https://api.sofascore.app/api/v1/team/1977/image" width="20" height="20"> Atlético-MG    |        10 |        9 |          7 |       31.67 |         26.98 |       4.69 |      39 |     26 |
|             8 | <img src="https://api.sofascore.app/api/v1/team/1961/image" width="20" height="20"> Fluminense    |        10 |        7 |          9 |       35.51 |         33.47 |       2.04 |      37 |     26 |
|             9 | <img src="https://api.sofascore.app/api/v1/team/5981/image" width="20" height="20"> Flamengo      |         9 |       10 |          7 |       35.81 |         35.68 |       0.13 |      37 |     26 |
|            10 | <img src="https://api.sofascore.app/api/v1/team/1958/image" width="20" height="20"> Botafogo      |         9 |        9 |          8 |       35.14 |         31.01 |       4.13 |      36 |     26 |
|            11 | <img src="https://api.sofascore.app/api/v1/team/49202/image" width="20" height="20"> Cuiabá        |         7 |       12 |          7 |       26.83 |         28.29 |      -1.46 |      33 |     26 |
|            12 | <img src="https://api.sofascore.app/api/v1/team/1960/image" width="20" height="20"> Goiás        |         7 |       10 |          9 |       26.29 |         31.62 |      -5.33 |      31 |     26 |
|            13 | <img src="https://api.sofascore.app/api/v1/team/1957/image" width="20" height="20"> Corinthians   |         7 |        9 |         10 |       26.44 |         34.93 |      -8.49 |      30 |     26 |
|            14 | <img src="https://api.sofascore.app/api/v1/team/5926/image" width="20" height="20"> Grêmio      |         6 |       12 |          8 |       34.85 |         38.22 |      -3.37 |      30 |     26 |
|            15 | <img src="https://api.sofascore.app/api/v1/team/1955/image" width="20" height="20"> Bahia       |         8 |        5 |         13 |       34.60 |         39.09 |      -4.49 |      29 |     26 |
|            16 | <img src="https://api.sofascore.app/api/v1/team/1974/image" width="20" height="20"> Vasco       |         7 |        8 |         11 |       34.36 |         33.61 |       0.75 |      29 |     26 |
|            17 | <img src="https://api.sofascore.app/api/v1/team/1968/image" width="20" height="20"> Santos      |         6 |        9 |         11 |       30.21 |         37.06 |      -6.85 |      27 |     26 |
|            18 | <img src="https://api.sofascore.app/api/v1/team/1973/image" width="20" height="20"> América-MG  |         5 |       10 |         11 |       33.38 |         40.55 |      -7.17 |      25 |     26 |
|            19 | <img src="https://api.sofascore.app/api/v1/team/1966/image" width="20" height="20"> Internacional |         3 |        7 |         16 |       30.21 |         37.06 |      -6.85 |      27 |     26 |
|            20 | <img src="https://api.sofascore.app/api/v1/team/1982/image" width="20" height="20"> Coritiba  |         5 |       10 |         11 |       33.38 |         40.55 |      -7.17 |      25 |     26 |

