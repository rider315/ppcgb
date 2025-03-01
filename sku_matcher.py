
# import pandas as pd
# from thefuzz import fuzz
# from thefuzz import process
# import re
# from typing import Optional, List, Tuple, Dict, Set
# from pathlib import Path
# from utils.dictionary_manager import DictionaryManager5Lang

# class SKUMatcher:
#     def __init__(self, known_skus: List[str]):
#         self.known_skus = known_skus
#         self.cleaned_known_skus = [self.preprocess_sku(sku) for sku in known_skus]
#         self.dict_manager = DictionaryManager5Lang()
#         self.keyword_sku_map: Dict[str, Set[str]] = {}
#         self.sku_keyword_map: Dict[str, Set[str]] = {}
#         self.load_mappings()
        
#     def load_mappings(self):
#         """Load keyword-SKU mappings from file"""
#         file_path = Path("attached_assets/keyword_sku_mappings.xlsx")
#         if file_path.exists():
#             df = pd.read_excel(file_path)
#             if not df.empty:
#                 self.keyword_sku_map = df.set_index('keyword')['skus'].apply(eval).to_dict()
#                 self.sku_keyword_map = df.set_index('sku')['keywords'].apply(eval).to_dict()
    
#     def save_mappings(self):
#         """Save current mappings to file"""
#         keyword_data = [{"keyword": k, "skus": list(v)} for k, v in self.keyword_sku_map.items()]
#         sku_data = [{"sku": k, "keywords": list(v)} for k, v in self.sku_keyword_map.items()]
        
#         df_keyword = pd.DataFrame(keyword_data)
#         df_sku = pd.DataFrame(sku_data)
        
#         with pd.ExcelWriter(Path("attached_assets/keyword_sku_mappings.xlsx")) as writer:
#             df_keyword.to_excel(writer, sheet_name='keyword_to_sku', index=False)
#             df_sku.to_excel(writer, sheet_name='sku_to_keyword', index=False)

#     def update_mappings_from_bulk(self, bulk_file: str):
#         """Update mappings from bulk file"""
#         df = pd.read_excel(bulk_file)
        
#         # Try different possible column names for keyword
#         keyword_columns = ['Keyword-Text', 'Keyword', 'keyword']
#         keyword_col = None
#         for col in keyword_columns:
#             alt_name = self.dict_manager.get_value(col)
#             if col in df.columns:
#                 keyword_col = col
#                 break
#             elif alt_name and alt_name in df.columns:
#                 keyword_col = alt_name
#                 break
                
#         if not keyword_col:
#             return False
            
#         # Group by ad group ID and create mappings
#         for ad_group_id in df['Anzeigengruppen-ID'].unique():
#             group_df = df[df['Anzeigengruppen-ID'] == ad_group_id]
            
#             keywords = set(group_df[keyword_col].dropna())
#             skus = set(group_df['SKU'].dropna())
            
#             # Update both mappings
#             for keyword in keywords:
#                 if keyword not in self.keyword_sku_map:
#                     self.keyword_sku_map[keyword] = set()
#                 self.keyword_sku_map[keyword].update(skus)
                
#             for sku in skus:
#                 if sku not in self.sku_keyword_map:
#                     self.sku_keyword_map[sku] = set()
#                 self.sku_keyword_map[sku].update(keywords)
        
#         self.save_mappings()
#         return True

#     def get_skus_for_keyword(self, keyword: str) -> Set[str]:
#         """Get all SKUs associated with a keyword"""
#         return self.keyword_sku_map.get(keyword, set())

#     def get_keywords_for_sku(self, sku: str) -> Set[str]:
#         """Get all keywords associated with a SKU"""
#         return self.sku_keyword_map.get(sku, set())
        
#     @staticmethod
#     def preprocess_sku(sku: str) -> str:
#         if not isinstance(sku, str):
#             sku = str(sku)
#         cleaned = sku.strip().upper()
#         prefixes = ["ARTIKEL NR.", "ARTIKEL-NR.", "SKU-", "SKU:", "ART."]
#         for prefix in prefixes:
#             if cleaned.startswith(prefix):
#                 cleaned = cleaned[len(prefix):].strip()
#         cleaned = re.sub(r'[^\w\-]', '', cleaned)
#         return cleaned
    
#     def find_exact_match(self, input_sku: str) -> Optional[str]:
#         cleaned_input = self.preprocess_sku(input_sku)
#         try:
#             idx = self.cleaned_known_skus.index(cleaned_input)
#             return self.known_skus[idx]
#         except ValueError:
#             return None
    
#     def find_fuzzy_match(self, input_sku: str, threshold: int = 80) -> Tuple[Optional[str], int]:
#         cleaned_input = self.preprocess_sku(input_sku)
#         best_match, score, idx = process.extractOne(
#             cleaned_input,
#             self.cleaned_known_skus,
#             scorer=fuzz.token_sort_ratio
#         )
#         if score >= threshold:
#             return self.known_skus[idx], score
#         return None, score
    
#     def find_best_match(self, input_sku: str, threshold: int = 80) -> Tuple[Optional[str], int, str]:
#         exact_match = self.find_exact_match(input_sku)
#         if exact_match:
#             return exact_match, 100, "exact"
#         fuzzy_match, score = self.find_fuzzy_match(input_sku, threshold)
#         if fuzzy_match:
#             return fuzzy_match, score, "fuzzy"
#         return None, score, "no_match"


import pandas as pd
from thefuzz import fuzz
from thefuzz import process
import re
from typing import Optional, List, Tuple, Dict, Set
from pathlib import Path
from utils.dictionary_manager import DictionaryManager5Lang

class SKUMatcher:
    def __init__(self, known_skus: List[str]):
        self.known_skus = known_skus
        self.cleaned_known_skus = [self.preprocess_sku(sku) for sku in known_skus]
        self.dict_manager = DictionaryManager5Lang()
        self.keyword_sku_map: Dict[str, Set[str]] = {}
        self.sku_keyword_map: Dict[str, Set[str]] = {}
        self.load_mappings()
        
    def load_mappings(self):
        file_path = Path("attached_assets/keyword_sku_mappings.xlsx")
        if file_path.exists():
            df = pd.read_excel(file_path)
            if not df.empty:
                self.keyword_sku_map = df.set_index('keyword')['skus'].apply(eval).to_dict()
                self.sku_keyword_map = df.set_index('sku')['keywords'].apply(eval).to_dict()
    
    def save_mappings(self):
        keyword_data = [{"keyword": k, "skus": list(v)} for k, v in self.keyword_sku_map.items()]
        sku_data = [{"sku": k, "keywords": list(v)} for k, v in self.sku_keyword_map.items()]
        
        df_keyword = pd.DataFrame(keyword_data)
        df_sku = pd.DataFrame(sku_data)
        
        with pd.ExcelWriter(Path("attached_assets/keyword_sku_mappings.xlsx")) as writer:
            df_keyword.to_excel(writer, sheet_name='keyword_to_sku', index=False)
            df_sku.to_excel(writer, sheet_name='sku_to_keyword', index=False)

    def update_mappings_from_bulk(self, bulk_file: str):
        df = pd.read_excel(bulk_file)
        
        keyword_columns = ['Keyword-Text', 'Keyword', 'keyword']
        keyword_col = None
        for col in keyword_columns:
            alt_name = self.dict_manager.get_value(col)
            if col in df.columns:
                keyword_col = col
                break
            elif alt_name and alt_name in df.columns:
                keyword_col = alt_name
                break
                
        if not keyword_col:
            return False
            
        for ad_group_id in df['Anzeigengruppen-ID'].unique():
            group_df = df[df['Anzeigengruppen-ID'] == ad_group_id]
            
            keywords = set(group_df[keyword_col].dropna())
            skus = set(group_df['SKU'].dropna())
            
            for keyword in keywords:
                if keyword not in self.keyword_sku_map:
                    self.keyword_sku_map[keyword] = set()
                self.keyword_sku_map[keyword].update(skus)
                
            for sku in skus:
                if sku not in self.sku_keyword_map:
                    self.sku_keyword_map[sku] = set()
                self.sku_keyword_map[sku].update(keywords)
        
        self.save_mappings()
        return True

    def get_skus_for_keyword(self, keyword: str) -> Set[str]:
        return self.keyword_sku_map.get(keyword, set())

    def get_keywords_for_sku(self, sku: str) -> Set[str]:
        return self.sku_keyword_map.get(sku, set())
        
    @staticmethod
    def preprocess_sku(sku: str) -> str:
        if not isinstance(sku, str):
            sku = str(sku)
        cleaned = sku.strip().upper()
        prefixes = ["ARTIKEL NR.", "ARTIKEL-NR.", "SKU-", "SKU:", "ART."]
        for prefix in prefixes:
            if cleaned.startswith(prefix):
                cleaned = cleaned[len(prefix):].strip()
        cleaned = re.sub(r'[^\w\-]', '', cleaned)
        return cleaned
    
    def find_exact_match(self, input_sku: str) -> Optional[str]:
        cleaned_input = self.preprocess_sku(input_sku)
        try:
            idx = self.cleaned_known_skus.index(cleaned_input)
            return self.known_skus[idx]
        except ValueError:
            return None
    
    def find_fuzzy_match(self, input_sku: str, threshold: int = 80) -> Tuple[Optional[str], int]:
        cleaned_input = self.preprocess_sku(input_sku)
        best_match, score, idx = process.extractOne(
            cleaned_input,
            self.cleaned_known_skus,
            scorer=fuzz.token_sort_ratio
        )
        if score >= threshold:
            return self.known_skus[idx], score
        return None, score
    
    def find_best_match(self, input_sku: str, threshold: int = 80) -> Tuple[Optional[str], int, str]:
        exact_match = self.find_exact_match(input_sku)
        if exact_match:
            return exact_match, 100, "exact"
        fuzzy_match, score = self.find_fuzzy_match(input_sku, threshold)
        if fuzzy_match:
            return fuzzy_match, score, "fuzzy"
        return None, score, "no_match"