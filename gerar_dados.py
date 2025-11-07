import random
import faker
import pandas as pd
from datetime import datetime, timedelta

# Criando uma instância do Faker para gerar dados realistas
fake = faker.Faker()

# Função para gerar a data aleatória
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Função para gerar os registros
def generate_data(num_records):
    data = []
    start_date = datetime(2025, 10, 1)
    end_date = datetime(2025, 10, 31)
    
    for i in range(num_records):
        aluno_id = i + 1
        nome = fake.name()
        sexo = random.choice(["M", "F", "Outro"])
        idade = random.randint(18, 60)
        data_cadastro = random_date(start_date, end_date).strftime('%d/%m/%Y')
        
        # Gerar treino
        data_treino = random_date(start_date, end_date).strftime('%d/%m/%Y')
        horario_entrada = random.randint(6, 20)
        horario_saida = horario_entrada + random.randint(1, 2)  # Diferença de 60 a 90 minutos
        duracao_treino = horario_saida - horario_entrada
        tipo_treino = random.choice(["Musculação", "Funcional", "Cardio"])
        equipamento_usado = random.choice(["Halteres", "Esteira", "Leg Press", "Supino", "Máquinas de Puxada"])
        tempo_uso_equipamento = random.randint(10, 60)
        ocupacao_equipamento = random.randint(30, 100)
        
        carga_media_kg = random.randint(10, 150) if tipo_treino == "Musculação" else None
        evolucao_treino = random.randint(0, 20)
        
        # Feedback
        nota_satisfacao = random.randint(7, 10)
        promotor = 1 if nota_satisfacao >= 9 else 0
        
        # Status e Plano
        status_aluno = random.choice(["Ativo", "Inativo", "Desistente"])
        plano = random.choice(["Mensal", "Trimestral", "Semestral", "Anual"])
        
        # Adicionando o registro na lista
        data.append([
            aluno_id, nome, sexo, idade, data_cadastro,
            data_treino, horario_entrada, horario_saida, duracao_treino,
            tipo_treino, equipamento_usado, tempo_uso_equipamento, ocupacao_equipamento,
            carga_media_kg, evolucao_treino, nota_satisfacao, promotor,
            status_aluno, plano
        ])
    
    # Criando o DataFrame do Pandas
    df = pd.DataFrame(data, columns=[
        "AlunoID", "NomeAluno", "Sexo", "Idade", "DataCadastro",
        "DataTreino", "HorarioEntrada", "HorarioSaida", "DuracaoTreinoMin",
        "TipoTreino", "EquipamentoUsado", "TempoUsoEquipamentoMin", "OcupacaoEquipamento",
        "CargaMediaKg", "EvolucaoTreino%", "NotaSatisfacao", "Promotor",
        "StatusAluno", "Plano"
    ])
    
    # Salvando o arquivo XLSX
    file_path = 'academia_fitness_x.xlsx'
    df.to_excel(file_path, index=False)
    
    return file_path

# Gerando o arquivo com 5000 registros
generate_data(5000)
