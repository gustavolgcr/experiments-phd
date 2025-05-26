import json
from deepeval.test_case import LLMTestCase
from evaluations.criteria import get_criteria  # Certifique-se de ter esse arquivo em sua estrutura de projeto

def evaluate_icl_versions(path_json: str, path_output: str, n_repeticoes: int = 5):
    with open(path_json, 'r', encoding='utf-8') as f:
        exemplos = json.load(f)

    criterios = get_criteria()
    resultados = []

    for exemplo in exemplos:
        print(f"Avaliando exemplo: {exemplo['pergunta']}")
        entrada = f"Pergunta: {exemplo['pergunta']}\nPerfil: {exemplo['perfil']}\n"

        for criterio in criterios:
            scores_zero = []
            scores_one = []
            scores_few = []

            for _ in range(n_repeticoes):
                # Zero-shot
                caso_zero = LLMTestCase(input=entrada, actual_output=exemplo["resposta_zero_shot"])
                criterio.measure(caso_zero)
                scores_zero.append(round(criterio.score * 10, 2))

                # One-shot
                caso_one = LLMTestCase(input=entrada, actual_output=exemplo["resposta_one_shot"])
                criterio.measure(caso_one)
                scores_one.append(round(criterio.score * 10, 2))

                # Few-shot
                caso_few = LLMTestCase(input=entrada, actual_output=exemplo["resposta_few_shot"])
                criterio.measure(caso_few)
                scores_few.append(round(criterio.score * 10, 2))

            resultados.append({
                "pergunta": exemplo["pergunta"],
                "perfil": exemplo["perfil"],
                "criterio": criterio.name,
                "scores_zero_shot": scores_zero,
                "scores_one_shot": scores_one,
                "scores_few_shot": scores_few
            })

    with open(path_output, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

    return resultados