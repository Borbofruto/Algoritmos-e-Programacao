class ValidProduct:
    @staticmethod
    def code(user_input):
        if user_input.startswith("P") and len(user_input) >= 3:
            return True
        else:
            return False

    @staticmethod
    def description(user_input):
        if not user_input == "":
            return True
        else:
            return False

    @staticmethod
    def price(user_input):
        try:
            float(user_input)
        except ValueError:
            return False
        else:
            return True

    @staticmethod
    def quantity(user_input):
            try:
                int(user_input)
            except ValueError:
                return False
            else:
                return True

class RegisterProduct:
    @staticmethod
    def code():
        while True:
            user_input = input("Digite o código do produto (inicia com P): ").strip().upper()

            if ValidProduct.code(user_input):
                code = user_input
                return code
            else:
                print("Código inválido. Digite um código válido.")

    @staticmethod
    def description():
        while True:
            user_input =  input("Digite o nome do produto: ").strip().title()

            if ValidProduct.description(user_input):
                description = user_input
                return description
            else:
                print("Nome inválido. Digite pelo menos 1 caractere.")

    @staticmethod
    def price():
        while True:
            user_input = input("Digite o preço unitário (R$): ")

            if ValidProduct.price(user_input):
                price = float(user_input)

                if price <= 0:
                    print('ERRO. Apenas valores maiores que "0" são válidos. Digite um valor válido.')
                else:
                    return price            
            else:
                print("Preço inválido. Digite apenas algarismos.")

    @staticmethod
    def quantity():
            while True:
                user_input = input("Digite a quantidade de unidades do produto: ")

                if ValidProduct.quantity(user_input):
                    quantity = int(user_input)

                    if quantity <= 0:
                        print('ERRO. Apenas valores maiores que "0" são válidos. Digite um valor válido.')
                    else:
                        return quantity            
                else:
                    print("Quantidade inválida. Digite apenas algarismos.")

    @classmethod
    def create_product(cls):
        return {
            "code": cls.code(),
            "description": cls.description(),
            "price": cls.price(),
            "quantity": cls.quantity()
        }
    
carrinho = []

while True:
    carrinho.append(RegisterProduct.create_product())
    if input("Deseja adicionar outro produto? (S/N): ") == "N":
        break

for produto in carrinho:
    print(f"O produto {produto['description']}, código - {produto['code']}, custa R${produto['price']:.2f}, e o total de {produto['quantity']} unidades dele é R${produto['price'] * produto['quantity']:.2f}")
