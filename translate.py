#!/usr/bin/env python

import deepl, os, sys

# limits input to save on api calls, first argument determines which way
# the translation goes, es for English to Spanish or se for Spanish to English
def arg_check():
    if len(sys.argv) == 1:
        print(
            "Usage: tran se <word of phrase>\n\t"
            "Translates the input text from Spanish to English\n"
            "       tran es <word or phrase>\n\t"
            "Translates the input text from English to Spanish\n\n"
            "       tran usage\n\t"
            "Shows DeepL API key usage"
        )
        sys.exit(1)
    elif len(sys.argv) > 20:
        print("Error: This program doesn't support more than 20 "
            "words at a time.")
        sys.exit(1)

    if sys.argv[1] == 'usage':
        flag = "USAGE"
    elif sys.argv[1] == 'se':
        flag = "EN-US"
    elif sys.argv[1] == 'es':
        flag = "ES"
    else:
        print("Error: First arg must be 'se' or 'es' for translation to "
            "English or Spanish respectively")
        sys.exit(1)

    return flag
   
# checks the usage of the DeepL free API calls
def api_check(translator):
    usage = translator.get_usage()
    if usage.any_limit_reached:
        print("This DeepL API key has reached its usage limit.")
        sys.exit(1)
    else:
        print(f"Usage: {usage.character.count} / {usage.character.limit}")
        sys.exit(1)

# requires a DeepL API key, which are free to acquire, however you must
# provide billing information. Currently set as an env variable
def init_deepl():
    auth_key = os.environ["DEEPL_API_KEY"]
    translator = deepl.Translator(auth_key)
    return translator

# based on the flag set by the first argument, text is translated as single
# words or as strings built by successive script args, API usage can
# also be shown
def trans_input(translator, flag):
    if flag == "USAGE":
        api_check(trans)
    if len(sys.argv) == 3:
        newword = translator.translate_text(sys.argv[2],
                                                target_lang=flag)
        return newword
    else:
        phrase = ''
        for word in sys.argv[2:]:
            phrase += word + ' '
        newphrase = translator.translate_text(phrase, 
                                              target_lang=flag)
        return newphrase

if __name__ == "__main__":
    flag = arg_check()

    trans = init_deepl()

    if flag == "USAGE":
        api_check(trans)

    output = trans_input(trans, flag)

    print(output)
