from app import models

class AccountManager:
    '''
    Provides functions for logging in and signing up accounts.
    '''

    def account_exists(username: str):
        '''Checks if account with [username] exists.'''
        return models.User.query.filter_by(username=username).first()
    
    def get_account_from_username(username: str):
        '''
        Returns <User object> if the account exists
        using the provided username. Returns None if
        no such account exists.
        '''
        return models.User.query.filter_by(username=username).first()
    
    def get_account_salt(username: str):
        if AccountManager.account_exists(username):
            return AccountManager.get_account_from_username(username).salt
