# Detección de Malaria mediante Inteligencia Artificial

¿Te has preguntado alguna vez cuál es el animal más mortífero de la historia? ¿El causante de millones de muertes al año? Este proyecto aborda la detección de malaria, una enfermedad potencialmente mortal, utilizando técnicas avanzadas de inteligencia artificial.

## Introducción

La malaria, transmitida por el mosquito Anofeles infectado con el parásito Plasmodium falciparum, sigue siendo uno de los mayores desafíos de salud pública a nivel mundial. En 2020, se reportaron aproximadamente 241 millones de casos de malaria en todo el mundo, resultando en 627,000 muertes.

Este proyecto utiliza técnicas de aprendizaje profundo para analizar automáticamente imágenes de células sanguíneas, clasificando a los pacientes como sanos o infectados con un alto grado de precisión.

## Datos Utilizados

- Dataset: [Detección de Malaria de Kaggle](https://www.kaggle.com/datasets/sayeemmohammed/malaria-detection)
- 15,031 imágenes de alta resolución (224x224 píxeles) en formato JPG
- Distribución:
  - Entrenamiento: 13,152 imágenes
  - Prueba: 1,253 imágenes
  - Validación: 626 imágenes

![Células infectadas](ruta/a/10_primeras_imagenes_infectadas_train.jpg)
![Células no infectadas](ruta/a/10_primeras_imagenes_uninfected.jpg)

## Modelo de Detección

- Arquitectura base: MobileNetV2
- Modificaciones:
  - Capa de Global Average Pooling
  - Dos capas densas con 100 unidades y activación ReLU
  - Capa de salida con 2 unidades y activación softmax

## Resultados

- Precisión en datos de entrenamiento: 88.72%
- Precisión en datos de prueba: 89.46%
- Pérdida en datos de entrenamiento: 0.2781
- Pérdida en datos de prueba: 0.2647

## Implementación

El modelo ha sido implementado como una aplicación web utilizando Django, permitiendo a los usuarios cargar imágenes para su análisis en tiempo real.

## Instalación y Uso

1. Clone este repositorio
2. Instale las dependencias: pip install -r requirements.txt
3. Ejecute la aplicación Streamlit: streamlit run app.py
4 .La aplicación se abrirá automáticamente en su navegador predeterminado

Despliegue
La aplicación está desplegada y disponible para su uso en:
https://malaria-detector-siskzoaxsmm7ucgetk9eae.streamlit.app/

## Trabajo Futuro

- Explorar arquitecturas de modelos alternativas
- Ampliar el conjunto de datos
- Mejorar la interpretabilidad del modelo

## Documentación Detallada

Para una explicación más profunda del proyecto, metodología y resultados, consulte:
- https://tiny-citrine-a6e.notion.site/Detecci-n-de-Malaria-mediante-Inteligencia-Artificial-725da3ccc5c84b99bb67dbdc15ec95da

## Despliege del modelo APP
- https://malaria-detector-siskzoaxsmm7ucgetk9eae.streamlit.app/

## Contacto

Pablo de Haro Pishoudt
- [GitHub](https://github.com/Pablodeharo)
- [LinkedIn](https://www.linkedin.com/in/pablo-de-haro-pishoudt-0871972b6/)

Estoy abierto a colaboraciones y siempre interesado en discutir nuevas ideas en el campo de la inteligencia artificial y el aprendizaje automático aplicado a la salud.
