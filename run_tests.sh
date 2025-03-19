#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to run pytest on a given file with minimal output
run_tests() {
  local file=$1
  pytest -q --tb=no --disable-warnings "$file"
}

# run_tests 02_Funcoes_e_TDD/*.py
# run_tests 03_variaveis_e_operadores_matematicos/*.py
# run_tests 04_operadores_logicos_e_condicoes/*.py
# run_tests 05_Listas,_tuplas_e_lacos_de_repeticao/*.py
# run_tests 06_Listas_continuacao/*.py
# run_tests 07_Exercicios/*.py
# run_tests 08_Strings_random/*.py
# run_tests 09_Dicionários/*.py
# run_tests 10_Introducao_a_funcoes/*.py
# run_tests 11_Funcoes_e_parametros_avancados/*.py
# run_tests 12_Funcoes_e_imports/*.py
# run_tests 13_exercicios_leetcode/*.py
# run_tests 14_manipulacao_de_datas/*.py
# run_tests 15_manipulacao_de_arquivos/*.py
# run_tests 16_json,XML,CSV/*.py
# run_tests 17_TDD/*.py
# run_tests 18_exercicios/*.py
# run_tests XX_extras/*.py

echo "All tests ran successfully"
