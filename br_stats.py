import pandas as pd
import asyncio
import aiohttp
from playwright.sync_api import sync_playwright
from io import StringIO

times_serie_a = [
    "Athletico", "América-MG", "Atlético-MG", "Bahia", "Cuiabá", "Goiás",
    "Corinthians", "Flamengo", "Fluminense", "Grêmio", "Internacional",
    "Botafogo", "Palmeiras", "Santos", "São Paulo", "Cruzeiro",
    "Fortaleza", "Coritiba", "RB Bragantino", "Vasco"
]

tabela = pd.DataFrame(
    data = {
        'time': times_serie_a,
        'vitorias': len(times_serie_a)*[0],
        'empates': len(times_serie_a)*[0],
        'derrotas': len(times_serie_a)*[0],
        'gols_pro': len(times_serie_a)*[0.0],
        'gols_contra': len(times_serie_a)*[0.0],
    }
)

headers = {
    "Host": "api.sofascore.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://www.sofascore.com/",
    "Origin": "https://www.sofascore.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers",
}

def get_classfc():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        url = 'https://ge.globo.com/futebol/brasileirao-serie-a/'
        page.goto(url)
        page.wait_for_selector('div.classificacao__pontos-corridos')

        content = page.content()
        browser.close()
    # Wrap the HTML content in StringIO objects
    content_io = StringIO(content)

    # Read the HTML content using pd.read_html
    df_list = pd.read_html(content_io)
    # Now, you can access the DataFrames from df_list
    df_times = df_list[0]
    df_pontos = df_list[1]
    # Concatenate them vertically
    result = pd.concat([df_times, df_pontos], axis=1)
    result.set_index('Classificação', inplace=True, drop=True)
    result.index.name = None
    result.drop(columns=['Classificação.2', 'ÚLT. JOGOS', '%'], inplace=True)
    result.rename(
        columns={
        'Classificação.1': 'Times', 'P': 'pontos', 'J': 'jogos', 'V': 'vitorias', 'E': 'empates', 'D': 'derrotas', 'GP': 'gols_pro', 'GC': 'gols_contra', 'SG': 'saldo_gols'
        }, inplace=True
        )
    result['Times'] = result['Times'].str[:-3]

    return result


def count_round(round, tabela, criterio):
    for index, row in round.iterrows():
        dict_criterio = {
            'xg': abs(row[f'xg_result']) > 0.5 and max(row['xg_home'], row['xg_away']) > 0.5,
            'gc': abs(row[f'{criterio}_result']) != 0.0
        }
        if dict_criterio[criterio]:
            if row[f'{criterio}_result'] > 0:
                tabela.loc[tabela['time'] == row['home'], 'vitorias'] += 1
                tabela.loc[tabela['time'] == row['away'], 'derrotas'] += 1
            else:
                tabela.loc[tabela['time'] == row['away'], 'vitorias'] += 1
                tabela.loc[tabela['time'] == row['home'], 'derrotas'] += 1
        else:
            tabela.loc[tabela['time'] == row['home'], 'empates'] += 1
            tabela.loc[tabela['time'] == row['away'], 'empates'] += 1
        tabela.loc[tabela['time'] == row['home'], 'gols_pro'] += row[f'{criterio}_home']
        tabela.loc[tabela['time'] == row['home'], 'gols_contra'] += row[f'{criterio}_away']
        tabela.loc[tabela['time'] == row['away'], 'gols_pro'] += row[f'{criterio}_away']
        tabela.loc[tabela['time'] == row['away'], 'gols_contra'] += row[f'{criterio}_home']
    tabela[f'saldo_{criterio}'] = tabela['gols_pro'] - tabela['gols_contra']
    tabela['pontos'] = 3*tabela['vitorias'] + 1*tabela['empates']
    tabela['jogos'] = tabela['vitorias'] + tabela['empates'] + tabela['derrotas']
    tabela.sort_values(['pontos', 'vitorias', f'saldo_{criterio}', 'gols_pro'], ascending=False, ignore_index=True, inplace=True)
    tabela.index += 1

    return tabela

async def get_stats_match(session, id):
    url_stats_base = f'https://api.sofascore.com/api/v1/event/{id}/statistics'
    
    try:
        async with session.get(url_stats_base, headers=headers) as response:
            data_raw = await response.json()
            
            if data_raw:
                xg_raw = data_raw['statistics'][0]['groups'][0]['statisticsItems'][0]
                xg_home = xg_raw['homeValue']
                xg_away = xg_raw['awayValue']
                gc_raw = data_raw['statistics'][0]['groups'][4]['statisticsItems'][0]
                gc_home = gc_raw['homeValue']
                gc_away = gc_raw['awayValue']
                return xg_home, xg_away, gc_home, gc_away
    except aiohttp.ClientResponseError as e:
        print(f'Stats not found for match_id: {id}')
        pass

async def get_round_data(session, round):
    print(f'Parsing data from round {round}...')
    url_rounds = f'https://api.sofascore.com/api/v1/unique-tournament/325/season/48982/events/round/{round}'
    async with session.get(url_rounds, headers=headers) as response:
        data_raw = await response.json()
        round_data = []

        for game in data_raw['events']:
            try:
                round_data.append({
                    'round': round,
                    'game_id': game['id'],
                    'home': game['homeTeam']['shortName'],
                    'home_score': game['homeScore']['current'],
                    'away': game['awayTeam']['shortName'],
                    'away_score': game['awayScore']['current'],
                    'status': game['status']['code']
                })
            except:
                pass
        xg_data = await asyncio.gather(*[get_stats_match(session, game['game_id']) for game in round_data])

        for i, game in enumerate(round_data):
            round_data[i]['xg_home'], round_data[i]['xg_away'], round_data[i]['gc_home'], round_data[i]['gc_away'] = xg_data[i]
            round_data[i]['xg_result'] = round_data[i]['xg_home'] - round_data[i]['xg_away']
            round_data[i]['gc_result'] = round_data[i]['gc_home'] - round_data[i]['gc_away']

        df = pd.DataFrame(round_data)
        return df
    

async def main():
    global tabela
    async with aiohttp.ClientSession() as session:
        for round in range(1, 27):
            round_df = await get_round_data(session, round)
            tabela = count_round(round_df, tabela, 'gc')
        print(tabela)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    #print(get_classfc())