# Exercicios-prog Entrega1

## Descrição do código.

- O funcionamento do código é simples, através de lógica booleana definida em intervalos que são contabilizados por um contador que contabiliza cada publisher, ela altera as os valores dos objetos da classe twits_mensage. O primeiro operador lógico utiliza faz um circulo que após 17 chamada, entra em outro operador lógico que realiza a rotação em outro intervalo, depois ele inicia uma linha reta que após 2 chamadas realiza mais uma rotação que finaliza dando inicio ao criação de uma nova circunferência menor, que finaliza realizando outra rotação, indo em linha reta e depois parando. Formando assim o desenho de uma pokebola

## Explicação em blocos

### Primeiro bloco condicional

- Até 17 chamadas(uma chamada por segundo) ele mantem a velocidade linear em 1.2 e a angular em 0.5 rad

### Segundo bloco condicional

- A partir da chamada 17 até a 19 ele zera a velocidade linear, mas aumenta a rotação em 0.9 rad. Intervalo abordado [17,19[

### Terceiro bloco condicional

- A partir da chamda 19 até a chamada 20, ele zera a rotação e aumenta a velocidade linear. Intervalo abordado [19,20]

### Quarto bloco condicional

- A partir da chamada 21 até a chamada 25, ele zera a velocidade linear e aumenta a rotação em 0.9 rad. Intervalo abordado ]20, 26[

### Quinto bloco condicional

- A partir da chamada 26 até a chamada 45, ele aumenta a velocidade linear em 0,3 e a rotação em 0.5. Intervalo abordado [26,45]

### Sexto bloco condicional

- A partir da chamada 46 até a chamada 50, ele zera a velocidade linear, mas aumenta a rotação em 0.9 rad. Intervalo abordado ]45,50]

### Sétimo bloco condicional

- Por uma chamada ele zera a rotação e aumenta a velocidade linear em 1.0 Intervalo abordado ]50,51]

### Oitavo bloco condicional

Por fim em qualquer chamada acima da chamada 52 ele zera tanto a velocidade linear quanto a rotação.

![Animação](https://user-images.githubusercontent.com/99265654/234142377-d7bd4aad-80ee-4bb2-8415-2b664b177ee2.gif)

# Exercicios-prog Entrega 2

## Classes

- O código possui duas classes a classe fila que implementas funções para se utilizar uma fila simples e a classe TurtleController que realiza toda a interação dos tópicos para a movimentação do turtlebot

## Funções

- As principais funções da classe fila são a enqueue que adicioona os elementos na fila e a dequeue que retira o primeiro elemento da fila a cada vez que é executado.
- As principais funções da classe TurtleController é a get_position que interage com o tópico /odom pegando a posição atual do turtlebot e a Segue_ponto que interage com o timer para publicar a velocidade e todos os comandos de controle de angulação como o calculo do arco tangente através da diferença entre o ponto foco do turtlebot e o ponto atual do turtlebot.
- Por fim na função principal main() é feito a adição dos pontos dados em um array para a fila que para cada vez que o robo passa por esse ponto ele é retirado da fila de modo que quando a fila esta vazia o robo zera sua velocidade linear e encerra o programa

# Video de funcionamento

## Terminal

![Alt text](Videos/Anima%C3%A7%C3%A3o.gif)

## Gazebo

![Alt text](Videos/turtlebot.gif)

# Exercicio Prog entrega 3

- Para os testes com os modelos convulcionais de rede do yolo v8 é necessário alguns passos a serem seguidos que estão explicados no notebook do colab, contudo irei abordar de maneira sucinta aqui.

1. Pré configuração de ambiente.

   - Para começar o processo de treinamento é necessário garantir que está utilizando a GPU devido ao alto grau de processamento interno a CPU por si só não é suficente sendo necessário utilizar a placa de video. Porntanto, como as placas de video da nividia possuem a integração do software CUDA, é possivel utilizá las para diversas funcionalidades que antes estavam limitadas a apenas uma parte do hardware.

2. Instalação e importação de bibliotecas

   - Para o modelo é necessário utilizar um dataset que será a base de alimentação para o treinamento de indentificação do tipo de imagem que estamos buscando, além de outras bibliotecas que irão auxiliar na visualização das imagens, resultados e diretórios utilizados. Assim nessa etapa será importado e instalado todos os requisitos necessário além do próprio modleo YOLO V8.

3. Treinamento do modelo

   - Nessa etapa é quando criamos o diretório onde iremos colocar o nosso dataset e definir alguns atributos chaves como o numero de épocas que serão utilizadas, a quatidade de imagens que serão avaliadas como base de treino e assim iniciar o processo de treinamento do modelo.

4. Verificação de resultados e teste
   - Por fim, nessa ultima etapa será feito a verificação de alguns resultados do treinamento do modelo como a criação de uma matriz de confusão e imagens que foram utilizadas no treinamento e como foram identificadas. Portanto, feito isso basta testar o modelo com uma imagem externa como é apresentado no gif abaixo

![Alt text](Videos/predictracha.gif)

# Exercicio entrega 4 

## Arquivos 

### Enviar.py
- Este arquivo tem como objetivo fazer a leitura do das imagens publicadas pelo publisher.py utilizando a classe image_subscribe que realiza tópicos a fim de receber e processar o quadros enviados, criando assim um nó para cadavez que uma imagem for recebida ele execute a função listener callback que  converte a mensagem de imagem ROS para uma imagem OpenCV, passa essa imagem pelo modelo YOLO para obter os resultados da detecção de objetos e em seguida, exibe a imagem processada usando cv2.imshow. Assim a imagem codificada em .png e através de uma requisição post http ela é enviada para o servidor local.
### Publisher.py 
- Este arquivo cria um publisher que através do opencv converte um arquivo mp4 em frames e envia eles em um periodo de tempo definido no timer que para um tópico, a cada envio chama a função timer_callback que tem a finalidade de dar um getlogger para cada envio de imagem e verifica se a imagem esta sendo enviada caso não esteja (quando o video acaba) ele reinicia o processo e printa no terminal o processo. 
### Main.py
- Este arquivo tem o objetivo de criar um servidor utilizando o fast API e criar a conexão com o supa base através de atributos como url e key. Além de criar rotas de get para puxar os itens presentes no bucket do supabase, um post para enviar fotos para o supaba e a rota upload que recebe arquvis enviado pelo Client e salvas eles na pasta recebidos. 
## Video da execução dos códigos

![Alt text](Videos/ponderada4.gif)
