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
            "Translates the input text from English to Spanish"
        )
        sys.exit(1)
    elif len(sys.argv) > 20:
        print("Error: This program doesn't support more than 20 "
            "words at a time.")
        sys.exit(1)

    if sys.argv[1] == 'se':
        flag = "EN-US"
    elif sys.argv[1] == 'es':
        flag = "ES"
    else:
        print("Error: First arg must be 'se' or 'es' for translation to "
            "English or Spanish respectively")
        sys.exit(1)

    return flag
   
# requires a DeepL API key, which are free to acquire, however you must
# provide billing information. Currently set as an env variable
def init_deepl():
    auth_key = os.environ["DEEPL_API_KEY"]
    translator = deepl.Translator(auth_key)
    return translator

# based on the flag set by the first argument, text is translated as single
# words or as strings built by successive script args
def trans_input(translator, flag):
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

    output = trans_input(trans, flag)

    print(output)
