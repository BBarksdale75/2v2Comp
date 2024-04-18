class AccountNotFound(Exception):
    """Exception raised when an account is not found."""

    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"Account with ID {account_id} not found")
