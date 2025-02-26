# quicktranslate   
Translate to or from Spanish/English in the command line using the DeepL API.    

### to install   
The recommended installation method is via [pipx](https://github.com/pypa/pipx), which greatly improves the UX of installing and managing python CLI apps; it can be found in the repos of most major distributions. After it's been installed, you can install quicktranslate by executing this command within your terminal:   
```pipx install git+https://github.com/emzilia/quicktranslate.git```   

### to use   
```
Usage: trans [option] <word or phrase to translate in quotes>
Translates the quoted input text from Spanish to English or vice versa
or show API key usage.
  Options:
    -se		    Translates the quoted input text from Spanish to English
    -es		    Translates the quoted input text from English to Spanish
    -u, --usage	    Shows DeepL API key usage
    -h, --help	    Shows this help message
```   

### in action   
```
> $ trans -es "Please help, they keep me in a small box"
Por favor ayuda, me tienen en una pequeña caja
> $ trans -se "No te preocupes, esto sólo mejora"
Don't worry, it only gets better
```
