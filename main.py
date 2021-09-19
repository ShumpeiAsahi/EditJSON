import json
#JSONファイルを開き辞書型にする
with open('gen1-jp.json','r',encoding="utf-8_sig") as data_file:
    data = json.load(data_file)

#特定のキーを削除
for element in data:
    if 'stage' in element:
        del element['stage']
    if 'base_stats' in element:
        del element['base_stats']
    if 'ev_yield' in element:
        del element['ev_yield']
    if 'catch-rate' in element:
        del element['catch-rate']
    if 'abilities' in element:
        del element['abilities']
    if 'items' in element:
        del element['items']
    if 'egg-group' in element:
        del element['egg-group']
    if 'exp-group' in element:
        del element['exp-group']

    if 'hatch-cycles' in element:
        del element['hatch-cycles']
    if 'items' in element:
        del element['items']
    if 'egg-group' in element:
        del element['egg-group']
    if 'exp-group' in element:
        del element['exp-group']

#削除した辞書をJSONファイルに上書き
with open('gen1-jp.json', 'w', encoding="utf-8_sig") as data_file:
    data = json.dump(data, data_file,indent=2,ensure_ascii=False)