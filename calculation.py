# from decimal import InvalidOperation
# import pandas as pd
# from utils.dictionary_manager import DictionaryManager5Lang

# EQUIPMENT_SETTINGS = {
#     "Standard": {
#         "damping_factor": 0.5,  # Erhöht von 0.2 auf 0.5 für stärkere Anpassungen
#         "max_increase": 0.8,    # Erhöht von 0.5 auf 0.8 um größere Steigerungen zu erlauben
#         "max_decrease": 0.5,
#         "impression_threshold": 100,
#         "impression_boost": 1.5,
#         "conversion_rate_impact": 0.1
#     },
#     "Leicht": {
#         "damping_factor": 0.3,  # Leicht erhöht von 0.2
#         "max_increase": 0.3,    # Leicht erhöht von 0.2
#         "max_decrease": 0.1,
#         "impression_threshold": 500,
#         "impression_boost": 1.2,
#         "conversion_rate_impact": 0.2
#     },
#     "Schwer": {
#         "damping_factor": 0.8,  # Erhöht von 0.1 auf 0.8 für aggressive Anpassungen
#         "max_increase": 1.5,    # Erhöht von 1.0 auf 1.5
#         "max_decrease": 0.3,
#         "impression_threshold": 50,
#         "impression_boost": 2.0,
#         "conversion_rate_impact": 0.1
#     }
# }

# def validate_positive(value: float) -> bool:
#     return isinstance(value, (int, float)) and value >= 0

# def calculate_standard_bid(
#     current_bid: float,
#     target_roas: float,
#     current_roas: float,
#     strategy: str,
#     row_data: dict,
#     equipment: dict,
#     df: pd.DataFrame = None,
#     current_index: int = None
# ) -> float:
#     """Standardberechnung für ein neues Gebot"""
#     if row_data is None:
#         row_data = {}
#     if equipment is None:
#         equipment = {}

#     dict_manager = DictionaryManager5Lang()
#     try:
#         # Versuche Werte mit verschiedenen möglichen Spaltennamen zu finden
#         spend_column = next((col for col in ["Ausgaben", "Spend", dict_manager.get_translation("Ausgaben", "en")] 
#                            if col in row_data), "Ausgaben")
#         spend = float(row_data.get(spend_column, 0))

#         # Wenn aktuelle Zeile keine Daten hat und DataFrame + Index verfügbar sind
#         if spend == 0 and df is not None and current_index is not None and current_index + 1 < len(df):
#             next_row = df.iloc[current_index + 1]
#             next_spend = float(next_row.get(spend_column, 0))
#             next_roas = float(next_row.get("ROAS", 0))

#             # Wenn nächste Zeile vollständige Daten hat und ROAS nicht 0 ist
#             if next_spend > 0 and next_roas > 0:
#                 return calculate_standard_bid(
#                     current_bid=current_bid,
#                     target_roas=target_roas,
#                     current_roas=next_roas,
#                     strategy=strategy,
#                     row_data=next_row.to_dict(),
#                     equipment=equipment,
#                     df=df,
#                     current_index=current_index + 1
#                 )

#         if spend == 0:
#             return round(current_bid, 2)

#         if current_roas is None:
#             current_roas = target_roas

#         if strategy == "Individuell":
#             if not isinstance(equipment, dict):
#                 return round(current_bid, 2)
#             try:
#                 damping_factor = float(equipment.get("damping_factor", 0.2))
#                 max_increase = float(equipment.get("max_increase", 0.5))
#                 max_decrease = float(equipment.get("max_decrease", 0.5))
#                 impression_threshold = float(equipment.get("impression_threshold", 100))
#                 impression_boost = float(equipment.get("impression_boost", 1.5))
#                 conversion_rate_impact = float(equipment.get("conversion_rate_impact", 0.1))
#             except (ValueError, TypeError):
#                 return round(current_bid, 2)
#         else:
#             s = EQUIPMENT_SETTINGS.get(strategy, EQUIPMENT_SETTINGS["Standard"])
#             damping_factor = s["damping_factor"]
#             max_increase = s["max_increase"]
#             max_decrease = s["max_decrease"]
#             impression_threshold = s["impression_threshold"]
#             impression_boost = s["impression_boost"]
#             conversion_rate_impact = s["conversion_rate_impact"]

#         # conversion_rate_impact => nur wenn current_roas < target_roas
#         cr_factor = 0.0
#         if current_roas < target_roas:
#             cr_factor = conversion_rate_impact

#         effective_damp = damping_factor + cr_factor
#         roas_ratio = (current_roas/target_roas) if target_roas > 0 else 1.0
#         new_bid = current_bid * (1 + effective_damp * (roas_ratio - 1))

#         # clamp
#         new_bid = min(new_bid, current_bid * (1 + max_increase))
#         new_bid = max(new_bid, current_bid * (1 - max_decrease))

#         # Impression-Boost mit Dictionary-Lookup
#         impression_column = next((col for col in ["Impressionen", "Impressions", dict_manager.get_translation("Impressionen", "en")] 
#                                if col in row_data), "Impressionen")
#         impr = row_data.get(impression_column, 999999)
#         if impr < impression_threshold:
#             new_bid = new_bid * impression_boost

#         return round(new_bid, 2)

#     except (ValueError, InvalidOperation, ZeroDivisionError):
#         return round(current_bid, 2)

# def calculate_new_bid(
#     current_bid: float,
#     target_roas: float = 2.0,
#     current_roas: float = None,
#     strategy: str = "Standard",
#     row_data: dict = None,
#     equipment: dict = None,
#     sku_rules: list = None,
#     sku_matcher = None
# ) -> float:
#     """Berechnet ein neues Gebot basierend auf verschiedenen Parametern."""
#     try:
#         if not isinstance(current_bid, (int, float)) or current_bid < 0:
#             raise ValueError("Ungültiges Gebot")
#         if not isinstance(target_roas, (int, float)) or target_roas <= 0:
#             raise ValueError("Ungültiger ROAS")

#         # Phase 1: Standardberechnung mit globalen Einstellungen
#         standard_bid = calculate_standard_bid(
#             current_bid=current_bid,
#             target_roas=target_roas,
#             current_roas=current_roas,
#             strategy=strategy,
#             row_data=row_data,
#             equipment=equipment if strategy == "Individuell" else None
#         )

#         # Phase 2: SKU-spezifische Regeln temporär deaktiviert
#         # TODO: SKU-spezifische Logik wurde temporär entfernt
#         # Implementiere später eine stabilere Version der SKU-Regel-Anwendung

#         return standard_bid

#     except Exception as e:
#         print(f"Error in calculate_new_bid: {str(e)}")
#         return round(current_bid, 2)


from decimal import InvalidOperation
import pandas as pd
from utils.dictionary_manager import DictionaryManager5Lang

EQUIPMENT_SETTINGS = {
    "Standard": {
        "damping_factor": 0.5,
        "max_increase": 0.8,
        "max_decrease": 0.5,
        "impression_threshold": 100,
        "impression_boost": 1.5,
        "conversion_rate_impact": 0.1
    },
    "Leicht": {
        "damping_factor": 0.3,
        "max_increase": 0.3,
        "max_decrease": 0.1,
        "impression_threshold": 500,
        "impression_boost": 1.2,
        "conversion_rate_impact": 0.2
    },
    "Schwer": {
        "damping_factor": 0.8,
        "max_increase": 1.5,
        "max_decrease": 0.3,
        "impression_threshold": 50,
        "impression_boost": 2.0,
        "conversion_rate_impact": 0.1
    }
}

def validate_positive(value: float) -> bool:
    return isinstance(value, (int, float)) and value >= 0

def calculate_standard_bid(
    current_bid: float,
    target_roas: float,
    current_roas: float,
    strategy: str,
    row_data: dict,
    equipment: dict,
    df: pd.DataFrame = None,
    current_index: int = None
) -> float:
    if row_data is None:
        row_data = {}
    if equipment is None:
        equipment = {}

    dict_manager = DictionaryManager5Lang()
    try:
        spend_column = next((col for col in ["Ausgaben", "Spend", dict_manager.get_translation("Ausgaben", "en")] 
                           if col in row_data), "Ausgaben")
        spend = float(row_data.get(spend_column, 0))

        if spend == 0 and df is not None and current_index is not None and current_index + 1 < len(df):
            next_row = df.iloc[current_index + 1]
            next_spend = float(next_row.get(spend_column, 0))
            next_roas = float(next_row.get("ROAS", 0))

            if next_spend > 0 and next_roas > 0:
                return calculate_standard_bid(
                    current_bid=current_bid,
                    target_roas=target_roas,
                    current_roas=next_roas,
                    strategy=strategy,
                    row_data=next_row.to_dict(),
                    equipment=equipment,
                    df=df,
                    current_index=current_index + 1
                )

        if spend == 0:
            return round(current_bid, 2)

        if current_roas is None:
            current_roas = target_roas

        if strategy == "Individuell":
            if not isinstance(equipment, dict):
                return round(current_bid, 2)
            try:
                damping_factor = float(equipment.get("damping_factor", 0.2))
                max_increase = float(equipment.get("max_increase", 0.5))
                max_decrease = float(equipment.get("max_decrease", 0.5))
                impression_threshold = float(equipment.get("impression_threshold", 100))
                impression_boost = float(equipment.get("impression_boost", 1.5))
                conversion_rate_impact = float(equipment.get("conversion_rate_impact", 0.1))
            except (ValueError, TypeError):
                return round(current_bid, 2)
        else:
            s = EQUIPMENT_SETTINGS.get(strategy, EQUIPMENT_SETTINGS["Standard"])
            damping_factor = s["damping_factor"]
            max_increase = s["max_increase"]
            max_decrease = s["max_decrease"]
            impression_threshold = s["impression_threshold"]
            impression_boost = s["impression_boost"]
            conversion_rate_impact = s["conversion_rate_impact"]

        cr_factor = 0.0
        if current_roas < target_roas:
            cr_factor = conversion_rate_impact

        effective_damp = damping_factor + cr_factor
        roas_ratio = (current_roas / target_roas) if target_roas > 0 else 1.0
        new_bid = current_bid * (1 + effective_damp * (roas_ratio - 1))

        new_bid = min(new_bid, current_bid * (1 + max_increase))
        new_bid = max(new_bid, current_bid * (1 - max_decrease))

        impression_column = next((col for col in ["Impressionen", "Impressions", dict_manager.get_translation("Impressionen", "en")] 
                               if col in row_data), "Impressionen")
        impr = row_data.get(impression_column, 999999)
        if impr < impression_threshold:
            new_bid = new_bid * impression_boost

        return round(new_bid, 2)

    except (ValueError, InvalidOperation, ZeroDivisionError):
        return round(current_bid, 2)

def calculate_new_bid(
    current_bid: float,
    target_roas: float = 2.0,
    current_roas: float = None,
    strategy: str = "Standard",
    row_data: dict = None,
    equipment: dict = None,
    sku_rules: list = None,
    sku_matcher = None
) -> float:
    try:
        if not isinstance(current_bid, (int, float)) or current_bid < 0:
            raise ValueError("Invalid bid")
        if not isinstance(target_roas, (int, float)) or target_roas <= 0:
            raise ValueError("Invalid ROAS")

        # Phase 1: Standard calculation with equipment or strategy settings
        standard_bid = calculate_standard_bid(
            current_bid=current_bid,
            target_roas=target_roas,
            current_roas=current_roas,
            strategy=strategy,
            row_data=row_data,
            equipment=equipment if strategy == "Individuell" else None
        )

        # Phase 2: Apply SKU-specific rules if provided
        if sku_rules and sku_matcher:
            sku = row_data.get("SKU", None) if row_data else None
            if sku:
                for rule in sku_rules:
                    if sku_matcher.find_exact_match(sku) == rule["sku"]:
                        return calculate_standard_bid(
                            current_bid=current_bid,
                            target_roas=rule["target_roas"],
                            current_roas=current_roas,
                            strategy=rule["strategy"],
                            row_data=row_data,
                            equipment=equipment if rule["strategy"] == "Individuell" else None
                        )

        return standard_bid

    except Exception as e:
        print(f"Error in calculate_new_bid: {str(e)}")
        return round(current_bid, 2)