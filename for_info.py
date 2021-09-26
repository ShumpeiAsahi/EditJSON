import json
#JSONファイルを開き辞書型にする

for i in range(1,9):
        
    with open(f'gen{i}-jp.json','r',encoding="utf-8_sig") as data_file:
        data = json.load(data_file)

    #特定のキーを削除
    for element in data:
        if 'stage' in element:
            del element['stage']
        if 'ev_yield' in element:
            del element['ev_yield']
        if 'catch-rate' in element:
            del element['catch-rate']
        if 'items' in element:
            del element['items']
        if 'egg-group' in element:
            del element['egg-group']
        if 'exp-group' in element:
            del element['exp-group']

        if 'hatch-cycles' in element:
            del element['hatch-cycles']
        if 'height' in element:
            del element['height']
        if 'weight' in element:
            del element['weight']
        if 'color' in element:
            del element['color']

        if 'evolutions' in element:
            del element['evolutions']
        if 'tms' in element:
            del element['tms']
        if 'trs' in element:
            del element['trs']
        if 'galar_dex' in element:
            del element['galar_dex']
        
        if 'gender-ratio' in element:
            del element['gender-ratio']
        if 'level_up_moves' in element:
            del element['level_up_moves']
        if 'egg_moves' in element:
            del element['egg_moves']

    #削除した辞書をJSONファイルに上書き
    with open(f'gen{i}-jp.json', 'w', encoding="utf-8_sig") as data_file:
        data = json.dump(data, data_file,indent=2,ensure_ascii=False)