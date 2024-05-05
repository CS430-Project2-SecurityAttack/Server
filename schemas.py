from pydantic import BaseModel

class SymmetricKey(BaseModel):
    """
    Represents a symmetric key.

    Attributes:
        id (str): The ID of the symmetric key.
        mac_address (str): The MAC address associated with the symmetric key.
        key (str): The actual key value.
    """
    id: str
    mac_address: str
    key: str

class SymmetricKeyCreate(BaseModel):
    """
    Represents the creation of a symmetric key.

    Attributes:
        mac_address (str): The MAC address associated with the symmetric key.
    """
    mac_address: str
    
class BankAccount(BaseModel):
    """
    Represents a bank account.

    Attributes:
        routing_number (str): The routing number of the bank account.
        account_holder (str): The name of the account holder.
        account_number (str): The bank account number.
    """
    routing_number: str
    account_holder: str
    account_number: str

class BankAccountCreate(BaseModel):
    """
    Represents the creation of a bank account.

    Attributes:
        routing_number (str): The routing number of the bank account.
        account_holder (str): The name of the account holder.
        account_number (str): The bank account number.
    """
    routing_number: str
    account_holder: str
    account_number: str
    