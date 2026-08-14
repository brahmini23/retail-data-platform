from pathlib import Path

def save_csv(df, filename):
    #output from generated records
    output_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / filename
    df.to_csv(output_file, index=False)

    print(f"Generated {len(df)} records in " + filename)
    print(f"Saved to {output_file}")
