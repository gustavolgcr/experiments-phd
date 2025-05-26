from deepeval.metrics import GEval
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
            name="FocoRelevanteAoPerfil",
            criteria=(
                "A resposta enfatiza as informações mais relevantes para o perfil indicado?\n\n"
                "✔️ Exemplo (perfil: Técnico):\n"
                "Foco em desempenho tático, distribuição em campo, variações de intensidade, posicionamento.\n"
                "✔️ Exemplo (perfil: Torcedor):\n"
                "Foco em impacto geral no jogo, emoção, destaque individual, efeito sobre o placar.\n\n"
                "❌ Ruins: Respostas genéricas que poderiam servir para qualquer perfil ou que misturam informações irrelevantes para o perfil indicado."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        GEval(
            name="AdequacaoDeLinguagemAoPerfil",
            criteria=(
                "A linguagem usada na resposta está adequada ao perfil indicado, considerando tom, formalidade e vocabulário?\n\n"
                "✔️ Exemplo:\n"
                "- Perfil: Torcedor → linguagem mais entusiasmada, informal, direta (ex.: 'o cara arrebentou no jogo!').\n"
                "- Perfil: Técnico → vocabulário analítico, técnico (ex.: 'a média de acelerações sugere sobrecarga na transição ofensiva').\n\n"
                "❌ Ruins: Linguagem excessivamente neutra ou incongruente com o perfil (ex.: usar jargões táticos com perfil de criança ou torcedor casual)."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        GEval(
            name="OrganizacaoTextualEClareza",
            criteria=(
                "A resposta apresenta estrutura clara e bem organizada para facilitar a leitura pelo perfil indicado?\n\n"
                "✔️ Esperado:\n"
                "- Frases curtas e diretas para perfis leigos.\n"
                "- Parágrafos organizados por ideia (ex.: primeiro dados, depois interpretação).\n"
                "- Uso de conectores que ajudam na fluidez.\n\n"
                "❌ Ruins:\n"
                "- Frases longas e confusas, ou estrutura que mistura dados e interpretações sem transição.\n"
                "- Linguagem truncada ou repetitiva que dificulta a leitura."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        GEval(
            name="PersonalizacaoDetectavel",
            criteria=(
                "A resposta apresenta elementos perceptíveis de personalização, demonstrando adaptação ao perfil do usuário?\n\n"
                "✔️ Indicadores:\n"
                "- Referência direta ao perfil (ex.: 'como torcedor, você pode gostar de saber que...').\n"
                "- Escolha seletiva de dados com justificativa voltada ao perfil.\n"
                "- Mudança de ênfase ou linguagem comparado a outro perfil.\n\n"
                "❌ Ruins:\n"
                "- Respostas que parecem copiadas para qualquer perfil.\n"
                "- Nenhuma adaptação aparente na linguagem ou foco."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
    ]


def get_criteria_experiment_4():
    return [
        # Alucinação interpretativa
        GEval(
            name="InferenciasNaoJustificadas",
            criteria=(
                "A resposta apresenta inferências, julgamentos ou interpretações que não estão diretamente sustentadas pelos dados apresentados?\n"
                "Exemplos incluem:\n"
                "- Atribuições de comprometimento, liderança, esforço ou importância tática sem evidência explícita.\n"
                "- Frases como 'isso demonstra dedicação', 'foi essencial para o time', 'claramente se destacou', se não há dado que comprove.\n"
                "\n"
                "Se a resposta apenas relatar os dados, sem extrapolar, atribua nota máxima.\n"
                "Quanto mais subjetiva e interpretativa for a resposta sem base nos dados apresentados, menor deve ser a nota."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
        # Alucinação contextual
        GEval(
            name="CoerenciaComPerfil",
            criteria=(
                "A resposta está escrita com o estilo, vocabulário e foco compatíveis com o perfil do usuário informado?\n"
                "\n"
                "Considere como inadequações:\n"
                "- Uso de linguagem técnica ou jargões táticos com perfis leigos (ex: torcedor).\n"
                "- Uso de expressões emocionais, informais ou opinativas com perfis técnicos (ex: técnico, fisioterapeuta).\n"
                "- Ênfase fora do foco típico do perfil (ex: falar de empolgação e torcida para um técnico).\n"
                "\n"
                "Quanto mais a resposta se adequa ao perfil esperado, maior deve ser a nota.\n"
                "Quanto mais desalinhada em termos de tom, foco ou vocabulário, menor a nota."
            ),
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
        ),
    ]
