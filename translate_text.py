from translate import Translator

config = Translator(from_lang='english', to_lang='pt-br')

text = config.translate('world')

print(text)

