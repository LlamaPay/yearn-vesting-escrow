from brownie import VestingEscrowSimple, accounts

def main():
    acct = accounts.load(2)
    return VestingEscrowSimple.deploy()