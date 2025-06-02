from deepeval.metrics import GEval
from deepeval.metrics.g_eval import Rubric
from deepeval.test_case import LLMTestCaseParams


def get_criteria():
    return [
        GEval(
            name="AdequacaoAoPerfil",
            criteria=(
                "A resposta demonstra estar ajustada ao perfil de quem fez a pergunta? "
                "Considere se a seleção de informações, o foco do conteúdo e a linguagem usada foram moldados de acordo com as possíveis expectativas e necessidades desse perfil."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        GEval(
            name="UsoDeInformacoesRelevantes",
            criteria=(
                "A resposta priorizou informações que são realmente úteis e relevantes para o perfil indicado? "
                "Evite premiar respostas que apenas repetem todos os dados disponíveis sem considerar sua utilidade prática no contexto da pergunta e do perfil."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        GEval(
            name="TomEEstiloAdequado",
            criteria=(
                "O tom e o estilo textual da resposta são apropriados para o perfil informado? "
                "Considere o nível de formalidade, vocabulário, tipo de construção textual e abordagem comunicacional adotada."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        GEval(
            name="ClarezaNaComunicacao",
            criteria=(
                "A resposta é clara, compreensível e bem organizada para o tipo de usuário especificado? "
                "Considere estrutura de parágrafos, encadeamento lógico, fluidez e ausência de ambiguidades ou jargões desnecessários."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        GEval(
            name="PersonalizacaoExplicita",
            criteria=(
                "Há sinais claros de que a resposta foi personalizada com base no perfil do usuário? "
                "Procure por indícios de filtragem seletiva de dados, adaptação de vocabulário ou ênfase em aspectos mais relevantes conforme o contexto do perfil."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        GEval(
            name="SelecaoDeDadosRelevantes",
            criteria=(
                "A resposta apresenta dados que foram claramente escolhidos com critério, conforme o tipo de pergunta e perfil? "
                "Penalize casos em que há inclusão de dados supérfluos ou omissão de pontos centrais para uma boa resposta contextualizada."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        GEval(
            name="AusenciaDeAlucinacoes",
            criteria=(
                "A resposta se limita ao uso de informações apresentadas explicitamente nos dados fornecidos? "
                "Penalize qualquer conteúdo inventado, extrapolado ou que não possa ser verificado nos dados disponíveis."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
    ]


def get_criteria_experiment_1():
    return [
        GEval(
            name="Personalização Perceptível",
            criteria="Avalie se a resposta apresenta sinais claros de adaptação ao perfil do usuário, seja pela linguagem, pelo tom ou pelo tipo de análise fornecida.",
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.CONTEXT,
            ],
            # verbose_mode=True,
            rubric=[
                Rubric(
                    score_range=(0, 2),
                    expected_outcome="A resposta é totalmente genérica, sem qualquer traço de adaptação — nem no tom, nem no conteúdo.",
                ),
                Rubric(
                    score_range=(3, 6),
                    expected_outcome="A personalização é fraca ou ambígua; há um esforço mínimo, mas a resposta ainda parece reaproveitável para qualquer perfil.",
                ),
                Rubric(
                    score_range=(7, 9),
                    expected_outcome="A resposta apresenta personalização clara, por meio do estilo de linguagem ou da adição de conteúdo relevante ao perfil.",
                ),
                Rubric(
                    score_range=(10, 10),
                    expected_outcome="A personalização é inequívoca e ajustada ao perfil, com estilo, conteúdo e tom moldados de forma consistente para o tipo de usuário.",
                ),
            ],
        ),
        GEval(
            name="Alinhamento com Preferências do Perfil",
            criteria="Avalie se a resposta prioriza informações úteis, compreensíveis e valiosas para o perfil informado, considerando o grau de detalhamento esperado.",
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.CONTEXT,
            ],
            # verbose_mode=True,
            rubric=[
                Rubric(
                    score_range=(0, 2),
                    expected_outcome="A resposta ignora as preferências do perfil, como usar linguagem técnica para leigos ou omitir detalhes importantes para profissionais.",
                ),
                Rubric(
                    score_range=(3, 6),
                    expected_outcome="A resposta mistura informações úteis com outras que não interessam ao perfil ou usa um grau de complexidade inadequado.",
                ),
                Rubric(
                    score_range=(7, 9),
                    expected_outcome="A resposta mostra boa seleção de conteúdo, focando nos dados relevantes para o perfil e evitando exageros ou omissões.",
                ),
                Rubric(
                    score_range=(10, 10),
                    expected_outcome="A resposta demonstra entendimento preciso das preferências do perfil, com conteúdo perfeitamente ajustado em tipo e profundidade.",
                ),
            ],
        ),
        GEval(
            name="Consistência da Personalização",
            criteria="Verifique se a personalização está presente de forma coesa em toda a resposta, sem restrição a apenas uma frase inicial ou final.",
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.CONTEXT,
            ],
            # verbose_mode=True,
            rubric=[
                Rubric(
                    score_range=(0, 2),
                    expected_outcome="A personalização está ausente ou aparece de maneira pontual e desconexa.",
                ),
                Rubric(
                    score_range=(3, 6),
                    expected_outcome="A personalização aparece em algumas partes, mas não é sustentada ao longo do texto.",
                ),
                Rubric(
                    score_range=(7, 9),
                    expected_outcome="A personalização está presente de forma consistente, com poucas variações de tom ou foco.",
                ),
                Rubric(
                    score_range=(10, 10),
                    expected_outcome="A resposta mantém um estilo e tom personalizados do início ao fim, com adaptação contínua ao perfil.",
                ),
            ],
        ),
    ]


def get_criteria_experiment_3():
    return [
        GEval(
            name="TomAdequadoAoPerfil",
            criteria=(
                """
Tom Adequado ao Perfil (1–10) — avalia o quanto o tom da resposta está alinhado ao perfil do usuário indicado. O tom inclui o estilo da linguagem, as expressões utilizadas e a atitude comunicativa geral da resposta.

Um tom bem alinhado reflete as expectativas comunicativas típicas do perfil. Isso pode envolver o uso de expressões características, terminologia específica, grau de formalidade, entusiasmo ou objetividade, conforme apropriado ao perfil em questão.

**Notas altas (8–10)** devem ser atribuídas **somente quando**:
- O tom e o estilo são claramente coerentes com o perfil ao longo de toda a resposta.
- Há uso de expressões, comentários ou construções que indicam forte alinhamento ao papel assumido pelo usuário (ex: termos técnicos, linguagem emocional, informalidade ou formalidade conforme o caso).
- A personalização é distribuída e **sustentada**, não restrita a um único trecho.

**Notas intermediárias (4–7)** devem ser atribuídas quando:
- A resposta possui **alguns elementos de personalização**, mas o tom predominante ainda é genérico ou neutro.
- A adaptação ao perfil está presente, mas é **pontual**, sutil ou restrita a frases isoladas.
- Há tentativa de personalização, mas sem consistência no tom ao longo da resposta.

**Notas baixas (1–3)** devem ser atribuídas quando:
- O tom é completamente genérico, técnico ou neutro, sem qualquer sinal claro de adaptação ao perfil.
- A resposta parece padronizada e não demonstra esforço para se adequar ao interlocutor indicado.

Este critério busca recompensar respostas que incorporam de forma consciente o papel esperado para o perfil e penalizar aquelas que não expressam variação adequada de linguagem ou atitude comunicativa.
"""
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.CONTEXT,
            ],
            verbose_mode=True,
        ),
        GEval(
            name="QuantidadeDeInformacoesParaOPerfil",
            criteria=(
                """
Quantidade de Informações Relevantes (1–10) — avalia o quanto a resposta apresenta conteúdo informativo denso, específico e útil, considerando as necessidades informacionais do perfil de usuário.

**Notas altas (8–10)** devem ser atribuídas **somente quando**:
- A resposta contém múltiplos dados objetivos extraídos da base (ex: valores numéricos, nomes de jogadores, métricas específicas).
- Os dados estão contextualizados de forma útil e alinhada ao perfil (ex: explicações ou comparações que ajudem o usuário a interpretar os dados).
- A densidade informacional é alta e atende de forma clara a complexidade da pergunta.

**Notas intermediárias (4–7)** devem ser atribuídas quando:
- A resposta traz **alguns dados úteis**, mas não os explora completamente ou deixa de contextualizá-los para o perfil.
- Pode haver uma predominância de informações genéricas com apenas uma ou duas menções mais específicas.
- A resposta responde à pergunta, mas poderia ter sido mais rica.

**Notas baixas (1–3)** devem ser atribuídas quando:
- A resposta é vaga, genérica ou meramente opinativa, com pouca ou nenhuma evidência quantitativa.
- Os dados estão ausentes ou são irrelevantes para o perfil e o tipo de pergunta.
- Falta substância informacional para sustentar uma boa análise para o usuário.
"""
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.CONTEXT,
            ],
            verbose_mode=True,
        ),
        GEval(
            name="PersonalizacaoPerceptivel",
            criteria=(
                """
Personalização Perceptível (1–10) — avalia o quanto a resposta vai além da apresentação de dados crus e molda o conteúdo à perspectiva e interesses do perfil indicado.

**Notas altas (8–10)** devem ser atribuídas **somente quando**:
- A resposta contextualiza os dados com comentários, interpretações ou explicações que fazem sentido específico para o perfil.
- A linguagem e o foco da resposta indicam que a informação foi moldada pensando no papel e nas preocupações daquele tipo de usuário.
- Há esforço explícito em transformar os dados em conhecimento útil sob a ótica do perfil.

**Notas intermediárias (4–7)** devem ser atribuídas quando:
- A resposta contém **alguma tentativa de contextualização**, mas ela é superficial ou genérica.
- O dado é relevante, mas a resposta não se aprofunda nas implicações ou usos potenciais para o perfil.
- Há traços de personalização, mas não sustentados ao longo da resposta.

**Notas baixas (1–3)** devem ser atribuídas quando:
- A resposta apenas apresenta os dados de forma direta e genérica, sem qualquer adaptação à perspectiva do perfil.
- A linguagem e o conteúdo parecem indiferenciados, como se fossem direcionados a qualquer pessoa.
- Não há esforço evidente de personalização ou contextualização.
"""
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.CONTEXT,
            ],
            verbose_mode=True,
        ),
    ]


def get_criteria_experiment_4():
    return [
        # Alucinação interpretativa
        GEval(
            name="InferenciasNaoJustificadas",
            criteria=(
                """Inferências Não Justificadas (1–10) — avalia o quanto a resposta evita interpretações subjetivas, julgamentos ou conclusões que não estejam sustentadas pelos dados apresentados.

**Notas altas (8–10)** devem ser atribuídas **somente quando**:
- A resposta se limita a relatar os dados de forma objetiva.
- Não há inferências sobre esforço, desempenho, importância, ou qualquer avaliação subjetiva que vá além do que os dados sustentam.
- A linguagem é descritiva e fundamentada.

**Notas intermediárias (4–7)** devem ser atribuídas quando:
- A resposta contém **algumas interpretações ou adjetivações subjetivas**, mas que ainda mantêm certo alinhamento com os dados apresentados.
- Ex: dizer que um jogador "teve boa atuação" sem dados claros, mas com algum apoio implícito.

**Notas baixas (1–3)** devem ser atribuídas quando:
- A resposta está repleta de inferências não justificadas, como:
    - "Foi essencial para o time"
    - "Mostrou grande liderança"
    - "Se destacou claramente"
  ...sem apresentar métricas, comparações ou dados que embasem tais afirmações.
- A subjetividade domina a resposta sem conexão clara com evidências.
"""
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.CONTEXT,
            ],
        ),
        # Alucinação contextual
        GEval(
            name="CoerenciaComPerfil",
            criteria=(
                """Coerência com o Perfil (1–10) — avalia se o estilo de escrita, o vocabulário e o foco da resposta estão compatíveis com o perfil informado.

**Notas altas (8–10)** devem ser atribuídas **somente quando**:
- A linguagem, o estilo e os pontos enfatizados são claramente adequados ao perfil (ex: técnico, torcedor, jornalista).
- Não há jargões excessivos para perfis leigos nem informalidades para perfis técnicos.
- A resposta adota uma abordagem coerente do início ao fim com o tipo de usuário.

**Notas intermediárias (4–7)** devem ser atribuídas quando:
- A maior parte da resposta está adequada, mas há pequenos deslizes no vocabulário, foco ou nível de formalidade.
- Pode haver uma frase que soe deslocada, mas o restante está alinhado.

**Notas baixas (1–3)** devem ser atribuídas quando:
- A resposta usa linguagem técnica com um perfil leigo (ex: torcedor) ou linguagem informal/opinativa com um perfil técnico (ex: fisioterapeuta).
- Há desalinhamento claro entre o conteúdo apresentado e o que seria esperado para o tipo de usuário.
- O foco da resposta foge das prioridades típicas do perfil.
"""
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
                LLMTestCaseParams.CONTEXT,
            ],
        ),
    ]
