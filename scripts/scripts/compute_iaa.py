#!/usr/bin/env python3
"""IAA Computation Script - Project 1B"""

import json
import numpy as np
from sklearn.metrics import cohen_kappa_score
import krippendorff

def compute_iaa(data_file='gold_standard/gold_50.json'):
    """Compute IAA metrics."""
    
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {data_file}")
        return None
    
    print("=" * 60)
    print("INTER-ANNOTATOR AGREEMENT REPORT")
    print("=" * 60)
    
    annotators = ['expert', 'A1', 'A2', 'A3', 'A4', 'A5']
    dimensions = ['satisfaction', 'urgency', 'frustration', 'confusion']
    
    results = {}
    
    for dim in dimensions:
        matrix = []
        for item in data:
            row = []
            for ann in annotators:
                val = item.get('annotator_scores', {}).get(ann, {}).get(dim)
                if val is not None:
                    row.append(val)
            if len(row) >= 2:
                matrix.append(row)
        
        if matrix:
            matrix = np.array(matrix)
            alpha = krippendorff.alpha(matrix, level_of_measurement='ordinal')
            
            kappas = []
            for i in range(len(annotators)):
                for j in range(i+1, len(annotators)):
                    scores_i, scores_j = [], []
                    for item in data:
                        si = item.get('annotator_scores', {}).get(annotators[i], {}).get(dim)
                        sj = item.get('annotator_scores', {}).get(annotators[j], {}).get(dim)
                        if si is not None and sj is not None:
                            scores_i.append(si)
                            scores_j.append(sj)
                    if len(scores_i) >= 2:
                        kappa = cohen_kappa_score(scores_i, scores_j, weights='quadratic')
                        kappas.append(kappa)
            
            avg_kappa = np.mean(kappas) if kappas else 0
            results[dim] = {'alpha': alpha, 'avg_kappa': avg_kappa}
            
            print(f"\n{dim.capitalize()}:")
            print(f"  Krippendorff's α: {alpha:.3f}")
            print(f"  Avg Cohen's κ: {avg_kappa:.3f}")
            
            if alpha >= 0.70:
                print(f"  Status: ✅ PASS (≥ 0.70)")
            else:
                print(f"  Status: ❌ FAIL (< 0.70)")
    
    print("\n" + "=" * 60)
    print("IAA COMPUTATION COMPLETE")
    print("=" * 60)
    
    return results

if __name__ == "__main__":
    compute_iaa()
