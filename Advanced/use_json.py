import json
import os

os.chdir('Data')

result = []
with open('poet.song.20.json',encoding='utf-8') as f:
    poet_dic=json.load(f)
    print(type(poet_dic))

    for index, poet in enumerate(poet_dic):

        if index <5:
            print(index)
            print(poet)
            print(type(poet))
            print(poet['paragraphs'])
            result.append(poet)

    # print(result)


with open('output.json','w',encoding='utf-8') as f2:
    json.dump(result,f2,indent=4,ensure_ascii=False)
