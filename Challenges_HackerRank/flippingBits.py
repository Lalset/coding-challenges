    # O número n é recebido em decimal, mas internamente ele tem uma representação binária de 32 bits.
    
    # É utiliada a operação XOR (^) com 0xFFFFFFFF, que é 11111111 11111111 11111111 11111111 em binário.
    # Como XOR com 1 inverte os bits (0 vira 1 e 1 vira 0), isso faz com que todos os bits de n sejam invertidos.
    
    # O resultado da operação ainda é um número binário de 32 bits, mas o Python automaticamente converte
    # de volta para um número decimal, que é o valor final retornado.

def flippingBits(n):
    return n ^ 0xFFFFFFFF

# Local Mode
# if __name__ == "__main__":
#     q = int(input("How many numbers? ")) 
#     for _ in range(q):
#         n = int(input("Enter a number: ")) 
#         print(flippingBits(n)) 