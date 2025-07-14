from passlib.context import CryptContext
pwd_crt = CryptContext(schemes = ['bcrypt'],deprecated = 'auto')

class Hash():
    def dcrypt(password: str):
        return  pwd_crt.hash(password)
    
    def verify(hashed_password,plain_password):
        return pwd_crt.verify(plain_password,hashed_password)