#デフォルトであるモジュールと同一ファイル名の時は、読み込めない
import configparser

inifile = configparser.ConfigParser()
inifile.read('config.ini','UTF-8')

print(inifile.get('settings', 'host'))
print(inifile.get('settings', 'port'))

print(inifile.get('system', 'os'))
print(inifile.get('system', 'version'))
print(inifile.get('system', 'path'))

print(inifile.get('user', 'name'))
print(inifile.get('user', 'password'))
print(inifile.get('user', 'mail'))