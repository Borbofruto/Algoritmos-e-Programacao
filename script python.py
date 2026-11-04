class ValidProduct:
    @staticmethod
    def code(user_input):
        if user_input.startswith("P") and len(user_input) >= 3:
            return True
        else:
            return False

    @staticmethod
    def description(user_input):
        if user_input != "":
            return True
        else:
            return False

    @staticmethod
    def price(user_input):
        if 0 < user_input < float("inf"):
            return True
        else:
            return False

    @staticmethod
    def quantity(user_input):
        if user_input > 0:
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
            user_input = input("Digite o nome do produto: ").strip().title()

            if ValidProduct.description(user_input):
                description = user_input
                return description
            else:
                print("Nome inválido. Digite pelo menos 1 caractere.")

    @staticmethod
    def price():
        while True:
            user_input = input("Digite o preço unitário (R$): ").strip()

            try:
                price = float(user_input)
            except ValueError:
                print("ERRO: Digite um número válido para o preço.")
            else:
                if ValidProduct.price(price):
                    return price
                else:
                    print("ERRO: Digite um número válido para o preço.")

    @staticmethod
    def quantity():
        while True:
            user_input = input("Digite a quantidade de unidades do produto: ").strip()

            try:
                quantity = int(user_input)
            except ValueError:
                print("ERRO: Digite um número inteiro positivo para a quantidade.")
            else:
                if ValidProduct.quantity(quantity):
                    return quantity
                else:
                    print("ERRO: Digite um número inteiro positivo para a quantidade.")

    @staticmethod
    def discount(quantity):
        if quantity < 5:
            rate = 0
        elif quantity >= 5 and quantity <= 9:
            rate = 0.05
        elif quantity >= 10 and quantity <= 19:
            rate = 0.10
        else:
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

        gross_value = product["price"] * product["quantity"]
        discount_rate = cls.discount(product["quantity"])
        discount_value = gross_value * discount_rate
        net_value = gross_value - discount_value

        product["discount"] = discount_value

        print(
            f"Subtotal Bruto: R$ {gross_value:.2f} | "
            f"Desconto ({discount_rate * 100:.0f}%): R$ {discount_value:.2f} | "
            f"Líquido: R$ {net_value:.2f}"
        )

        return product


def checkout_manager(shopping_cart, user_name):
    itens_comprados = ", ".join([product["description"] for product in shopping_cart])
    quantidade_total_pecas = sum([product["quantity"] for product in shopping_cart])
    total_bruto = sum([product["price"] * product["quantity"] for product in shopping_cart])
    desconto = sum([product["discount"] for product in shopping_cart])
    total_liquido = total_bruto - desconto

    try:
        preco_medio_por_peca = total_liquido / quantidade_total_pecas
    except ZeroDivisionError:
        preco_medio_por_peca = 0.0

    total_vogais = 0
    for caracter in itens_comprados.lower():
        if caracter in "aeiouáàâãéêíóôõúü":
            total_vogais += 1

    tres_primeiras_letras = user_name[:3].upper()
    letras_invertidas = tres_primeiras_letras[::-1]
    tamanho_nome = len(user_name.replace(" ", ""))
    valor_inteiro = int(total_liquido)
    codigo_fidelidade = f"{letras_invertidas}{tamanho_nome}-{valor_inteiro}"

    print(f"""
==================== EXTRATO FISCAL ====================
Itens Comprados: {itens_comprados}
Quantidade Total de Peças: {quantidade_total_pecas} unidades
Total Bruto: R$ {total_bruto:.2f}
Desconto Total: R$ {desconto:.2f}
VALOR FINAL A PAGAR: R$ {total_liquido:.2f}
Preço Médio por Peça: R$ {preco_medio_por_peca:.2f}
Total de Vogais nos Nomes: {total_vogais} vogais
Nome do Cliente: {user_name}
Código de Fidelidade Gerado: {codigo_fidelidade}
=======================================================
""")


print("=== MERCADOTECH EXPRESS - CAIXA INTELIGENTE ===")
carrinho = []
carrinho.append(RegisterProduct.create_product())

while True:
    pedido_novo_produto = input("Deseja adicionar outro produto? (S/N): ").strip().upper()

    if pedido_novo_produto == "S":
        carrinho.append(RegisterProduct.create_product())
    elif pedido_novo_produto == "N":
        while True:
            user_name = input("Qual seu nome? ").strip().title()
            if len(user_name) >= 3:
                break
            else:
                print("Nome inválido. Digite pelo menos 3 caracteres.")
        break
    else:
        print('Opção inválida, digite apenas "S" ou "N"')

checkout_manager(carrinho, user_name)
