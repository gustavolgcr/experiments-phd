import json
# from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from evaluations.criteria import get_criteria

def evaluate_pairs(path_json):
    with open(path_json, 'r') as f:
        exemplos = json.load(f)

    criterios = get_criteria()
    resultados = []

    for exemplo in exemplos:
        dados_tool_personareact = json.dumps(exemplo.get("dados_personareact", {}), indent=2, ensure_ascii=False)
        dados_tool_react = json.dumps(exemplo.get("dados_react", {}), indent=2, ensure_ascii=False)
        entrada = f"""Pergunta: {exemplo['pergunta']}\nPerfil do usuário: {exemplo['perfil']}\n\n[DADOS DISPONÍVEIS PARA A RESPOSTA]:\n"""
        # entrada = f"{exemplo['pergunta']} Perfil: {exemplo['perfil']}"

        for criterio in criterios:
            # Avaliação da resposta do PersonaReAct
            caso_personareact = LLMTestCase(
                input=entrada + dados_tool_personareact,
                actual_output=exemplo["resposta_personareact"]
            )
            criterio.verbose_mode = True
            
            criterio.measure(caso_personareact)
            evaluation_steps = criterio.evaluation_steps
            score_personareact = round(criterio.score * 10, 2)
            reason_personareact = criterio.reason
            
            # Avaliação da resposta do ReAct com Prompt Enriquecido
            caso_react_prompt = LLMTestCase(
                input=entrada + dados_tool_react,
                actual_output=exemplo["resposta_react_prompt"]
            )
            criterio.measure(caso_react_prompt)
            score_react_prompt = round(criterio.score * 10, 2)
            reason_react_prompt = criterio.reason
            
            percent_diff = 100 * (score_personareact - score_react_prompt) / (score_react_prompt + 1e-8)

            vencedor = "Empate"
            if score_personareact > score_react_prompt:
                vencedor = "PersonaReAct"
            elif score_react_prompt > score_personareact:
                vencedor = "ReAct com Prompt Enriquecido"

            resultados.append({
                "pergunta": exemplo["pergunta"],
                "perfil": exemplo["perfil"],
                "criterio": criterio.name,
                "evaluation_steps": evaluation_steps,
                "score_personareact": score_personareact,
                "reason_personareact": reason_personareact,
                "score_react_prompt": score_react_prompt,
                "reason_react_prompt": reason_react_prompt,
                "percentual_ganho_personareact": round(percent_diff, 2),
                "vencedor": vencedor
            })

    with open("src/results/evaluation_results.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

    return resultados

def evaluate_with_repetitions(path_json: str, path_output: str, n_repeticoes: int = 5):
    with open(path_json, 'r', encoding='utf-8') as f:
        exemplos = json.load(f)

    criterios = get_criteria()
    resultados = []

    for exemplo in exemplos:
        dados_tool_personareact = json.dumps(exemplo.get("dados_personareact", {}), indent=2, ensure_ascii=False)
        dados_tool_react = json.dumps(exemplo.get("dados_react", {}), indent=2, ensure_ascii=False)
        entrada = f"""Pergunta: {exemplo['pergunta']}\nPerfil do usuário: {exemplo['perfil']}\n\n[DADOS DISPONÍVEIS PARA A RESPOSTA]:\n"""

        for criterio in criterios:
            scores_personareact = []
            scores_react_prompt = []

            for _ in range(n_repeticoes):
                # PersonaReAct
                caso_personareact = LLMTestCase(
                    input=entrada + dados_tool_personareact,
                    actual_output=exemplo["resposta_personareact"]
                )
                criterio.measure(caso_personareact)
                scores_personareact.append(round(criterio.score * 10, 2))  # escala de 0–10

                # ReAct com Prompt Enriquecido
                caso_react_prompt = LLMTestCase(
                    input=entrada + dados_tool_react,
                    actual_output=exemplo["resposta_react_prompt"]
                )
                criterio.measure(caso_react_prompt)
                scores_react_prompt.append(round(criterio.score * 10, 2))

            resultados.append({
                "pergunta": exemplo["pergunta"],
                "perfil": exemplo["perfil"],
                "criterio": criterio.name,
                "scores_personareact": scores_personareact,
                "scores_react_prompt": scores_react_prompt
            })

    with open(path_output, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

    return resultados