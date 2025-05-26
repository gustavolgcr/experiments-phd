from evaluations.evaluator import evaluate_pairs, evaluate_with_repetitions

if __name__ == "__main__":
    caminho_entrada = "src/data/questions_and_answers_tecnico.json"
    caminho_saida = "src/results/evaluation_results_with_repetitions_tecnico.json"
    # resultados = evaluate_pairs(caminho_entrada)
    resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida)
    # print("\nAvaliação concluída. Resultados salvos em resultados/resultados_avaliacao.json")