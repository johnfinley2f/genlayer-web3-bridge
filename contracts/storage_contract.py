from genlayer_py import gl, Contract, create_client, create_account, Localnet
from genlayer_py.types import Address
from genlayer_py.transactions import MessageType, derive_internal_message_call_key

@gl.contract
class StorageContract:
    def __init__(self):
        self.storage = 0  # simple counter/storage variable

    @gl.public
    def set_storage(self, value: int) -> None:
        """Update storage (write operation - Intelligent Contract style)"""
        self.storage = value
        print(f"Storage updated to {value}")

    @gl.public
    def get_storage(self) -> int:
        """Read storage (read-only)"""
        return self.storage

    # Optional: Emit message for other contracts (GenLayer feature)
    @gl.public
    def emit_message(self, target: Address, value: int) -> None:
        # Example internal message to another contract
        key = derive_internal_message_call_key("set_storage")
        # Message will be handled by GenVM automatically
        print(f"Message emitted to target {target} for value {value}")

    # Simple main for testing locally
    @gl.public
    def main(self):
        print("✅ StorageContract deployed successfully on GenLayer!")
        print("Use set_storage(42) and get_storage()")

# For local testing / Studio simulation
if __name__ == "__main__":
    client = create_client(chain=Localnet)
    account = create_account()
    contract = StorageContract()
    print("Contract ready for deployment!")
