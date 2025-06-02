from evaluations.evaluator import evaluate_pairs, evaluate_with_repetitions

if __name__ == "__main__":
    
    print("Analisando o perfil Torcedor do Time.")
    caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_torcedor.json"
    caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_torcedor.json"
    resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)
    
    print("Analisando o perfil Técnico do Time.")
    caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_tecnico.json"
    caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_tecnico.json"
    resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)
    
    print("Analisando o perfil Narrador de Jogo de Futebol.")
    caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_narrador.json"
    caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_narrador.json"
    resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)
    
    # print("Analisando o perfil Torcedor do Time - Factual Direta.")
    # caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_torcedor_factual_direta.json"
    # caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_torcedor_factual_direta_verbose.json"
    # resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=1)
    
    # print("Analisando o perfil Torcedor do Time - Narrativa Descritiva.")
    # caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_torcedor_narrativa_descritiva.json"
    # caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_torcedor_narrativa_descritiva.json"
    # resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)
    
    # print("Analisando o perfil Comissão Técnica do Time - Factual Direta.")
    # caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_comissao_factual_direta.json"
    # caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_comissao_factual_direta.json"
    # resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)
    
    # print("Analisando o perfil Comissão Técnica do Time - Narrativa Descritiva.")
    # caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_comissao_narrativa_descritiva.json"
    # caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_comissao_narrativa_descritiva.json"
    # resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)
    
    # print("Analisando o perfil Jornalista Esportivo - Factual Direta.")
    # caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_jornalista_factual_direta.json"
    # caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_jornalista_factual_direta.json"
    # resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)
    
    # print("Analisando o perfil Jornalista Esportivo - Narrativa Descritiva.")
    # caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_jornalista_narrativa_descritiva.json"
    # caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_jornalista_narrativa_descritiva.json"
    # resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)
    
    # print("Analisando o perfil Árbitro do Jogo - Factual Direta.")
    # caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_arbitro_factual_direta.json"
    # caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_arbitro_factual_direta.json"
    # resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)
    
    # print("Analisando o perfil Árbitro do Jogo - Narrativa Descritiva.")
    # caminho_entrada = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/data/experiment_3/questions_and_answers_experiment_3_arbitro_narrativa_descritiva.json"
    # caminho_saida = "/Users/gustavolgcr/doutorado/implementacoes/experiments/src/results/experiment_3/evaluation_results_with_repetitions_experiment_3_arbitro_narrativa_descritiva.json"
    # resultados = evaluate_with_repetitions(caminho_entrada, caminho_saida, n_repeticoes=20)