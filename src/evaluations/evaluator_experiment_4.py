import json
from deepeval.test_case import LLMTestCase
from evaluations.criteria import get_criteria_experiment_4  # Deve conter os dois critérios novos

def evaluate_experiment_4(path_json: str, path_output: str, n_repeticoes: int = 5):
    with open(path_json, 'r', encoding='utf-8') as f:
        exemplos = json.load(f)

    criterios = get_criteria_experiment_4()
    resultados = []

    for exemplo in exemplos:
        print(f"Avaliando: {exemplo['pergunta']} - Perfil: {exemplo['perfil']}")

        entrada = (
            f"Pergunta: {exemplo['pergunta']}\n"
            f"Perfil do usuário: {exemplo['perfil']}\n"
            f"Observações baseadas nos dados reais: {exemplo['observação']}"
        )

        for criterio in criterios:
            scores = []

            for _ in range(n_repeticoes):
                caso = LLMTestCase(
                    input=entrada,
                    actual_output=exemplo["resposta"]
                )
                criterio.measure(caso)
                scores.append(round(criterio.score * 10, 2))  # escala de 0–10

            resultados.append({
                "pergunta": exemplo["pergunta"],
                "perfil": exemplo["perfil"],
                "criterio": criterio.name,
                "scores": scores
            })

    with open(path_output, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

    return resultados