#!/usr/bin/env python

import deepl, os, sys

# first argument determines which way the translation goes, 'es' for english
# to spanish or 'se' for spanish to english, 'usage' shows api key usage.
def arg_check() -> str:
    if len(sys.argv) == 1:
        print(
            "Usage: tran se \"<word or phrase>\"\n\t"
            "Translates the quoted input text from Spanish to English\n"
            "       tran es \"<word or phrase>\"\n\t"
            "Translates the quoted input text from English to Spanish\n"
            "       tran usage\n\t"
            "Shows DeepL API key usage (no quotes)"
        )
        sys.exit(1)
    elif len(sys.argv) == 2 and sys.argv[1] != 'usage':
        print(
            "Error: If not using 'usage', two arguments are required."
        )
        sys.exit(1)
    elif len(sys.argv) > 3:
        print(
            "Error: This program doesn't support more than one block "
            "of quotes at a time"
        )
        sys.exit(1)

    match sys.argv[1]:
        case 'usage':
            flag: str = "USAGE"
        case 'se':
            flag: str = "EN-US"
        case 'es':
            flag: str = "ES"
        case _:
            print(
                "Error: First arg must be 'se' or 'es' for translation to "
                "English or Spanish respectively.\n'usage' to see api key usage."
            )
            sys.exit(1)

    return flag
   
# requires a DeepL api key, which is free to acquire. checks api usage and
# closes if it's reached its limit, shows usage data if flag is set
# set as an env variable
def init_deepl(flag):
    auth_key: str = os.environ["DEEPL_API_KEY"]
    translator = deepl.Translator(auth_key)
    api_check(translator, flag)
    return translator

# checks the usage of the DeepL api calls
def api_check(translator, flag) -> None:
    usage = translator.get_usage()
    if usage.any_limit_reached:
        print(
            "Error: This DeepL API key has reached its usage limit."
        )
        sys.exit(1)
    if flag == 'USAGE':
        print(
            f"Usage: {usage.character.count} / {usage.character.limit} "
            "characters"
        )
        sys.exit(1)

# text is translated based on the flag previously set.
def trans_input(translator, flag) -> str:
    newword: str = translator.translate_text(
        sys.argv[2],
        target_lang=flag
    )
    return newword

if __name__ == "__main__":
    flag: str = arg_check()
    trans = init_deepl(flag)
    output: str = trans_input(trans, flag)

    print(output)
