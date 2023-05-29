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
## Classe 
 - O código possui duas classse a classe fila que implementas funções para se utilizar uma fila simples e a classe TurtleController que realiza toda a interação dos tópicos para a movimentação do turtlebot 
 ## Funções 
 - As principais funções da classe fila são a enqueue que adicioona os elementos na fila e a dequeue que retira o primeiro elemento da fila a cada vez que é executado.
 - As principais funções da classe TurtleController é a get_position que interage com o tópico /odom pegando a posição atual do turtlebot e a Segue_ponto que interage com o timer para publicar a velocidade e todos os comandos de controle de angulação como o calculo do arco tangente através da diferença entre o ponto foco do turtlebot e o ponto atual do turtlebot.
 - Por fim na função principal main() é feito a adição dos pontos dados na fila que para cada vez que o robo passa por esse ponto ele é retirado da fila de modo que quando a fila esta vazia o robo zera sua velocidade linear e encerra o programa 
 # Video de funcionamento 
 
