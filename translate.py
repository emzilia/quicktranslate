#!/usr/bin/env python

import os, sys

# check if deepl api is installed, if not exit
try:
    import deepl
except ImportError:
    print("Error: Script requires pip packages that are missing: deepl")
    sys.exit(1)

# first argument determines which way the translation goes, 'es' for english
# to spanish or 'se' for spanish to english, 'usage' shows api key usage.
def arg_check(trans) -> str:
    output = ''
    try:
        option = sys.argv[1]
    except IndexError:
        print_help()
        sys.exit(1)
    try:
        text: str = sys.argv[2]
    except IndexError:
        print_help()
        sys.exit(1)

    if len(sys.argv) == 1:
        print_help()
    elif len(sys.argv) == 2:
        if option == '-h' or option == '--help':
            print_help()
        if option == '-u':
            print_usage(trans)
    elif len(sys.argv) == 3:
        if option == '-se':
            flag: str = "EN-US"
            output = trans_input(trans, flag, text)
        elif option == '-es':
            flag: str = "ES"
            output = trans_input(trans, flag, text)
    elif len(sys.argv) > 3:
        print(
            "Error: This script doesn't support more than one block "
            "of quotes at a time"
        )
        sys.exit(1)

    return output
   
# requires a DeepL api key, which is free to acquire. checks api usage and
# closes if it's reached its limit, shows usage data if flag is set
# set as an env variable
def init_deepl():
    auth_key: str = os.environ["DEEPL_API_KEY"]
    translator = deepl.Translator(auth_key)
    return translator

# text is translated based on the flag previously set.
def trans_input(translator, flag, text) -> str:
    output: str = translator.translate_text(
        text,
        target_lang=flag
    )
    return output

# checks the usage of the DeepL api calls
def print_usage(translator) -> None:
    usage = translator.get_usage()
    if usage.any_limit_reached:
        print(
            "Error: This DeepL API key has reached its usage limit."
        )
        sys.exit(1)
    print(
            f"Usage: {usage.character.count} / {usage.character.limit} "
            "characters"
    )
    sys.exit(1)

def print_help() -> None:
    print(
        "Usage: tran [option] <word or phrase to translate in quotes>\n"
        "Translates the quoted input text from Spanish to English or vice versa\n"
        "or show API key usage.\n"
        "  Options:\n"
        "    -se\t\t"
        "    Translates the quoted input text from English to Spanish\n"
        "    -es\t\t"
        "    Translates the quoted input text from English to Spanish\n"
        "    -u, --usage\t"
        "    Shows DeepL API key usage\n"
        "    -h, --help\t"
        "    Shows this help message\n"
    )
    sys.exit(1)

if __name__ == "__main__":
    trans = init_deepl()
    output = arg_check(trans)

    print(output)
