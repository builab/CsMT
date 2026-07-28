#!/usr/bin/env python3
import argparse
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(
        description="Plot stacked histogram of resolution grouped by decoration status."
    )
    parser.add_argument(
        "--input", "-i",
        default="MT.csv",
        help="Path to the input CSV file (default: MT.csv)."
    )
    parser.add_argument(
        "--output", "-o",
        default="MT_res_hist.pdf",
        help="Path to the output file (default: MT_res_hist.pdf)."
    )
    parser.add_argument(
        "--bin", "-b",
        type=float,
        default=0.5,
        help="Bin width for the histogram (default: 0.5)."
    )
    parser.add_argument(
        "--res_cutoff", "-c",
        type=float,
        default=8.0,
        help="Maximum resolution cutoff value (default: 8.0)."
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # 1. Load dataset
    try:
        df = pd.read_csv(args.input)
    except Exception as e:
        print(f"Error reading file '{args.input}': {e}")
        sys.exit(1)

    # 2. Locate the 'Decorated' / 'Decoration' column
    dec_col = None
    for col in df.columns:
        if col.strip().lower() in ['decorated', 'decoration']:
            dec_col = col
            break

    if dec_col is None:
        print("Error: Could not find 'Decorated' or 'Decoration' column.")
        sys.exit(1)

    if 'Resolution' not in df.columns:
        print("Error: Could not find 'Resolution' column.")
        sys.exit(1)

    # 3. Handle exported merged cells by forward-filling blank entries
    df[dec_col] = df[dec_col].ffill()

    # 4. Clean resolution values and filter by cutoff
    df['Resolution'] = pd.to_numeric(df['Resolution'], errors='coerce')
    df_filtered = df[df['Resolution'] <= args.res_cutoff].copy()

    if df_filtered.empty:
        print(f"Warning: No data available with Resolution <= {args.res_cutoff}.")
        sys.exit(0)

    # 5. Standardize text entries
    df_filtered['Decoration_Clean'] = (
        df_filtered[dec_col].astype(str).str.strip().str.title()
    )
    df_filtered['Decoration_Clean'] = df_filtered['Decoration_Clean'].replace(
        {'Undecoreated': 'Undecorated'}
    )

    # 6. Split resolution dataset by category
    decorated_res = df_filtered[
        df_filtered['Decoration_Clean'] == 'Decorated'
    ]['Resolution'].dropna()

    undecorated_res = df_filtered[
        df_filtered['Decoration_Clean'] == 'Undecorated'
    ]['Resolution'].dropna()

    # 7. Define histogram bins based on command-line flags
    min_val = np.floor(df_filtered['Resolution'].min())
    bins = np.arange(min_val, args.res_cutoff + args.bin, args.bin)

    # 8. Generate stacked histogram
    plt.figure(figsize=(10, 6))
    plt.hist(
        [decorated_res, undecorated_res],
        bins=bins,
        stacked=True,
        label=['Decorated', 'Undecorated'],
        color=['#3B76D8', '#E3A03B'],
        edgecolor='black',
        alpha=0.85,
    )

    # Formatting
    plt.xlabel('Resolution')
    plt.ylabel('Count')
    plt.title('Histogram of MT Resolution (Decorated & Undecorated)')
    plt.legend(title='Category')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()

    # 9. Save figure to output file
    plt.savefig(args.output, dpi=300)
    print(f"Successfully created plot: {args.output}")

if __name__ == '__main__':
    main()