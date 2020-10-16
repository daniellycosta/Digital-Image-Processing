---
id: doc1
title: Exercícios da 1ª Unidade
sidebar_label: Example Page
---

Exercícios **2 - 6** encontrados na página do professor [Agostinho Brito](https://agostinhobritojr.github.io/tutorial/pdi/)

## Região Negativa

O exercício encontrado na [seção 2.2](https://agostinhobritojr.github.io/tutorial/pdi/#_exerc%C3%ADcios) pede para que dado uma imagem e dois pontos, uma região seja traçada e exibida com o negativo da imagem.

Para isso, foi convencionado que a entrada do algoritmo seria escrito como mostrado logo abaixo:

`python3 setup.py <path_da_imagem> <coord_x_p1> <coord_y_p1> <coord_x_p2> <coord_y_p2>`

Antes do processamento é necessário garantir que todas as entradas sejam fornecidas bem como garantir que os pontos se encontrem dentro da imagem. O trecho de código abaixo mostram como esses tratamentos foram feitos.

```python
if len(sys.argv) < 6:
    sys.exit("Missing parameters")

if img is None:
    sys.exit("Could not read the image")

rows, columns = img.shape

if p1[0] > rows or p1[1] > columns:
    sys.exit(f"P1 should be inside the picture dimensions ({rows}X{columns})")
if p2[0] > rows or p2[1] > columns:
    sys.exit(f"P2 should be inside the picture dimensions ({rows}X{columns})")

if p1[0] > p2[0]:
    sys.exit(f"P1 x coordinate should be lower than P2 x coordinate")
if p1[1] > p2[1]:
    sys.exit(f"P1 y coordinate should be lower than P2 y coordinate")
```

Passando do estágio de verificação, o negativo da região passada é obtido percorrendo os _pixels_ da região trocando o seu valor pelo complemento conforme demonstrado no trecho de código abaixo.

```python
for i in range(p1[0], p2[0]):
    for j in range(p1[1], p2[1]):
        img[i][j] = 1-img[i][j]
```

Fazendo isso, o resultado será a imagem com a região escolhida em negativo

<center>
<figure float="middle" class="image">
  <img src="./assets/biel.png" alt="biel.png">
  <figcaption>Figura 1 - Imagem de entrada</figcaption> 
</figure>
<figure class="image">
  <img src="./assets/regions_out.png" alt="regions_out.png">
  <figcaption>Figura 2 - Imagem de Saída com os pontos P1(10,10) e P2(100,220)</figcaption>  
</figure>
</center>

## Troca de Regiões

Nesse exercício, foi pedido para que passando uma imagem, os quadrantes sejam trocados nas diagonais. Para isso, foi convencionado que a imagem seria passada pelo terminal na hora da execução utilizando-se do comando abaixo.

<center>
`python3 setup.py <path_da_imagem>`
</center>

Após a imagem ser processada com sucesso, foi obtido o _pixel_ de separação dos quadrantes. Considerando que as imagens passadas serão quadradas o _pixel_ de separação foi obtido utilizando-se do seguinte algoritmo.

```python
row_limit = int(rows/2)
columns_limit = int(columns/2)
```

Uma vez obtidos os _pixels_ de separação, as quatro regiões (quadrantes) da imagem foram obtidos da seguinte forma

```python
region1 = img[0:row_limit, 0:columns_limit]
region2 = img[0:row_limit, columns_limit:columns]
region3 = img[row_limit:rows, 0:columns_limit]
region4 = img[row_limit:rows, columns_limit:columns]
```

Por fim, os quadrantes foram concatenados na nova ordem formando a imagem de saída conforme mostrado no trecho de código e nas Figuras 3 e 4 abaixo

```python
upper_img = cv.hconcat([region4, region3])
lower_img = cv.hconcat([region2, region1])

out_img = cv.vconcat([upper_img, lower_img])
```

<center>
<figure float="middle" class="image">
  <img src="./assets/biel.png" alt="biel.png">
  <figcaption>Figura 3 - Imagem de entrada</figcaption> 
</figure>
<figure class="image">
  <img src="./assets/change_regions_out.png" alt="change_regions_out.png">
  <figcaption>Figura 4 - Imagem de Saída com os quadrantes trocados</figcaption>  
</figure>
</center>

## Labeling

O exercício de labeling, no tópico de [preenchimentos de regiões](https://agostinhobritojr.github.io/tutorial/pdi/#_exerc%C3%ADcios_2), pergunta em seu primeiro tópico, o que acontece caso se tenha mais de 255 objetos na cena e a solução.

Observando o algoritmo de [labeling](https://agostinhobritojr.github.io/tutorial/pdi/exemplos/labeling.cpp) é possível perceber que ao exceder uma quantidade de objetos de 255, o programa original irá ter uma falha ao tentar preencher um tom de cinza inexistente na imagem. Para solucionar esse problema passou-se a utilizar o resto da divisão do contador por 254 somado de um como o tom de cinza do objeto e passamos a incrementação do contador para depois da decisão do tom de cinza, assim teremos tons de cinza variando entre 1 e 254.

No segundo ponto do exercício é pedido para que se aprimore o algoritmo de modo a não contar bolhas que tocam as bordas da imagem e identificar bolhas com ou sem buracos internos, considerando ainda que podem existir regiões com mais de um buraco.

<center>
<figure float="middle" class="image">
  <img src="./assets/bolhas.png" alt="bolhas.png">
  <figcaption>Figura 5 - Imagem utilizada como entrada</figcaption> 
</figure>
</center>

Na solução feita, inicialmente as bordas da imagem (Figura 5) foram limpas utilizando-se do método _foodFill_ , conforme pode ser visto abaixo, passando como parâmetro a cor do fundo da imagem, que nesse caso é preto (0).

```python
rows, columns = img.shape

for i in range(columns):
    cv2.floodFill(img,None,(i,rows-1),0)
    cv2.floodFill(img,None,(i,0),0)

for j in range(rows):
    cv2.floodFill(img,None,(columns-1,j),0)
    cv2.floodFill(img,None,(0,j),0)

```

<center>
<figure float="middle" class="image">
  <img src="./assets/Image - Border cleaning.png" alt="Border cleaning.png">
  <figcaption>Figura 6 - Imagem após o tratamento de bordas</figcaption> 
</figure>
</center>

Após o tratamento das bordas (Figura 7), a quantidade de objetos presentes na imagem foi contado utilizando-se do método de _labeling_ já mencionado anteriormente

<center>
<figure float="middle" class="image">
  <img src="./assets/Image - Labeling.png" alt="Labeling.png">
  <figcaption>Figura 7 - Imagem após Labeling</figcaption> 
</figure>
</center>

```python
noObjects = 0
for i in range(columns):
    for j in range(rows):
        if img[i,j] == 255:
            shade = 1 + (noObjects%254)
            cv2.floodFill(img,None,(j,i),shade)
            noObjects+=1

print(f'We found {noObjects} objects in the picture')

```

Em seguida, trocou-se a cor do plano de fundo para branco (255), deste modo, é possível identificar os buracos presentes na figura pela cor preta (Figura 8).

```python
cv2.floodFill(img,None,(0,0),255)
```

<center>
<figure float="middle" class="image">
  <img src="./assets/Image - Inverting.png" alt="Inverting colors.png">
  <figcaption>Figura 8 - Imagem após a troca de cor no plano de fundo</figcaption> 
</figure>
</center>

Por fim, para diferenciar as bolhas com e sem buracos, a imagem foi varrida, e com auxílio do método de preenchimento de regiões os buracos foram um a um sendo preenchidos, enquanto um contador contabilizava a quantidade de buracos encontrados checando se o buraco encontrado fazia parte de uma bolha contabilizada ou não. A forma de varredura mencionado pode ser conferida no trecho de código abaixo.

```python
noHollowObjecs = 0
for i in range(columns):
    for j in range(rows):
        if img[i,j] == 0:
            cv2.floodFill(img,None,(j,i),255)
            #tests to see if hole is in anew object that has not been flooded yet
            for difI in [-1,0,1]:
                for difJ in [-1,0,1]:
                    if img[i-difI,j-difJ] != 255:
                        cv2.floodFill(img,None,(j-difJ,i-difI),255)
                        noHollowObjecs+=1

print(f'There were {noHollowObjecs} objects with holes in the picture')
print(f'There were {noObjects - noHollowObjecs} objects with no holes in the picture')
```

Com isso as saídas do algoritmo foram o trecho abaixo exibidos no terminal e a Figura 9:

```
We found 21 objects in the picture
There were 7 objects with holes in the picture
There were 14 objects with no holes in the picture
```

<center>
<figure float="middle" class="image">
  <img src="./assets/Image - After.png" alt="after.png">
  <figcaption>Figura 9 - Imagem de entrada</figcaption> 
</figure>
</center>

## Equalização de Histograma
