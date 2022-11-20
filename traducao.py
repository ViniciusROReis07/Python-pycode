from translate import Translator

s = Translator(from_lang="pt-br", to_lang="de")

res = s.translate("Ola, tudo bem?")

print(res)