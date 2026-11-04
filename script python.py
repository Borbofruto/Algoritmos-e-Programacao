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
    def discount(quantity):
        if quantity < 5:
            rate = 0
        elif quantity >= 5 and quantity <= 9:
            rate = 0.05
        elif quantity >= 10 and quantity <= 19:
            rate = 0.1
        elif quantity > 20:
            rate = 0.15

        discount = rate

        return discount

    @classmethod
    def create_product(cls):
        product = {
            "code": cls.code(),
            "description": cls.description(),
            "price": cls.price(),
            "quantity": cls.quantity(),
        }
        gross_value = product['price'] * product['quantity']
        discount_rate = cls.discount(product["quantity"])

        product["discount"] = gross_value * discount_rate

        print(f"Subtotal Bruto: R$ {gross_value:.2f} | Desconto ({discount_rate}%): R$ {product['discount']} | Líquido: R$ {(product['price'] * product['quantity']) - product['discount']:.2f}")

        return product

def checkout_manager(shopping_cart, user_name):
    itens_comprados = f"{', '.join([dictionary['description'] for dictionary in shopping_cart])}"
    quantidade_total_pecas = sum([dictionary['quantity'] for dictionary in shopping_cart])
    total_bruto = sum([dictionary['price'] for dictionary in shopping_cart]) * quantidade_total_pecas
    desconto = sum([dictionary['discount'] for dictionary in shopping_cart])
    total_liquido = total_bruto - desconto
    preco_medio_por_peca = total_liquido / quantidade_total_pecas
    
    print(f"""
    ==================== EXTRATO FISCAL ====================
    Itens Comprados: {itens_comprados}
    Quantidade Total de Peças: {quantidade_total_pecas} unidades
    Total Bruto: R${total_bruto:.2f}
    Desconto Total: R${desconto:.2f}
    VALOR FINAL A PAGAR: R${total_liquido:.2f}
    Preço Médio por Peça: R${preco_medio_por_peca:.2f}
    Código do produto
    """)
    
carrinho = []

carrinho.append(RegisterProduct.create_product())

while True:
    pedido_novo_produto = input("Deseja adicionar outro produto? (S/N): ").strip().upper()
    if pedido_novo_produto == "S":
        carrinho.append(RegisterProduct.create_product())
    elif pedido_novo_produto == "N":
        user_name = input("Qual seu nome? ").strip().upper()
        break
    else:
        print('Opção inválida, digite apenas "S" ou "N"')

    
checkout_manager(carrinho, user_name)
