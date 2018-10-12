#JSONAPIの利用の確認

import json

json_data = {'Python':'python-izm.com','SearchEngine':('google.co.jp','yahoo.co.jp')}

print(type(json_data))

#indentを指定して、数値に応じたインデント表示をする
encode_json_data = json.dumps(json_data,indent=4)

print(encode_json_data)
print(type(encode_json_data))

#JSON文字列からPythonオブジェクト(ディクショナリ)へ変換する

decode_json_data = json.loads(encode_json_data)

print(decode_json_data)
print(type(decode_json_data))