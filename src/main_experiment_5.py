from evaluations.evaluator_icl import evaluate_icl_versions

if __name__ == "__main__":
    caminho_entrada = "src/data/questions_and_answers_icl_tecnico.json"
    caminho_saida = "src/results/evaluation_results_icl_with_repetitions_tecnico.json"
    # resultados = evaluate_pairs(caminho_entrada)
    resultados = evaluate_icl_versions(caminho_entrada, caminho_saida, n_repeticoes=20)
    # print("\nAvaliação concluída. Resultados salvos em resultados/resultados_avaliacao.json")