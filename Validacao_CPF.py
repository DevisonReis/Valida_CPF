def tam_cpf(cpf: str):
	if len(cpf) != 11 or not cpf.isdigit():
		return 'Tamanho do CPF incorreto.'
	else:
		return True
		
def pDigito(cpf: str):
	if len(cpf) > 11 or len(cpf) < 11:
		return False
	else:
		peso = 10
		soma = 0
		for n in range(9):
			soma += int(cpf[n]) * peso
			peso -= 1
		resto = (soma * 10) % 11
		
		if resto == 10:
			resto = 0
		if resto == int(cpf[-2]):
			return True
		else:
			return False
			
def sDigito(cpf: str):
	if len(cpf) > 11 or len(cpf) < 11:
		return False
	else:
		peso = 11
		soma = 0
		for n in range(10):
			soma += int(cpf[n]) * peso
			peso -= 1
		resto = (soma * 10) % 11
		
		if resto == 10:
			resto = 0
		if resto == int(cpf[-1]):
			return True
		else:
			return False

def valida(cpf: str):
	if cpf == cpf[: : -1]:
		return False
		
cpf = input('Informe o CPF: ').replace('.', '').replace('-', '')

tam_cpf(cpf)
pDigito(cpf)
sDigito(cpf)
valida(cpf)

if tam_cpf(cpf) == True and pDigito(cpf) == True and sDigito(cpf) == True:
	print('CPF válido!')
else:
	print('CPF inválido!')
	