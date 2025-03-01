
import pandas as pd
from pathlib import Path

def load_format_template():
    """Lädt das Formatierungstemplate aus der Beispieldatei"""
    template_path = Path("attached_assets/beispielformat.xlsx")
    if template_path.exists():
        return pd.read_excel(template_path)
    return None

def apply_template_format(df):
    """Wendet das Format aus der Vorlage auf das DataFrame an"""
    template_df = load_format_template()
    if template_df is None:
        return df
    
    formatted_df = df.copy()
    for col in formatted_df.columns:
        if col in template_df.columns:
            # Formatierung aus Template übernehmen
            formatted_df[col] = formatted_df[col].astype(template_df[col].dtype)
            
    return formatted_df
