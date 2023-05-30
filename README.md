# genetic_knapsack

generate_individual(): Essa função gera um indivíduo aleatório, representando uma possível solução para o problema da mochila. O indivíduo é um vetor binário onde cada elemento representa a presença (1) ou ausência (0) de um item na mochila. Essa função é utilizada para criar a população inicial.

calculate_fitness(individual): Essa função calcula a aptidão (fitness) de um indivíduo, ou seja, seu valor total considerando o valor dos itens selecionados e levando em conta a capacidade máxima da mochila. Caso a capacidade seja excedida, a aptidão é penalizada para evitar soluções inválidas.

selection(population): Essa função realiza a seleção de pais para a reprodução. Ela utiliza o método da roleta viciada, onde a probabilidade de um indivíduo ser selecionado é proporcional à sua aptidão em relação ao total da aptidão da população.

crossover(parent1, parent2): Essa função realiza o cruzamento (recombinação) entre dois indivíduos (pais) para gerar descendentes (filhos). O cruzamento é feito com base em uma taxa de cruzamento (CROSSOVER_RATE) e utiliza um ponto de corte aleatório para trocar informações genéticas entre os pais.

mutation(individual): Essa função realiza a mutação em um indivíduo. Ela percorre cada gene (elemento do vetor binário) do indivíduo e, com base em uma taxa de mutação (MUTATION_RATE), inverte o valor do gene (1 para 0 ou 0 para 1) aleatoriamente.

genetic_algorithm(): Essa é a função principal que executa o algoritmo genético. Ela começa gerando a população inicial de forma aleatória. Em seguida, itera por um número máximo de gerações (MAX_GENERATIONS) e realiza as seguintes etapas para cada geração:

Avaliação da aptidão dos indivíduos (fitness_scores).
Identificação do melhor indivíduo da geração atual (best_individual) e seu valor de aptidão (best_fitness).
Seleção e cruzamento dos indivíduos para gerar a próxima geração.
Mutação nos descendentes gerados.
Atualização da população com os descendentes.
Após as gerações, a função realiza uma avaliação final da aptidão dos indivíduos e identifica o melhor indivíduo global (melhor solução) e seu valor de aptidão correspondente. Por fim, imprime os resultados.