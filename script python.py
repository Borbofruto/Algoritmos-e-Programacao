class Valid:
    @staticmethod
    def product_id(user_input):
        if user_input.startswith("P") and len(id) >= 3:
            return True
        else:
            return False

class Register:
    @staticmethod
    def product_id():
        while True:
            user_input = input("Digite o código do produto (inicia com P):").strip().upper()
          
            if Valid.product_id(user_input):
                return user_input
            else:
                print("Produto inválido. Digie um código válido.")

product_id_registered = Register.product_id()