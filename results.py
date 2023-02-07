# This example uses the Beaker framework
from algosdk.transaction import *
from algosdk import *
from pyteal import *
from beaker import *
import os
from algosdk.abi import ABIType
from algosdk.encoding import encode_address, decode_address
from algosdk.atomic_transaction_composer import TransactionWithSigner
from algosdk.transaction import *
import json
from application import AppMember, MembershipRecord, MembershipClub  # type: ignore
class NamedTupleBox(Application):

        class VoteRecord(abi.NamedTuple):
            role: abi.Field[abi.String]
            voted: abi.Field[abi.Bool]

        @external
        def add_vote(self, role: abi.String, voted: abi.Bool,*, output: VoteRecord):
            return Seq(
                output.set(role, voted),
                App.box_put(Txn.sender(), output.encode()),
            )

def print_boxes(app_client: client.ApplicationClient):
        boxes = app_client.get_box_names()
        print(f"{len(boxes)} boxes found")
        for box_name in boxes:
            contents = app_client.get_box_contents(box_name)
            main=contents.decode()
            print(contents.decode())
def pr(app_client: client.ApplicationClient):
        boxes = app_client.get_box_names()
        for box_name in boxes:
            contents = app_client.get_box_contents(box_name)
            return contents.decode()
with open("data.json", "r") as file:
        data = json.load(file)
def remove_hex_values(s):
    new_string = ""
    for char in s:
        if ord(char) >= 32:
            new_string += char
    return new_string
main={}
for i in data:
    accs=sandbox.get_accounts()
    acct=accs.pop(1)
    app_client = client.ApplicationClient(
            sandbox.get_algod_client(), NamedTupleBox(), signer=acct.signer
        )
    app_client.app_id=data[i]['app_id']
    string = pr(app_client)
    new_string = remove_hex_values(string)
    if new_string in main.keys():
      main[new_string]+=1
    else:
        main[new_string]=1
print("Results of the voting are:")
print(main)
