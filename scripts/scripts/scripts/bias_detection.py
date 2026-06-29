#!/usr/bin/env python3
"""Bias Detection Script - Project 1B"""

import json
import numpy as np
from collections import Counter

def detect_bias(data_file='gold_standard/gold_50.json'):
    """Detect annotator biases."""
    
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {data_file}")
        return None
    
    print("=" * 60)
    print("ANNOTATOR BIAS AUDIT REPORT")
    print("=" * 60)
    
    annotators = ['A1', 'A2', 'A3', 'A4', 'A5']
    dimensions = ['satisfaction', 'urgency', 'frustration', 'confusion']
    
    bias_report = {}
    
    for ann in annotators:
        print(f"\n{'='*40}")
        print(f"ANNOTATOR: {ann}")
        print(f"{'='*40}")
        
        all_scores = []
        
        for dim in dimensions:
            scores = []
            for item in data:
                score = item.get('annotator_scores', {}).get(ann, {}).get(dim)
                if score is not None:
                    scores.append(score)
                    all_scores.append(score)
            
            if scores:
                hist = Counter(scores)
                mean = np.mean(scores)
                std = np.std(scores)
                mid_pct = hist.get(3, 0) / len(scores) * 100
                extreme_pct = (hist.get(1, 0) + hist.get(5, 0)) / len(scores) * 100
                
                print(f"\n{dim.capitalize()}:")
                print(f"  Mean: {mean:.2f}, Std: {std:.2f}")
                print(f"  Score distribution: {dict(sorted(hist.items()))}")
                print(f"  % at score 3 (mid): {mid_pct:.1f}%")
                print(f"  % at extremes (1/5): {extreme_pct:.1f}%")
                
                if mid_pct > 40:
                    print(f"  ⚠️ CENTRAL TENDENCY BIAS: >40% at score 3")
                    bias_report[ann] = bias_report.get(ann, []) + ['central_tendency']
                
                if extreme_pct < 10:
                    print(f"  ⚠️ AVOIDS EXTREMES: <10% at scores 1 or 5")
                    bias_report[ann] = bias_report.get(ann, []) + ['avoids_extremes']
        
        if all_scores:
            first_half = all_scores[:len(all_scores)//2]
            second_half = all_scores[len(all_scores)//2:]
            if first_half and second_half:
                std_first = np.std(first_half)
                std_second = np.std(second_half)
                if std_second > std_first * 1.3:
                    print(f"\n⚠️ FATIGUE BIAS: Higher variance in second half")
                    bias_report[ann] = bias_report.get(ann, []) + ['fatigue']
    
    print("\n" + "=" * 60)
    print("BIAS DETECTION SUMMARY")
    print("=" * 60)
    
    for ann, biases in bias_report.items():
        print(f"\n{ann}:")
        for bias in set(biases):
            print(f"  - {bias.replace('_', ' ').title()}")
    
    return bias_report

if __name__ == "__main__":
    detect_bias()
