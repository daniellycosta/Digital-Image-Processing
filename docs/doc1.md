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

```
Mauris vestibulum ullamcorper nibh, ut semper purus pulvinar ut. Donec volutpat orci sit amet mauris malesuada, non pulvinar augue aliquam. Vestibulum ultricies at urna ut suscipit. Morbi iaculis, erat at imperdiet semper, ipsum nulla sodales erat, eget tincidunt justo dui quis justo. Pellentesque dictum bibendum diam at aliquet. Sed pulvinar, dolor quis finibus ornare, eros odio facilisis erat, eu rhoncus nunc dui sed ex. Nunc gravida dui massa, sed ornare arcu tincidunt sit amet. Maecenas efficitur sapien neque, a laoreet libero feugiat ut.
```
