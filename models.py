from sqlalchemy import Column, String
import database 

class SymmetricKey(database.Base):
    """
    Represents a symmetric key used for encryption and decryption.

    Attributes:
        id (str): The unique identifier of the symmetric key.
        mac_address (str): The MAC address associated with the symmetric key.
        key (str): The actual symmetric key value.
    """
    __tablename__ = "symmetric_keys"

    id = Column(String, primary_key=True)  # Unique identifier for the symmetric key
    mac_address = Column(String)  # MAC address associated with the symmetric key
    key = Column(String)  # Actual symmetric key value
    
class BankAccount(database.Base):
    """
    Represents a bank account.

    Attributes:
        routing_number (str): The routing number of the bank account.
        account_holder (str): The account holder's name.
        account_number (str): The account number.
    """
    __tablename__ = "bank_accounts"

    routing_number = Column(String, primary_key=True)  # Routing number of the bank account
    account_holder = Column(String)  # Account holder's name
    account_number = Column(String)  # Account number