#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to run pytest on a given file with minimal output
run_tests() {
  local file=$1
  echo "Executando testes no arquivo: $file"
  pytest --tb=no --disable-warnings "$file"/*.py
  echo '-----------------------------------------------------'
}

    run_tests 02_Funcoes_e_TDD/
    run_tests 03_variaveis_e_operadores_matematicos/
    run_tests 04_operadores_logicos_e_condicoes/
    run_tests 05_Listas,_tuplas_e_lacos_de_repeticao/
    run_tests 06_Listas_continuacao/
    run_tests 07_Exercicios/
  # run_tests 08_Strings_random/
  # run_tests 09_Dicionários/
  # run_tests 10_Introducao_a_funcoes/
  # run_tests 11_Funcoes_e_parametros_avancados/
  # run_tests 12_Funcoes_e_imports/
  # run_tests 13_exercicios_leetcode/
  # run_tests 14_manipulacao_de_datas/
  # run_tests 15_manipulacao_de_arquivos/
  # run_tests 16_json,XML,CSV/
  # run_tests 17_TDD/
  # run_tests 18_exercicios/
  # run_tests XX_extras/

echo "All tests ran successfully"

