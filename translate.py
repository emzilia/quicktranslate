#!/usr/bin/env python

import deepl, os, sys

# limits input to save on api calls, first argument determines which way
# the translation goes, es for English to Spanish or se for Spanish to English
def arg_check() -> str:
    if len(sys.argv) == 1:
        print(
            "Usage: tran se \"<word of phrase>\"\n\t"
            "Translates the quoted input text from Spanish to English\n"
            "       tran es \"<word or phrase>\"\n\t"
            "Translates the quoted input text from English to Spanish\n"
            "       tran usage\n\t"
            "Shows DeepL API key usage (no quotes)"
        )
        sys.exit(1)
    elif len(sys.argv) == 2:
        print(
            "Error: This program requires at least two arguments to "
            "function"
        )
        sys.exit(1)
    elif len(sys.argv) > 3:
        print(
            "Error: This program doesn't support more than one block "
            "of quotes at a time"
        )
        sys.exit(1)

    if sys.argv[1] == 'usage':
        flag: str = "USAGE"
    elif sys.argv[1] == 'se':
        flag: str = "EN-US"
    elif sys.argv[1] == 'es':
        flag: str = "ES"
    else:
        print(
            "Error: First arg must be 'se' or 'es' for translation to "
            "English or Spanish respectively"
        )
        sys.exit(1)

    return flag
   
# requires a DeepL API key, which are free to acquire, however you must
# provide billing information. Currently set as an env variable
def init_deepl():
    auth_key: str = os.environ["DEEPL_API_KEY"]
    translator = deepl.Translator(auth_key)
    return translator

# checks the usage of the DeepL free API calls
def api_check(translator) -> None:
    usage = translator.get_usage()
    if usage.any_limit_reached:
        print(
            "This DeepL API key has reached its usage limit."
        )
        sys.exit(1)
    else:
        print(
            f"Usage: {usage.character.count} / {usage.character.limit}"
        )
        sys.exit(1)

# based on the flag set by the first argument, text is translated as single
# words or as strings built by successive script args, API usage can
# also be shown
def trans_input(translator, flag) -> str:
    if flag == "USAGE":
        api_check(trans)
    newword: str = translator.translate_text(
        sys.argv[2],
        target_lang=flag
    )
    return newword

if __name__ == "__main__":
    flag: str = arg_check()
    trans = init_deepl()
    output: str = trans_input(trans, flag)

    print(output)
