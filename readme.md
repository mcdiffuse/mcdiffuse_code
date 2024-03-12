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
| <audio class="audio-player" src="audio/e_1_mix.wav" controls preload></audio> | <audio class="audio-player" src="audio/e_1_recon.wav" controls preload></audio> |
| <audio class="audio-player" src="audio/e_2_mix.wav" controls preload></audio> | <audio class="audio-player" src="audio/e_2_recon.wav" controls preload></audio> |
|Difficult Samples |       |
| <audio class="audio-player" src="audio/d_1_mix.wav" controls preload></audio> | <audio class="audio-player" src="audio/d_1_recon.wav" controls preload></audio> |
|Hallucination Examples |   |
| <audio class="audio-player" src="audio/h_1_mix.wav" controls preload></audio> | <audio class="audio-player" src="audio/h_1_recon.wav" controls preload></audio> |
