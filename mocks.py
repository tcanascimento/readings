class Mocks:

    @staticmethod
    def lista_vazia():
        return []

    @staticmethod
    def lista_base():
        return [1,2,3,4]

    @staticmethod
    def msg_valores_diferentes():
        return "Valores diferentes!"

    @staticmethod
    def msg_erro_lista_vazia():
        return "Erro em lista vazia!"

    @staticmethod
    def expected_found():
        return lambda : (
            (0, []),
            (10, [1,2,3,4]),
            (4, [1,1,2]),
            (0, [1,2,-3]),
            (-1, [1,2,1,-5]),
            (1, [1,0,-1,1]),
            (1001, [1,1001,-1]),
            (999, [1000,-1])
        )