# github_youdao_anki

This Python tool can be use to convert word list exported from youdao dict (xml format) for Anki import (text format). 
The output file name is [YOUR_XML_NAME]_extracted.txt
As per Anki, the output file must be plain text with UTF-8 format.
';' is used as field seperator.
For more importing related info, please check https://docs.ankiweb.net/#/importing

Basic prerequisites: python3 and lxml need to be installed.

You can just run the following command in your shell cmd line:
  convertor_cli.py [FULL PATH OF YOUR XML FILE EXPORTED FROM YOUDAO DICT]

If you want to run GUI version of the program (convertor_gui.py), PyQt5 needs to be installed as a prerequisite. 

Anyway, cli version is sufficient to fullfil the job and "convertor.py" is the only file that you need to run the command.
