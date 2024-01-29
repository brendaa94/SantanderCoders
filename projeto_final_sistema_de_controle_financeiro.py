{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [
        "sB2xeWy5Xnit",
        "xNb_q1FaOi6t",
        "sW9skrIuO6Y_",
        "2E5P-rvS7pDc",
        "2yCiEPaN70TY",
        "scRhb5YT8GYm",
        "q-Ot08Yx8Qeg",
        "nUyaWb_5PDws",
        "MRo92_hpPMjJ",
        "dihGyqA_t52s",
        "uh4niwJCOPEV"
      ],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/brendaa94/SantanderCoders/blob/main/projeto_final_sistema_de_controle_financeiro.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Deverá ser desenvolvido um sistema para controle financeiro que receba as movimentações e as armazena em um arquivo csv ou json.\n",
        "\n",
        "O sistema deverá ser capaz de realizar as seguintes operações:\n",
        "\n",
        "---\n",
        "- Deem um nome criativo para a aplicação de vocês"
      ],
      "metadata": {
        "id": "6iPwvWWzOWRV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Projeto Final - Sistema de Controle Financeiro"
      ],
      "metadata": {
        "id": "xT7hQcg-OTK3"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Popular Registro"
      ],
      "metadata": {
        "id": "sB2xeWy5Xnit"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pip install Faker"
      ],
      "metadata": {
        "id": "EgYFkDfsR8EA",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9a47bd8f-91bc-47e6-c60b-a954174b0ef1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting Faker\n",
            "  Downloading Faker-22.6.0-py3-none-any.whl (1.7 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.7/1.7 MB\u001b[0m \u001b[31m9.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil>=2.4 in /usr/local/lib/python3.10/dist-packages (from Faker) (2.8.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.4->Faker) (1.16.0)\n",
            "Installing collected packages: Faker\n",
            "Successfully installed Faker-22.6.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from faker import Faker\n",
        "from datetime import datetime, timedelta\n",
        "import csv\n",
        "import json\n",
        "\n",
        "registros = [['id', 'Operação', 'Dia', 'Mês', 'Ano', 'Valor', 'Montante']]\n",
        "id_counter = 0"
      ],
      "metadata": {
        "id": "8dLQROR1o9ad"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Popular Registros\n",
        "for elemento in range(25):\n",
        "    id_counter += 1\n",
        "    fake = Faker()\n",
        "    operacao = fake.random_element(elements=('Receita', 'Despesa', 'Investimento'))\n",
        "    data = fake.date_between_dates(date_start=datetime(2023, 1, 1), date_end=datetime(2024, 12, 31))\n",
        "    valor = fake.random_int(min = 0, max = 5000)\n",
        "    if operacao == 'Despesa':\n",
        "      valor = -abs(valor)\n",
        "    novo_registro = [id_counter, operacao, data.strftime('%d'), data.strftime('%m'), data.strftime('%Y'), valor, 0.0]\n",
        "    registros.append(novo_registro)"
      ],
      "metadata": {
        "id": "I5YmGmQjsTIz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Verificando a base de dados\n",
        "for i in registros:\n",
        "  print(i)"
      ],
      "metadata": {
        "id": "0wYYqrQOYATz",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "91b358ba-c61c-47a7-85b8-9c3d1ff4f214"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['id', 'Operação', 'Dia', 'Mês', 'Ano', 'Valor', 'Montante']\n",
            "[1, 'Investimento', '07', '09', '2024', 3623, 0.0]\n",
            "[2, 'Receita', '26', '03', '2023', 339, 0.0]\n",
            "[3, 'Receita', '20', '08', '2024', 3144, 0.0]\n",
            "[4, 'Receita', '15', '07', '2024', 543, 0.0]\n",
            "[5, 'Investimento', '06', '01', '2023', 4050, 0.0]\n",
            "[6, 'Receita', '06', '06', '2024', 2411, 0.0]\n",
            "[7, 'Despesa', '02', '10', '2024', -3186, 0.0]\n",
            "[8, 'Investimento', '08', '12', '2024', 3018, 0.0]\n",
            "[9, 'Despesa', '15', '11', '2023', -1666, 0.0]\n",
            "[10, 'Investimento', '11', '11', '2024', 785, 0.0]\n",
            "[11, 'Receita', '24', '11', '2023', 4002, 0.0]\n",
            "[12, 'Despesa', '05', '04', '2024', -4896, 0.0]\n",
            "[13, 'Investimento', '27', '08', '2024', 2796, 0.0]\n",
            "[14, 'Receita', '18', '06', '2024', 3903, 0.0]\n",
            "[15, 'Receita', '05', '08', '2023', 3798, 0.0]\n",
            "[16, 'Receita', '06', '06', '2024', 4432, 0.0]\n",
            "[17, 'Investimento', '15', '02', '2023', 3489, 0.0]\n",
            "[18, 'Despesa', '27', '07', '2024', -2135, 0.0]\n",
            "[19, 'Despesa', '05', '05', '2023', -2808, 0.0]\n",
            "[20, 'Despesa', '01', '09', '2023', -2052, 0.0]\n",
            "[21, 'Receita', '24', '12', '2024', 2506, 0.0]\n",
            "[22, 'Receita', '01', '08', '2024', 3304, 0.0]\n",
            "[23, 'Receita', '17', '11', '2023', 2346, 0.0]\n",
            "[24, 'Despesa', '15', '02', '2023', -4920, 0.0]\n",
            "[25, 'Investimento', '08', '03', '2023', 2226, 0.0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Menu Inicial"
      ],
      "metadata": {
        "id": "vZP_2irQZFkn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Função que inicializa o algoritimo\n",
        "def sistema():\n",
        "  menu = menu_principal()\n",
        "  match menu:\n",
        "    case '1':\n",
        "      novo_registro()\n",
        "    case '2':\n",
        "      consultar()\n",
        "    case '3':\n",
        "      exportar_relatorio()\n",
        "    case '4':\n",
        "      agrupar()\n",
        "    case '5':\n",
        "      atualizar_registro()\n",
        "    case '6':\n",
        "      excluir_registro()\n",
        "    case '7':\n",
        "      print('\\nObrigado por utilizar nosso sistema!')\n",
        "    case _:\n",
        "      print('\\nEntrada Inválida!\\n')\n",
        "      sistema()\n",
        "\n",
        "# Função que solicita ao usuário qual o tipo de operação fazer\n",
        "def menu_principal():\n",
        "    menu = input('''\n",
        "======= Escolha a operação desejada =======\n",
        "\n",
        "  [1] Cadastrar | [2] Consulta\n",
        "  [3] Exportar  | [4] Consolidado\n",
        "  [5] Atualizar | [6] Excluir\n",
        "  [7] Sair\n",
        "\n",
        "===========================================\n",
        "    ''')\n",
        "    return menu"
      ],
      "metadata": {
        "id": "TYqn4uJQPPXm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Novos Registros**  \n",
        "Criar novos registros e identificar a data que o registro foi feito, qual tipo de movimentação, valor.  \n",
        "\n",
        "- Os tipos podem ser despesas, receita ou investimento:\n",
        "  - No caso de receita, o valor deve ser tratado como numerico e armazenado normalmente.\n",
        "  - no caso de despesas o valor deve ser recebido como positivo, mas armazenado como negativo\n",
        "  - No caso de investimento, deve ter uma informação a mais de 'Montante', em que será calculado quanto o dinheiro rendeu desde o dia que foi investido. Para essa finalidade utilize a seguinte formula: $M = C * (1 + i)^t$ ([Saiba mais](https://matematicafinanceira.org/juros-compostos/)), considere tudo em dias."
      ],
      "metadata": {
        "id": "xNb_q1FaOi6t"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função que armazena as informações da movimentação no Banco de Dados\n",
        "def novo_registro():\n",
        "    data_dia, data_mes, data_ano, tipo, valor = insira_dados()\n",
        "    atualiza_id_counter()\n",
        "    match tipo:\n",
        "        case ('Receita' | 'Investimento'):\n",
        "            registros.append([id_counter, tipo, data_dia, data_mes, data_ano, valor, 0.0])\n",
        "        case 'Despesa':\n",
        "            registros.append([id_counter, tipo, data_dia, data_mes, data_ano, -abs(valor), 0.0])\n",
        "    continuar()\n",
        "\n",
        "def continuar():\n",
        "    continua = input('Deseja continuar a cadastrar? (s/n)').lower()\n",
        "    match continua:\n",
        "        case 's':\n",
        "            novo_registro()\n",
        "        case 'n':\n",
        "            sistema()\n",
        "        case _:\n",
        "            print('Entrada Inválida!')\n",
        "\n",
        "\n",
        "# Fução que solicita as informações da Lançamento ao usuário\n",
        "def insira_dados():\n",
        "    tipo = receber_tipo()\n",
        "    valor = receber_valor()\n",
        "    data_dia, data_mes, data_ano = get_data()\n",
        "    return data_dia, data_mes, data_ano, tipo, valor\n",
        "\n",
        "def receber_valor():\n",
        "  valor = float(input('Qual o valor da operação: R$ '))\n",
        "  return valor\n",
        "\n",
        "\n",
        "# Função que recebe e valida o tipo\n",
        "def receber_tipo():\n",
        "    while True:\n",
        "        tipo = input('''\n",
        "====== Informe o Tipo de Movimentação ======\n",
        "\n",
        "               [1] Receita\n",
        "               [2] Despesa\n",
        "               [3] Investimento\n",
        "\n",
        "============================================\n",
        "      ''')\n",
        "        match tipo:\n",
        "            case '1':\n",
        "                return 'Receita'\n",
        "            case '2':\n",
        "                return 'Despesa'\n",
        "            case '3':\n",
        "                return 'Investimento'\n",
        "            case _:\n",
        "                print('\\nEntrada Inválida')\n",
        "\n",
        "\n",
        "# Função que armazena o dia, mês e ano no instante do cadastro\n",
        "def get_data():\n",
        "    data_dia = datetime.now().strftime('%d')\n",
        "    data_mes = datetime.now().strftime('%m')\n",
        "    data_ano = datetime.now().strftime('%Y')\n",
        "    return data_dia, data_mes, data_ano\n",
        "\n",
        "# Função que incrementa o gerador de ID\n",
        "def atualiza_id_counter():\n",
        "      global id_counter\n",
        "      id_counter += 1"
      ],
      "metadata": {
        "id": "skWjbNrIg2fF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "snhkaV1vhPgr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Ler** registros:\n",
        "Deverá ser possível consultar os registros por data, tipo ou valor.\n",
        "Consulta de valor por intervalo"
      ],
      "metadata": {
        "id": "sW9skrIuO6Y_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função que inicializa o Menu de Consultas\n",
        "def consultar():\n",
        "  filtro = menu_consultar()\n",
        "  match filtro:\n",
        "    case '1':\n",
        "      filtrar_data()\n",
        "    case '2':\n",
        "      filtrar_tipo()\n",
        "    case '3':\n",
        "      filtrar_valor()\n",
        "    case '0':\n",
        "      sistema()\n",
        "    case _:\n",
        "      print('\\nEntrada Inválida')\n",
        "      consultar()\n",
        "\n",
        "# Função que solicita ao usuário o Parametro de pesquisa\n",
        "def menu_consultar():\n",
        "    tipo_filtro = input('''\n",
        "=== Informe o Parametro a ser Pesquisado ===\n",
        "\n",
        "               [1] Período\n",
        "               [2] Tipo\n",
        "               [3] Valor\n",
        "               [0] Menu Inicial\n",
        "\n",
        "============================================\n",
        "''')\n",
        "    return tipo_filtro\n",
        "\n",
        "def continuar_consulta():\n",
        "    continua = input('\\nDeseja continuar consultando? (s/n)').lower()\n",
        "    match continua:\n",
        "        case 's':\n",
        "            consultar()\n",
        "        case 'n':\n",
        "            sistema()\n",
        "        case _:\n",
        "            print('Entrada Inválida!')"
      ],
      "metadata": {
        "id": "MsCyTRRRswI1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###### **Filtro por Data**"
      ],
      "metadata": {
        "id": "2E5P-rvS7pDc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função que executa a seleção dos lançamentos que estão dentro do intervalo selecionado\n",
        "def filtrar_data():\n",
        "    selecao = []\n",
        "    selecao.append(registros[0])\n",
        "    data_inicial, data_final = solicitar_periodo()\n",
        "    for lancamento in registros[1:]:\n",
        "        data_lancamento = montar_data(lancamento)\n",
        "        if (datetime.strptime(data_inicial, \"%d-%m-%Y\")) <= (datetime.strptime(data_lancamento, \"%d-%m-%Y\")) <= (datetime.strptime(data_final, \"%d-%m-%Y\")):\n",
        "          if lancamento[1] == 'Investimento':\n",
        "            atualizar_rendimento(lancamento)\n",
        "          selecao.append(lancamento)\n",
        "    return imprimir_selecao(selecao)\n",
        "\n",
        "# Função que solicita o intervalo de datas a ser pesquisado\n",
        "def solicitar_periodo():\n",
        "        data_inicial = input('Infomre a Data Inicial do Período (dd-mm-aaaa): ')\n",
        "        validar_date(data_inicial)\n",
        "        data_final = input('Infomre a Data Fnal do Período (dd-mm-aaaa): ')\n",
        "        validar_date(data_final)\n",
        "        data_inicial, data_final = validar_periodo(data_inicial, data_final)\n",
        "        return data_inicial, data_final\n",
        "\n",
        "#Função que valida se o período informado é coerente: Data Inicial < Data Final\n",
        "def validar_periodo(data_inicial, data_final):\n",
        "    if (datetime.strptime(data_inicial, \"%d-%m-%Y\")) <= (datetime.strptime(data_final, \"%d-%m-%Y\")):\n",
        "        return data_inicial, data_final\n",
        "    else:\n",
        "        print('\\nA data inicial não pode ser superior a data final.')\n",
        "        filtrar_data()\n",
        "\n",
        "# Função que valida datas\n",
        "def validar_date(data):\n",
        "    formato = '%d-%m-%Y'\n",
        "    try:\n",
        "        teste = bool(datetime.strptime(data, formato))\n",
        "        if teste:\n",
        "            return False\n",
        "    except:\n",
        "        print('\\nData não existe ou está fora do fomrato solicitado!')\n",
        "        filtrar_data()\n",
        "\n",
        "# Função que recebe os dados de Dia, mês e Ano dos registros e concatena em uma string\n",
        "def montar_data(lancamento):\n",
        "    data_lancamento = lancamento[2] + '-' + lancamento[3] + '-' + lancamento[4]\n",
        "    return data_lancamento"
      ],
      "metadata": {
        "id": "lD0KmH0h7oSG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###### **Filtro por Tipo**"
      ],
      "metadata": {
        "id": "2yCiEPaN70TY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def filtrar_tipo():\n",
        "  operacao = menu_tipo()\n",
        "  match operacao:\n",
        "    case '1':\n",
        "      selecao = list(filter(buscar_receitas, registros))\n",
        "      return imprimir_selecao(selecao)\n",
        "    case '2':\n",
        "      selecao = list(filter(buscar_despesas, registros))\n",
        "      return imprimir_selecao(selecao)\n",
        "    case '3':\n",
        "      selecao = list(filter(buscar_investimentos, registros))\n",
        "      return imprimir_selecao(selecao)\n",
        "    case _:\n",
        "      print('\\nEntrada Inválida')\n",
        "\n",
        "# Função que solicita o tipo de operação a ser filtrado ao usuário\n",
        "def menu_tipo():\n",
        "    operacao = input('''\n",
        "== Qual o Tipo de Operação deseja filtrar ==\n",
        "\n",
        "               [1] Receita\n",
        "               [2] Despesa\n",
        "               [3] Investimento\n",
        "\n",
        "============================================\n",
        "        ''')\n",
        "    return operacao\n",
        "\n",
        "\n",
        "# Função que itera no banco de dados e retorna as Movimentações de Receita\n",
        "def buscar_receitas(lancamento):\n",
        "    if lancamento[1] == 'Operação':\n",
        "        return lancamento\n",
        "    if lancamento[1] == 'Receita':\n",
        "        return lancamento\n",
        "\n",
        "# Função que itera no banco de dados e retorna as Movimentações de Despesas\n",
        "def buscar_despesas(lancamento):\n",
        "    if lancamento[1] == 'Operação':\n",
        "        return lancamento\n",
        "    if lancamento[1] == 'Despesa':\n",
        "        return lancamento\n",
        "\n",
        "# Função que itera no banco de dados e retorna as Movimentações de Investimentos\n",
        "def buscar_investimentos(lancamento):\n",
        "    if lancamento[1] == 'Operação':\n",
        "        return lancamento\n",
        "    if lancamento[1] == 'Investimento':\n",
        "        lancamento = atualizar_rendimento(lancamento)\n",
        "        return lancamento"
      ],
      "metadata": {
        "id": "poSJzJTW7297"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###### Filtro por Valor"
      ],
      "metadata": {
        "id": "scRhb5YT8GYm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função que filtra os elementos dentro do intervalo de valor solicitado\n",
        "def filtrar_valor():\n",
        "    valor_minimo, valor_maximo = solicitar_valor()\n",
        "    selecao = list([lancamento for lancamento in registros[1:] if valor_minimo <= lancamento[5] <= valor_maximo])\n",
        "    for lancamento in selecao:\n",
        "      if lancamento[1] == 'Investimento':\n",
        "        atualizar_rendimento(lancamento)\n",
        "    selecao.insert(0, registros[0])\n",
        "    return imprimir_selecao(selecao)\n",
        "\n",
        "# Função que solicita o intervalo de valores a ser pesquisado\n",
        "def solicitar_valor():\n",
        "    valor_minimo = float(input(\"Informe o valor mínimo do intervalo: \"))\n",
        "    valor_maximo = float(input(\"Informe o valor máximo do intervalo: \"))\n",
        "    return valor_minimo, valor_maximo"
      ],
      "metadata": {
        "id": "9ONJ7YAO8Kb8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###### **Impressão da Consulta**"
      ],
      "metadata": {
        "id": "q-Ot08Yx8Qeg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função que retorna a impressão da seleção dos dados\n",
        "def imprimir_selecao(selecao):\n",
        "    titulo_data = selecao[0][2] + '-' + selecao[0][3] + '-' + selecao[0][4]\n",
        "    print(f'\\n\\n{selecao[0][0]:^5} {selecao[0][1]:^15} {titulo_data:^12} {selecao[0][5]:>15} {selecao[0][6]:>15}')\n",
        "    for item in selecao[1:]:\n",
        "        if item[1] == 'Investimento':\n",
        "            data = item[2] + '-' + item[3] + '-' + item[4]\n",
        "            print(f'{item[0]:^5} {item[1]:^15} {data:^12} {float(item[5]):>15.2f} {float(item[6]):>15.2f}')\n",
        "        else:\n",
        "            data = item[2] + '-' + item[3] + '-' + item[4]\n",
        "            print(f'{item[0]:^5} {item[1]:^15} {data:^12} {float(item[5]):>15.2f}')\n",
        "    continuar_consulta()"
      ],
      "metadata": {
        "id": "LO6kzry28VaV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Atualizar** registros:\n",
        "No caso de atualização, pode-se atualizar o valor, o tipo e a data deverá ser a de atualização do registro."
      ],
      "metadata": {
        "id": "nUyaWb_5PDws"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função de inicialização de atualização de registros\n",
        "def atualizar_registro():\n",
        "  operacao = menu_atualizar()\n",
        "  match operacao:\n",
        "    case '1':\n",
        "      atualizar_lancamento()\n",
        "    case '2':\n",
        "      atualizar_montante()\n",
        "    case '3':\n",
        "      sistema()\n",
        "    case _:\n",
        "      print('\\nEntrada Inválida')\n",
        "      atualizar_registro\n",
        "\n",
        "# Função do Submenu Atualizar\n",
        "def menu_atualizar():\n",
        "  operacao = input('''\n",
        "========== Atualiza Registro por: ==========\n",
        "\n",
        "               [1] Tipo e Valor\n",
        "               [2] Montante\n",
        "               [3] Menu Principal\n",
        "\n",
        "============================================\n",
        "        ''')\n",
        "  return operacao\n",
        "\n",
        "# Função que executa a atualização do registro\n",
        "def atualizar_lancamento():\n",
        "    indice = get_id()\n",
        "    lancamento = registros[buscar_registro(indice)]\n",
        "    lancamento[1] = receber_tipo()\n",
        "    lancamento[5] = receber_valor()\n",
        "    if (lancamento[1] == 'Despesa'):\n",
        "      lancamento[5] = -abs(lancamento[5])\n",
        "    lancamento[2], lancamento[3], lancamento[4] = get_data()\n",
        "    if (lancamento[1] == 'Investimento'):\n",
        "      atualizar_rendimento(lancamento)\n",
        "    print('Lançamento atualizado com sucesso.')\n",
        "    return\n",
        "\n",
        "# Função que recebe o input do ID para atualizar\n",
        "def get_id():\n",
        "  try:\n",
        "    id = int(input(\"Infomre o ID da operação que deseja atualizar: \"))\n",
        "  except:\n",
        "    print('Entrada Inválida!')\n",
        "    get_id()\n",
        "  return id\n",
        "\n",
        "# Função que busca o registro que será atualizado\n",
        "def buscar_registro(id):\n",
        "    indice = 1\n",
        "    for lancamento in registros[1:]:\n",
        "      if lancamento[0] == id:\n",
        "        return indice\n",
        "      else:\n",
        "        indice += 1\n",
        "    print(f'\\nO ID nº {id} não foi encontrado.')\n",
        "    atualizar_registro()"
      ],
      "metadata": {
        "id": "ZeQI_Pgw_Xtp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Deletar**:  \n",
        "Deverá ser possível deletar o registro (caso necessário, considere o indice do elemento como ID)"
      ],
      "metadata": {
        "id": "MRo92_hpPMjJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função de execussão da exclusao de registro\n",
        "def excluir_registro():\n",
        "    indice = get_id_excluir()\n",
        "    lancamento = registros[buscar_registro_excluir(indice)]\n",
        "    registros.remove(lancamento)\n",
        "    print(f\"\\nRegistro com ID {indice} deletado com sucesso.\")\n",
        "    menu_principal()\n",
        "\n",
        "# Função que localiza o registro a ser excluido\n",
        "def buscar_registro_excluir(id):\n",
        "    indice = 1\n",
        "    for lancamento in registros[1:]:\n",
        "      if lancamento[0] == id:\n",
        "        return indice\n",
        "      else:\n",
        "        indice += 1\n",
        "    print(f'\\nO ID nº {id} não foi encontrado.')\n",
        "    sistema()\n",
        "\n",
        "# Função que recebe o input para exclusão de registro\n",
        "def get_id_excluir():\n",
        "  id = int(input(\"Qual registro deseja excluir?\"))\n",
        "  return id"
      ],
      "metadata": {
        "id": "32KuDePXpXZJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "N_klnbO0Mo3w"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Crie uma função que atualize os valores de rendimento sempre que chamada"
      ],
      "metadata": {
        "id": "dihGyqA_t52s"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função que busca os lançamento de investimento e pede a atualização do Montante\n",
        "def atualizar_montante():\n",
        "    for lancamento in registros:\n",
        "        if lancamento[1] == 'Investimento':\n",
        "            atualizar_rendimento(lancamento)\n",
        "    print('O montante das operações de investimentos foram atualizados.')\n",
        "    return registros\n",
        "\n",
        "# Função que executa a atualização do montante no lançamento\n",
        "def atualizar_rendimento(lancamento):\n",
        "    data_atual = datetime.now().strftime('%d-%m-%Y')\n",
        "    data_cadastro = montar_data(lancamento)\n",
        "    periodo = abs(datetime.strptime(data_atual, \"%d-%m-%Y\") - datetime.strptime(data_cadastro, \"%d-%m-%Y\"))\n",
        "    lancamento[6] = round((float(lancamento[5]) * ((1 + 0.02)**periodo.days)), 2)\n",
        "    return lancamento"
      ],
      "metadata": {
        "id": "t3xq_VfMqWG0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Crie uma função exportar_relatorio, que seja possível exportar um relatorio final em csv ou json."
      ],
      "metadata": {
        "id": "uh4niwJCOPEV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função de exportação de relatório\n",
        "def exportar_relatorio():\n",
        "    formato = menu_exportar()\n",
        "    match formato:\n",
        "      case '1':\n",
        "        criar_CSV()\n",
        "      case '2':\n",
        "        criar_JSON()\n",
        "      case '0':\n",
        "        sistema()\n",
        "      case _:\n",
        "        print(\"Entrada inválida!\")\n",
        "        exportar_relatorio()\n",
        "\n",
        "# Função que grava o arquivo CSV\n",
        "def criar_CSV():\n",
        "  with open('relatorio.csv', 'w') as arquivo_csv:\n",
        "    for registro in registros:\n",
        "      arquivo_csv.write(','.join(map(str, registro)) + '\\n')\n",
        "  print(\"\\nRelatório exportado para 'relatorio.csv'.\")\n",
        "  sistema()\n",
        "\n",
        "# Função que grava o arquivo JSON\n",
        "def criar_JSON():\n",
        "  dados = converter_dicionario()\n",
        "  with open('relatorio.json', 'w') as arquivo_json:\n",
        "    json.dump(converter_dicionario(), arquivo_json, indent=4, ensure_ascii=False)\n",
        "  print(\"\\nRelatório exportado para 'relatorio.json'.\")\n",
        "  sistema()\n",
        "\n",
        "# Função que gera dicionários para o salvamento em arquivo JSON\n",
        "def converter_dicionario():\n",
        "  chaves = registros[0]\n",
        "  relatorio_json = []\n",
        "  for lancamento in registros[1:]:\n",
        "    relatorio_json.append(dict(zip(chaves, lancamento)))\n",
        "  return relatorio_json\n",
        "\n",
        "# Função que apresenta o sub-menu da exportar e pede o input\n",
        "def menu_exportar():\n",
        "  formato = input('''\n",
        "======== Informe o Tipo de Arquivo =========\n",
        "\n",
        "               [1] CSV\n",
        "               [2] JSON\n",
        "               [0] Menu Inicial\n",
        "\n",
        "============================================\n",
        "''')\n",
        "  return formato"
      ],
      "metadata": {
        "id": "Xx-MlsHuOgq_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Crie pelo menos uma função de agrupamento, que seja capaz de mostrar o total de valor baseado em alguma informação (mes, tipo...)\n"
      ],
      "metadata": {
        "id": "DZ5I7CRcu_dB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Função que inicializa o agrupamento\n",
        "def agrupar():\n",
        "    formato = menu_agrupamento()\n",
        "    match formato:\n",
        "      case '1':\n",
        "        agrupar_receitas()\n",
        "      case '2':\n",
        "        agrupar_despesas()\n",
        "      case '3':\n",
        "        agrupar_investimentos()\n",
        "      case _:\n",
        "        print(\"Entrada inválida!\")\n",
        "        exportar_relatorio()\n",
        "\n",
        "# Função que recebe uma lista agrupada de Receitas e calcula o valor Total\n",
        "def agrupar_receitas():\n",
        "  selecao = list(filter(filtra_receitas, registros))\n",
        "  soma = 0\n",
        "  for lancamento in selecao:\n",
        "    soma += lancamento[5]\n",
        "  print(f\"\\nSão {len(selecao)} transações de Receita totalizando R$ {soma:.2f}.\")\n",
        "  sistema()\n",
        "\n",
        "# Função que recebe uma lista agrupada de Despesas e calcula o valor Total\n",
        "def agrupar_despesas():\n",
        "  selecao = list(filter(filtra_despesas, registros))\n",
        "  soma = 0\n",
        "  for lancamento in selecao:\n",
        "    soma += lancamento[5]\n",
        "  print(f\"\\nSão {len(selecao)} transações de Despesa totalizando R$ {soma:.2f}.\")\n",
        "  sistema()\n",
        "\n",
        "# Função que recebe uma lista agrupada de Investimentos e calcula o valor Total\n",
        "def agrupar_investimentos():\n",
        "  selecao = list(filter(filtra_investimentos, registros))\n",
        "  soma = 0\n",
        "  soma_montante = 0\n",
        "  atualizar_montante()\n",
        "  for lancamento in selecao:\n",
        "    soma += lancamento[5]\n",
        "    soma_montante += lancamento[6]\n",
        "  print(f\"\\nSão {len(selecao)} transações de Investimentos totalizando R$ {soma:.2f} em valor e R$ {soma_montante} montante.\")\n",
        "  sistema()\n",
        "\n",
        "# Função que cria lista agrupada de receitas\n",
        "def filtra_receitas(lancamento):\n",
        "  if lancamento[1] == 'Receita':\n",
        "    return lancamento\n",
        "\n",
        "# Função que cria lista agrupada de despesa\n",
        "def filtra_despesas(lancamento):\n",
        "  if lancamento[1] == 'Despesa':\n",
        "    return lancamento\n",
        "\n",
        "# Função que cria lista agrupada de investimentos\n",
        "def filtra_investimentos(lancamento):\n",
        "  if lancamento[1] == 'Investimento':\n",
        "    return lancamento\n",
        "\n",
        "# Função que apresenta o submenu de agrupamento\n",
        "def menu_agrupamento():\n",
        "  agrupar = input('''\n",
        "=== Informe o Parametro a ser Pesquisado ===\n",
        "\n",
        "               [1] Receitas\n",
        "               [2] Despesas\n",
        "               [3] Investimentos\n",
        "\n",
        "============================================\n",
        "''')\n",
        "  return agrupar"
      ],
      "metadata": {
        "id": "soW6QJA2t7vl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Teste de Mesa"
      ],
      "metadata": {
        "id": "nL8eotL6fjZj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sistema()"
      ],
      "metadata": {
        "id": "i5cEqC2ofmwg",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1f7f969c-d278-4038-ea92-72a7a46f2dfa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "======= Escolha a operação desejada =======\n",
            "\n",
            "  [1] Cadastrar | [2] Consulta\n",
            "  [3] Exportar  | [4] Consolidado\n",
            "  [5] Atualizar | [6] Excluir\n",
            "  [7] Sair\n",
            "\n",
            "===========================================\n",
            "    7\n",
            "\n",
            "Obrigado por utilizar nosso sistema!\n"
          ]
        }
      ]
    }
  ]
}