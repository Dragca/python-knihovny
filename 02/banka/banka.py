# Nasimulujte bankovní systém
#
# V adresáři jsou soubory pojmenované číslem účtu obsahující zůstatek účtu
# Implementujte skript banka.py, který bude ovládán parametry:
#
# Částka se bude čerpat z účtu 111 pomocí --from 111
# Částka se bude připisovat na účet 222 pomocí --to 222
# Převod částky 1000 se určí parametrem --amount 1000
#
# Snažte se řešit různé chyby:
# * účet neexistuje
# * zůstatek by šel do záporu
#
# Příklad použití:
#
#   python banka.py --from 111 --to 222 --amount 1000
#
# V praxi se píší skripty, kde nezáleží na pořadí pojmenovaných parametrů, tj.
# ideální je, když funguje libovolné pořadí parametrů při spuštění:
#
#   python banka.py --from 111 --amount 1000 --to 222
#   python banka.py --amount 1000 --from 111 --to 222
#
# Pro tento pokročilý způsob je však třeba použít pokročilou knihovnu pro práci
# s parametry příkazové řádky, jako např. argparse nebo click.

# co musím pohlídat: pohlídat počet parametrů, existenci účtů, zůstatek, kladná hodnota převodu
import argparse

def load_balance(account):# načti zůstatek
    """retrieves account balance from the file """
    try:
        with open(str(account), 'r') as f:
            return float(f.read().strip())#odstranit bílé znaky a převést na číslo, požila jsem float, kdyby si chtěl někdo posílat haléře
    except FileNotFoundError:
        raise FileNotFoundError(f"Account {account} does not exist.")

def enter_balance(account, amount):# zapiš zůstatek
    """will enter a new balance into the account"""
    with open(str(account), 'w') as f:
        f.write(str(amount))

def money_transfer(from_account, to_account, amount):# převod penez
    """will transfer money between accounts"""
    balance_from = load_balance(from_account)# zůstatek na účtu "from"
    balance_to = load_balance(to_account)# zůstatek na účtu "to"

    if balance_from < amount:
        raise ValueError(f'The account {from_account} does not have sufficient balance.')#podchycení, že je dostatečný zůstatek
    elif amount < 0:#podchycení, že je převáděná částka kladná, jinak to dělalo binec
        raise ValueError(f'The transfer amount: {amount} was not positive.')

    enter_balance(from_account, balance_from - amount)
    enter_balance(to_account, balance_to + amount)
    print(f"Transfered {amount} Kč from account {from_account} to account {to_account}.")

parser = argparse.ArgumentParser(description='bank transfer between accounts')
parser.add_argument("--from", type=int, required=True, help="source account")
parser.add_argument("--to", type=int, required=True, help="target account")
parser.add_argument("--amount", type=float, required=True, help="amount to transfer")
args = parser.parse_args()

try:
    money_transfer(getattr(args,"from"), getattr(args, "to"), args.amount)#protože jsem chtěla zkusit napsat kod anglicky a nemohla použít klíčové slovo from jako args.from, musela jsem použít getattr.
except (ValueError, FileNotFoundError) as error:
    print(f'Error: {error}')
