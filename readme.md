# Clarity or Confusion: The Double-Edged Sword of Diffusion-based Speech Enhancement
This repository contains the official codebase and example hosting for our paper "Clarity or Confusion: The Double-Edged Sword of Diffusion-based Speech Enhancement." Our work explores the impact of diffusion-based models on speech enhancement, comparing their performance in various scenarios.

![Model Comparison Diagram](images/mc_diffse_diagram.png)

## Organization
This section outlines the structure of the repository and the contents of each directory.
- `images/`: Contains images used in the README and other potentially interesting figures.
- `audio/`: Contains audio samples used in the README for demonstration.
- `code/`: Contains the code used for training and a simple Jupyter notebook for inference.

## Installation
Instructions on how to set up the environment and install necessary dependencies.

## Usage
Detailed instructions on how to use the code for training and inference.

## Speech Enhancement Examples
These examples showcase the performance of our models on speech enhancement tasks. Scroll horizontally to compare the mixed input with the output of each model.


| Mixed Audio  | MC-DiffSE |
|--------------|-----------|
|Easy Samples  |           |
[Mixture 1](audio/e_1_mix.wav) | [Reconstruction 1](audio/e_1_recon.wav)
[Mixture 2](audio/e_2_mix.wav) | [Reconstruction 2](audio/e_2_recon.wav)
|Difficult Samples |       |
[Mixture 1](audio/d_1_mix.wav) | [Reconstruction 1](audio/d_1_recon.wav)
|Hallucination Examples |       |
[Mixture 1](audio/h_1_mix.wav) | [Reconstruction 1](audio/h_1_recon.wav)

## Hallucination Examples

| Real Text  | Hallucination |
|--------------|-----------|
"who with his latin clergy was ignorant of the language the arts and the theology of the greeks" | "who with his latin clergy was ignorant of the language the arts and the theology of **greece**"  
||"who with his latin clergy **is** ignorant of the language the arts and the theology of **a priest**" |
"i even bought something from edge i mean missus wilson" | "i even bought something from edge i **i am** missus wilson"
||"i even bought something from edge i **i** mean missus wilson"|


<!-- 
### Real Text: 
"who with his latin clergy was ignorant of the language the arts and the theology of the greeks"

## Hallucinations:
"who with his latin clergy was ignorant of the language the arts and the theology of **greece**"

"who with his latin clergy **is** ignorant of the language the arts and the theology of **a priest**" -->
