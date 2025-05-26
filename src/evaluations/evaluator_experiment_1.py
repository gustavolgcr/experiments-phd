import json
from deepeval.test_case import LLMTestCase
from evaluations.criteria import get_criteria_experiment_1

def evaluate_with_repetitions(path_json: str, path_output: str, n_repeticoes: int = 5):
    with open(path_json, 'r', encoding='utf-8') as f:
        exemplos = json.load(f)

    criterios = get_criteria_experiment_1()
    resultados = []

    for exemplo in exemplos:
        print(f"Avaliando: {exemplo['pergunta']} - Perfil: {exemplo['perfil']}")
        entrada = f"Pergunta: {exemplo['pergunta']}\nPerfil do usuário: {exemplo['perfil']}"

        for criterio in criterios:
            scores_padrao = []
            scores_personalizada = []

            for _ in range(n_repeticoes):
                # Resposta padrão (sem Tailor)
                caso_padrao = LLMTestCase(input=entrada, actual_output=exemplo["resposta_padrao"])
                criterio.measure(caso_padrao)
                scores_padrao.append(round(criterio.score * 10, 2))

                # Resposta personalizada (com Tailor)
                caso_personalizada = LLMTestCase(input=entrada, actual_output=exemplo["resposta_personalizada"])
                criterio.measure(caso_personalizada)
                scores_personalizada.append(round(criterio.score * 10, 2))

            resultados.append({
                "pergunta": exemplo["pergunta"],
                "perfil": exemplo["perfil"],
                "criterio": criterio.name,
                "scores_resposta_padrao": scores_padrao,
                "scores_resposta_personalizada": scores_personalizada
            })

    with open(path_output, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

    return resultados