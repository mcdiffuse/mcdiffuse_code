# Clarity or Confusion: The Double-Edged Sword of Diffusion-based Speech Enhancement
This repository contains the official codebase and example hosting for our paper "Clarity or Confusion: The Double-Edged Sword of Diffusion-based Speech Enhancement." Our work explores the impact of diffusion-based models on speech enhancement, comparing their performance in various scenarios.

![Model Comparison Diagram](images/mc_diffse_diagram.png)

## Organization
This section outlines the structure of the repository and the contents of each directory.
- `images/`: Contains images used in the README and other potentially interesting figures.
- `audio/`: Contains audio samples used in the README for demonstration.
- `code/`: Contains the code used for training and a simple Jupyter notebook for inference.

## SGMSE & TF-Gridnet
Documentation and code for these models are available in their GitHub or Papers.

[SGMSE GitHub](https://github.com/sp-uhh/sgmse) | [TF-Gridnet Paper](https://arxiv.org/pdf/2211.12433.pdf) 

## Speech Enhancement Examples
These examples showcase the performance of our models on speech enhancement tasks. Scroll horizontally to compare the mixed input with the output of each model.


| Mixed Audio  | MC-DiffSE |
|--------------|-----------|
|Easy Samples  |           |
[Mixture 1](audio/mixture_1764_e_1_mix.wav) | [Reconstruction 1](audio/mixture_1764_e_1_recon.wav)
[Mixture 2](audio/mixture_1501_e_2_mix.wav) | [Reconstruction 2](audio/mixture_1501_e_2_recon.wav)
[Mixture 3](audio/mixture_673_e_3_mix.wav) | [Reconstruction 3](audio/mixture_673_e_3_recon.wav)
|Difficult Samples |       |
[Mixture 1](audio/mixture_1669_d_1_mix.wav) | [Reconstruction 1](audio/mixture_1669_d_1_recon.wav)
[Mixture 2](audio/mixture_1319_d_2_mix.wav) | [Reconstruction 2](audio/mixture_1319_d_2_recon.wav)
[Mixture 3](audio/mixture_1005_d_3_mix.wav) | [Reconstruction 3](audio/mixture_1005_d_3_recon.wav)
|Hallucination Examples |       |
[Mixture 1](audio/mixture_499_h_1_mix.wav) | [Reconstruction 1](audio/mixture_499_h_1_recon.wav)
[Mixture 2](audio/mixture_1341_h_2_mix.wav) | [Reconstruction 2](audio/mixture_1341_h_2_recon.wav)
[Mixture 3](audio/mixture_499_h_3_mix.wav) | [Reconstruction 3](audio/mixture_499_h_3_recon.wav)

## Hallucination Examples

| Real Text  | Hallucination |
|--------------|-----------|
"who with his latin clergy was ignorant of the language the arts and the theology of the greeks" | "who with his latin clergy was ignorant of the language the arts and the theology of **greece**"  
||"who with his latin clergy **is** ignorant of the language the arts and the theology of **a priest**" |
"i even bought something from edge i mean missus wilson" | "i even bought something from edge i **i am** missus wilson"
||"i even bought something from edge i **i** mean missus wilson"|
