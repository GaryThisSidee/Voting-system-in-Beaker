from typing import Final
from pyteal import abi, TealType, Global, Approve
from beaker import (
    Application,
    AccountStateValue,
    ApplicationStateValue,
    Authorize,
    create,
    external,
    opt_in,
    close_out,
    delete,
    client,
    sandbox,
    consts,
)
import json
from algosdk.transaction import *
from algosdk import *
from pyteal import *
from beaker import *
import os
from algosdk.abi import ABIType
from algosdk.encoding import encode_address, decode_address
from algosdk.atomic_transaction_composer import TransactionWithSigner
from algosdk.transaction import *
from beaker.client.application_client import ApplicationClient
from beaker.client.logic_error import LogicException
def print_boxes(app_client: client.ApplicationClient):
        boxes = app_client.get_box_names()
        print(f"{len(boxes)} boxes found")
        for box_name in boxes:
            contents = app_client.get_box_contents(box_name)
            print(contents.decode())
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


def demo():
    path="data.json"
    if os.path.isfile(path):
      with open("data.json", "r") as file:
        data = json.load(file)

    if __name__ == "__main__":
       accts = sandbox.get_accounts()
       voter_acct = accts.pop(0)
       acct2 = accts.pop(1)
       print("Enter the person u wanna vote to make sure all the leters are in the lower case format")
       idk=input()
       
       app_client1 = client.ApplicationClient(
           sandbox.get_algod_client(), NamedTupleBox(), signer=voter_acct.signer
       )
       value=data.get(str(voter_acct.address),False)
       if value:
            print("U have already submitted ur vote")
       else:
            app_client1.create()
            app_client1.fund(100 * consts.algo)
            print("App ID")
            print(app_client1.app_id)
            ls = voter_acct.address.encode()
            result = app_client1.call(
                    NamedTupleBox.add_vote,
                    role=idk,
                    voted=False,
                    boxes=[[app_client1.app_id, encoding.decode_address(voter_acct.address)]],
                )
            
            app_client2 = app_client1.prepare(signer=acct2.signer)
            print(f"Current app state: {app_client1.get_application_state()}")
            data[str(voter_acct.address)]={
                        "app_id":app_client1.app_id,
                    }
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
    else:
      if __name__ == "__main__":
       accts = sandbox.get_accounts()
       voter_acct = accts.pop()
       acct2 = accts.pop(1)
       idk=input()
       
       app_client1 = client.ApplicationClient(
           sandbox.get_algod_client(), NamedTupleBox(), signer=voter_acct.signer
       )
       app_client1.create()
       app_client1.fund(100 * consts.algo)

       ls = voter_acct.address.encode()
       result = app_client1.call(
               NamedTupleBox.add_vote,
               role=idk,
               voted=False,
               boxes=[[app_client1.app_id, encoding.decode_address(voter_acct.address)]],
           )
       
       app_client2 = app_client1.prepare(signer=acct2.signer)
       print(f"Current app state: {app_client1.get_application_state()}")
       data={}
       data[str(acct1.address)]={
            "app_id":app_client1.app_id,
        }
       with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
if __name__ == "__main__":
    demo()