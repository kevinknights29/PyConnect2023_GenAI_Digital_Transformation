# PyConnect2023_GenAI_Digital_Transformation

This repo contains the content related to the talk:

`Construyendo soluciones con Generative AI para la transformación digital`

**Content**

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Contributing](#contributing)

---

![image](https://github.com/kevinknights29/PyConnect2023_GenAI_Digital_Transformation/assets/74464814/505dbbbb-fda8-4e52-a1a2-ac9b724cd72f)

**New Features**

- Added model arguments control

![image](https://github.com/kevinknights29/PyConnect2023_GenAI_Digital_Transformation/assets/74464814/20518152-0b78-4b46-8c82-778da2cbcee7)

![image](https://github.com/kevinknights29/PyConnect2023_GenAI_Digital_Transformation/assets/74464814/1b2c7d59-3cee-4be4-9880-acbf71ff7bab)

## Overview

I wanted to showcase the true value of GenAI applications,
and the best way was to create a chatbot application for the entire conference.

### Idea

Build an application to support event's participants/attendees.

### Business Objective

Increase participants/attendees satisfaction (CSAT = customer satisfaction).

### Requirements

- GUI (graphical interface).
- Conference Knowledge Base.
- Personalization (unique experience for each user).

### GenAI (ML) Objective

Maximize participants/attendees experience.

### Technologies

- Langchain
- Streamlit
- Weaviate
- OpenAI

![image](https://github.com/kevinknights29/PyConnect2023_GenAI_Digital_Transformation/assets/74464814/9eb34254-1686-4925-89e8-083376807e6c)

### Data gathering

Collected all text information for each session in the calendar.

#### Schedule Content

![image](https://github.com/kevinknights29/PyConnect2023_GenAI_Digital_Transformation/assets/74464814/6bd6dc82-3498-496e-9967-20b133a8a3d7)

#### Session Content Example

![image](https://github.com/kevinknights29/PyConnect2023_GenAI_Digital_Transformation/assets/74464814/d51c8777-155d-4049-baae-26e3179ca84e)

#### Data Storage

In regard to vector stores, I selected weaviate since they are open source and provide a great free tier.

To create an account visit: [Weaviate - Homepage](https://weaviate.io/)

![image](https://github.com/kevinknights29/PyConnect2023_GenAI_Digital_Transformation/assets/74464814/95412eb5-f4f3-4c0b-a94f-46f7a82701d8)

### Model Selection

I selected OpenAI as the LLM service provider, since they offer a very good price/quality ratio.

- gpt-3.5-turbo
- text-embedding-ada-002

For reference, around 750 words predicted by `gpt-3.5-turbo` costs 0.002 USD.

## Getting Started

### Setup

Create the virtual environment with:

```bash
python -m venv .venv
```

Then, activate it with:

```bash
source .venv/bin/activate
```

Finally, install dependencies with:

```bash
pip install -r requirements.txt
```

### Local Usage

To run the streamlit application locally, use:

```bash
streamlit run app.py
```

This will automatically open a window in your default web browser.

#### Have fun!

![image](https://github.com/kevinknights29/PyConnect2023_GenAI_Digital_Transformation/assets/74464814/04385ebb-2d07-4a41-8823-2c156dfa1a15)

## Contributing

### Installing pre-commit

Pre-commit is already part of this project dependencies.
If you would like to installed it as standalone run:

```bash
pip install pre-commit
```

To activate pre-commit run the following commands:

- Install Git hooks:

```bash
pre-commit install
```

- Update current hooks:

```bash
pre-commit autoupdate
```

To test your installation of pre-commit run:

```bash
pre-commit run --all-files
```
