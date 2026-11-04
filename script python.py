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
            if float(user_input) > 0:
                return True
            else:
                return False

    @staticmethod
    def quantity(user_input):
            try:
                int(user_input)
            except ValueError:
                return False
            else:
                if int(user_input) > 0:
                    return True
                else:
                    return False

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
                return price
            else:
                print("ERRO: Digite um número válido para o preço.")

    @staticmethod
    def quantity():
            while True:
                user_input = input("Digite a quantidade de unidades do produto: ")

                if ValidProduct.quantity(user_input):
                    quantity = int(user_input)
                    return quantity            
                else:
                    print("ERRO: Digite um número válido para a quantidade.")

    @staticmethod
    def discount(quantity, price):
        if quantity < 5:
            rate = 0
        elif quantity >= 5 and quantity <= 9:
            rate = 0.05
        elif quantity >= 10 and quantity <= 19:
            rate = 0.1
        if quantity > 20:
            rate = 0.15

        gross_value = (quantity * price)
        discount = gross_value - (gross_value * rate)

        return discount

    @classmethod
    def create_product(cls):
        product = {
            "code": cls.code(),
            "description": cls.description(),
            "price": cls.price(),
            "quantity": cls.quantity(),
        }
        product["discount"] = cls.discount(product["quantity"], product["price"])

        return product

def checkout_manager(shopping_cart):
    itens_comprados = f"{', '.join([dictionary['description'] for dictionary in shopping_cart])}"
    quantidade_total_pecas = sum([dictionary['quantity'] for dictionary in shopping_cart])
    total_bruto = sum([dictionary['price'] for dictionary in shopping_cart])
    desconto = sum([dictionary['discount'] for dictionary in shopping_cart])
    
    print(f"""
    ==================== EXTRATO FISCAL ====================
    Itens Comprados: {itens_comprados}
    Quantidade Total de Peças: {quantidade_total_pecas} unidades
    Total Bruto: R${total_bruto:.2f}
    Desconto Total: R${desconto}
    Preço Médio por Peça: R${total_bruto / itens_comprados:.2f}
    """)
    
carrinho = []

carrinho.append(RegisterProduct.create_product())

while True:
    user_input = input("Deseja adicionar outro produto? (S/N): ").strip().upper()
    if user_input == "S":
        carrinho.append(RegisterProduct.create_product())
    elif user_input == "N":
        break
    else:
        print('Opção inválida, digite apenas "S" ou "N"')

checkout_manager(carrinho)
