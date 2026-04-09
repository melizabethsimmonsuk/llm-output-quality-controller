# AI Output Quality Control

A structured evaluation framework for assessing AI-generated responses across key dimensions:

- Accuracy  
- Relevance  
- Clarity  
- Completeness  
- Instruction Adherence  
- Safety  

## Overview

This project implements a simple scoring system for comparing multiple AI outputs against a prompt.

It produces a structured Markdown report summarizing:

- Per-dimension scores  
- Total scores  
- Preferred output selection  

## Usage

```bash
python3 compare_outputs.py --input sample_pairs.json --output generated_report.md
