from evaluations.evaluator_experiment_4 import evaluate_experiment_4

if __name__ == "__main__":
    caminho_entrada = "src/data/questions_and_answers_experiment_4.json"
    caminho_saida = "src/results/evaluation_results_icl_with_repetitions_experiment_4.json"
    # resultados = evaluate_pairs(caminho_entrada)
    resultados = evaluate_experiment_4(caminho_entrada, caminho_saida, n_repeticoes=20)
    # print("\nAvaliação concluída. Resultados salvos em resultados/resultados_avaliacao.json")