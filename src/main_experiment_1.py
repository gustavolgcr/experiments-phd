from evaluations.evaluator_experiment_1 import evaluate_with_repetitions

if __name__ == "__main__":
    caminho_entrada = "src/data/questions_and_answers_experiment_1.json"
    caminho_saida = "src/results/evaluation_results_with_repetitions_experiment_1.json"

    resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=1)
