def validate_email(email):
    if email.count('@') != 1:
        return False
    
    username, domain = email.split('@')

    if len(username) == 0:
        return False
    
    if '.' not in domain:
        return False
    
    if ' ' in email:
        return False
    
    parts = domain.split('.')
    if len(parts) < 2:
        return False
    
    extension = parts[-1]
    if extension not in ["com","org","in","edu","ac"]:
        return False

    return True 


