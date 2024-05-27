vim \
  -c 'hardcopy > output.ps' \
  -c quit constantes.ml

ps2pdf output.ps constantes.pdf
