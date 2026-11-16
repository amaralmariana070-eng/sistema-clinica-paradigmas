
class Consulta:

    
    def __init__(self, paciente, especialidade, valor, tem_convenio):
        self.paciente = paciente
        self.especialidade = especialidade
        self.__valor = valor  # Atributo privado (Encapsulamento)
        self.tem_convenio = tem_convenio

    
    def calcular_valor_final(self):
        if self.tem_convenio:
            return self.__valor * 0.70
        return self.__valor

    
    def exibir_dados(self):
        tipo = "Convênio (30% OFF)" if self.tem_convenio else "Particular"
        valor_final = self.calcular_valor_final()
        print(
            f"Paciente: {self.paciente} | Especialidade: {self.especialidade} "
            f"| Tipo: {tipo} | Valor: R$ {valor_final:.2f}"
        )



agenda = []  

while True:
    print("\n=== CLÍNICA MÉDICA (POO) ===")
    print("1 - Agendar Consulta")
    print("2 - Listar Consultas")
    print("3 - Ver Faturamento Total")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do paciente: ")
        esp = input("Especialidade: ")
        valor = float(input("Valor base da consulta (R$): "))
        conv = input("Possui convênio? (s/n): ").lower()

        if valor <= 0:
            print("[ERRO] O valor deve ser maior que zero!")
        else:
            tem_convenio = conv == "s"
            
            nova_consulta = Consulta(nome, esp, valor, tem_convenio)
            agenda.append(nova_consulta)
            print("[SUCESSO] Consulta agendada!")

    elif opcao == "2":
        print("\n--- CONSULTAS AGENDADAS ---")
        if len(agenda) == 0:
            print("Nenhuma consulta cadastrada.")
        else:
            for consulta in agenda:
                # Chamando o método do próprio objeto
                consulta.exibir_dados()

    elif opcao == "3":
        total = 0
        for consulta in agenda:
            total += consulta.calcular_valor_final()
        print(f"\nFaturamento Total Previsto: R$ {total:.2f}")

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("[ERRO] Opção inválida! Tente novamente.")
