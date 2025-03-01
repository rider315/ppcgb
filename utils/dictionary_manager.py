from typing import Dict

class DictionaryManager5Lang:
    def __init__(self):
        self.translations = {
            "Sponsored Products-Kampagnen": {
                "de": "Sponsored Products-Kampagnen",
                "en": "Sponsored Products Campaigns",
                "es": "Campañas de productos patrocinados",
                "it": "Campagne di prodotti sponsorizzati",
                "fr": "Campagnes de produits sponsorisés",
            },
            "Produkt": {
                "de": "Produkt",
                "en": "Product",
                "es": "Producto",
                "it": "Prodotto",
                "fr": "Produit",
            },
            "Entität": {
                "de": "Entität",
                "en": "Entity",
                "es": "Entidad",
                "it": "Entità",
                "fr": "Entité",
            },
            "Operation": {
                "de": "Operation",
                "en": "Operation",
                "es": "Operación",
                "it": "Operazione",
                "fr": "Opération",
            },
            "Kampagnen-ID": {
                "de": "Kampagnen-ID",
                "en": "Campaign ID",
                "es": "ID de campaña",
                "it": "ID campagna",
                "fr": "ID de campagne",
            },
            "Kampagnen-Typ": {
                "de": "Kampagnen-Typ",
                "en": "Campaign Type",
                "es": "Tipo de campaña",
                "it": "Tipo di campagna",
                "fr": "Type de campagne",
            },
            "Anzeigengruppen-ID": {
                "de": "Anzeigengruppen-ID",
                "en": "Ad group ID",
                "es": "ID del grupo de anuncios",
                "it": "ID del gruppo di annunci",
                "fr": "ID du groupe d'annonces",
            },
            "Portfolio-ID": {
                "de": "Portfolio-ID",
                "en": "Portfolio ID",
                "es": "ID de la cartera",
                "it": "ID del portfolio",
                "fr": "ID du portefeuille",
            },
            "Anzeigen-ID": {
                "de": "Anzeigen-ID",
                "en": "Ad ID",
                "es": "ID del anuncio",
                "it": "ID annuncio",
                "fr": "ID de l'annonce",
            },
            "Keyword-ID": {
                "de": "Keyword-ID",
                "en": "Keyword ID",
                "es": "ID de palabra clave",
                "it": "ID parola chiave",
                "fr": "ID de mot clé",
            },
            "Produkt-Targeting-ID": {
                "de": "Produkt-Targeting-ID",
                "en": "Product Targeting ID",
                "es": "ID de orientación de productos",
                "it": "ID di targeting del prodotto",
                "fr": "ID de ciblage de produits",
            },
            "Kampagnenname": {
                "de": "Kampagnenname",
                "en": "Campaign name",
                "es": "Nombre de la campaña",
                "it": "Nome della campagna",
                "fr": "Nom de la campagne",
            },
            "Name der Anzeigengruppe": {
                "de": "Name der Anzeigengruppe",
                "en": "Ad group name",
                "es": "Nombre del grupo de anuncios",
                "it": "Nome del gruppo di annunci",
                "fr": "Nom du groupe d'annonces",
            },
            "Kampagnenname (Nur zu Informationszwecken)": {
                "de": "Kampagnenname (Nur zu Informationszwecken)",
                "en": "Campaign name (Informational only)",
                "es": "Nombre de la campaña (solo informativo)",
                "it": "Nome della campagna (solo informativo)",
                "fr": "Nom de la campagne (à titre informatif seulement)",
            },
            "Name der Anzeigengruppe (Nur zu Informationszwecken)": {
                "de": "Name der Anzeigengruppe (Nur zu Informationszwecken)",
                "en": "Ad group name (Informational only)",
                "es": "Nombre del grupo de anuncios (solo informativo)",
                "it": "Nome del gruppo di annunci (solo informativo)",
                "fr": "Nom du groupe d'annonces (à titre informatif seulement)",
            },
            "Portfolioname (Nur zu Informationszwecken)": {
                "de": "Portfolioname (Nur zu Informationszwecken)",
                "en": "Portfolio name (Informational only)",
                "es": "Nombre de la cartera (solo informativo)",
                "it": "Nome del portfolio (solo informativo)",
                "fr": "Nom du portefeuille (à titre informatif seulement)",
            },
            "Startdatum": {
                "de": "Startdatum",
                "en": "Start date",
                "es": "Fecha de inicio",
                "it": "Data di inizio",
                "fr": "Date de début",
            },
            "Enddatum": {
                "de": "Enddatum",
                "en": "End date",
                "es": "Fecha de finalización",
                "it": "Data di fine",
                "fr": "Date de fin",
            },
            "Targeting-Typ": {
                "de": "Targeting-Typ",
                "en": "Targeting type",
                "es": "Tipo de orientación",
                "it": "Tipo di targeting",
                "fr": "Type de ciblage",
            },
            "Zustand": {
                "de": "Zustand",
                "en": "State",
                "es": "Estado",
                "it": "Stato",
                "fr": "État",
            },
            "Kampagnenstatus (Nur zu Informationszwecken)": {
                "de": "Kampagnenstatus (Nur zu Informationszwecken)",
                "en": "Campaign state (Informational only)",
                "es": "Estado de la campaña (solo informativo)",
                "it": "Stato della campagna (solo informativo)",
                "fr": "État de la campagne (à titre informatif seulement)",
            },
            "Anzeigengruppen-Status (Nur zu Informationszwecken)": {
                "de": "Anzeigengruppen-Status (Nur zu Informationszwecken)",
                "en": "Ad Group State (Informational only)",
                "es": "Estado del grupo de anuncios (solo informativo)",
                "it": "Stato del gruppo di annunci (solo informativo)",
                "fr": "État du groupe d'annonces (à titre informatif seulement)",
            },
            "Tagesbudget": {
                "de": "Tagesbudget",
                "en": "Daily budget",
                "es": "Presupuesto diario",
                "it": "Budget giornaliero",
                "fr": "Budget quotidien",
            },
            "SKU": {
                "de": "SKU",
                "en": "SKU",
                "es": "SKU",
                "it": "SKU",
                "fr": "SKU",
            },
            "ASIN (Nur zu Informationszwecken)": {
                "de": "ASIN (Nur zu Informationszwecken)",
                "en": "ASIN (Informational only)",
                "es": "ASIN (solo informativo)",
                "it": "ASIN (solo informativo)",
                "fr": "ASIN (à titre informatif seulement)",
            },
            "Berechtigungsstatus (Nur zu Informationszwecken)": {
                "de": "Berechtigungsstatus (Nur zu Informationszwecken)",
                "en": "Eligibility status (Informational only)",
                "es": "Estado de elegibilidad (solo informativo)",
                "it": "Stato di idoneità (solo informativo)",
                "fr": "Statut d'éligibilité (à titre informatif seulement)",
            },
            "Grund der Unzulässigkeit (Nur zu Informationszwecken)": {
                "de": "Grund der Unzulässigkeit (Nur zu Informationszwecken)",
                "en": "Reason for ineligibility (Informational only)",
                "es": "Motivo de inelegibilidad (solo informativo)",
                "it": "Motivo di ineleggibilità (solo informativo)",
                "fr": "Raison d'inéligibilité (à titre informatif seulement)",
            },
            "Standardgebot für die Anzeigengruppe": {
                "de": "Standardgebot für die Anzeigengruppe",
                "en": "Ad Group Default Bid",
                "es": "Oferta predeterminada del grupo de anuncios",
                "it": "Offerta predefinita del gruppo di annunci",
                "fr": "Enchère par défaut du groupe d'annonces",
            },
            "Standardgebot für die Anzeigengruppe (Nur zu Informationszwecken)": {
                "de": "Standardgebot für die Anzeigengruppe (Nur zu Informationszwecken)",
                "en": "Ad Group Default Bid (Informational only)",
                "es": "Oferta predeterminada del grupo de anuncios (solo informativo)",
                "it": "Offerta predefinita del gruppo di annunci (solo informativo)",
                "fr": "Enchère par défaut du groupe d'annonces (à titre informatif seulement)",
            },
            "Gebot": {
                "de": "Gebot",
                "en": "Bid",
                "es": "Oferta",
                "it": "Offerta",
                "fr": "Enchère",
            },
            "Keyword-Text": {
                "de": "Keyword-Text",
                "en": "Keyword text",
                "es": "Texto de palabra clave",
                "it": "Testo parola chiave",
                "fr": "Texte du mot clé",
            },
            "Keyword": {
                "de": "Keyword",
                "en": "Keyword text",
                "es": "Palabra clave",
                "it": "Parola chiave",
                "fr": "Mot clé",
            },
            "Muttersprache Keyword": {
                "de": "Muttersprache Keyword",
                "en": "Native language keyword",
                "es": "Palabra clave en idioma nativo",
                "it": "Parola chiave in lingua madre",
                "fr": "Mot clé en langue maternelle",
            },
            "Muttersprache Lokalisierung": {
                "de": "Muttersprache Lokalisierung",
                "en": "Native language locale",
                "es": "Ubicación en idioma nativo",
                "it": "Località in lingua madre",
                "fr": "Localité en langue maternelle",
            },
            "Übereinstimmungstyp": {
                "de": "Übereinstimmungstyp",
                "en": "Match type",
                "es": "Tipo de coincidencia",
                "it": "Tipo di corrispondenza",
                "fr": "Type de correspondance",
            },
            "Gebotsstrategie": {
                "de": "Gebotsstrategie",
                "en": "Bidding strategy",
                "es": "Estrategia de ofertas",
                "it": "Strategia di offerta",
                "fr": "Stratégie d'enchères",
            },
            "Platzierung": {
                "de": "Platzierung",
                "en": "Placement",
                "es": "Colocación",
                "it": "Posizionamento",
                "fr": "Placement",
            },
            "Prozentsatz": {
                "de": "Prozentsatz",
                "en": "Percentage",
                "es": "Porcentaje",
                "it": "Percentuale",
                "fr": "Pourcentage",
            },
            "Ausdruck für Produkt-Targeting": {
                "de": "Ausdruck für Produkt-Targeting",
                "en": "Product targeting expression",
                "es": "Expresión de orientación de productos",
                "it": "Espressione di targeting del prodotto",
                "fr": "Expression de ciblage de produits",
            },
            "Problem mit dem Ausdruck fuer Produkt-Targeting Behoben (Nur zu Informationszwecken)": {
                "de": "Problem mit dem Ausdruck für Produkt-Targeting Behoben (Nur zu Informationszwecken)",
                "en": "Resolved product targeting expression (Informational only)",
                "es": "Expresión de orientación de productos resuelta (solo informativo)",
                "it": "Espressione di targeting del prodotto risolta (solo informativo)",
                "fr": "Expression de ciblage de produits résolue (à titre informatif seulement)",
            },
            "Impressions": {
                "de": "Impressions",
                "en": "Impressions",
                "es": "Impresiones",
                "it": "Impressioni",
                "fr": "Impressions",
            },
            "Klicks": {
                "de": "Klicks",
                "en": "Clicks",
                "es": "Clics",
                "it": "Click",
                "fr": "Clics",
            },
            "Klickrate": {
                "de": "Klickrate",
                "en": "Click-through rate",
                "es": "Tasa de clics",
                "it": "Tasso di click-through",
                "fr": "Taux de clics",
            },
            "Ausgaben": {
                "de": "Ausgaben",
                "en": "Spend",
                "es": "Gastos",
                "it": "Spese",
                "fr": "Dépenses",
            },
            "Verkäufe": {
                "de": "Verkäufe",
                "en": "Sales",
                "es": "Ventas",
                "it": "Vendite",
                "fr": "Ventes",
            },
            "Bestellungen": {
                "de": "Bestellungen",
                "en": "Orders",
                "es": "Pedidos",
                "it": "Ordini",
                "fr": "Commandes",
            },
            "Einheiten": {
                "de": "Einheiten",
                "en": "Units",
                "es": "Unidades",
                "it": "Unità",
                "fr": "Unités",
            },
            "Conversion-Rate": {
                "de": "Conversion-Rate",
                "en": "Conversion rate",
                "es": "Tasa de conversión",
                "it": "Tasso di conversione",
                "fr": "Taux de conversion",
            },
            "ACOS": {
                "de": "ACOS",
                "en": "ACOS",
                "es": "ACOS",
                "it": "ACOS",
                "fr": "ACOS",
            },
            "CPC": {
                "de": "CPC",
                "en": "CPC",
                "es": "CPC",
                "it": "CPC",
                "fr": "CPC",
            },
            "ROAS": {
                "de": "ROAS",
                "en": "ROAS",
                "es": "ROAS",
                "it": "ROAS",
                "fr": "ROAS",
            },
            "Altes Gebot": {
                "de": "Altes Gebot",
                "en": "Old bid",
                "es": "Oferta anterior",
                "it": "Offerta precedente",
                "fr": "Ancienne enchère",
            },
            "Neues Gebot": {
                "de": "Neues Gebot",
                "en": "New bid",
                "es": "Nueva oferta",
                "it": "Nuova offerta",
                "fr": "Nouvelle enchère",
            },
            "Veränderung in %": {
                "de": "Veränderung in %",
                "en": "Change in %",
                "es": "Cambio en %",
                "it": "Variazione in %",
                "fr": "Changement en %",
            },
            "Veränderung in €": {
                "de": "Veränderung in €",
                "en": "Change in €",
                "es": "Cambio en €",
                "it": "Variazione in €",
                "fr": "Changement en €",
            },
            "dämpfungsfaktor": {
                "de": "dämpfungsfaktor",
                "en": "damping factor",
                "es": "factor de amortiguación",
                "it": "fattore di smorzamento",
                "fr": "facteur d'amortissement",
            },
            "max_erhöhung": {
                "de": "max_erhöhung",
                "en": "max increase",
                "es": "incremento máximo",
                "it": "aumento massimo",
                "fr": "augmentation maximale",
            },
            "max_senkung": {
                "de": "max_senkung",
                "en": "max decrease",
                "es": "disminución máxima",
                "it": "diminuzione massima",
                "fr": "diminution maximale",
            },
            "impressionen_schwelle": {
                "de": "impressionen_schwelle",
                "en": "impression threshold",
                "es": "umbral de impresiones",
                "it": "soglia impressioni",
                "fr": "seuil d'impressions",
            },
            "impressionen_boost": {
                "de": "impressionen_boost",
                "en": "impression boost",
                "es": "impulso de impresiones",
                "it": "boost impressioni",
                "fr": "boost d'impressions",
            },
            "conversion_einfluss": {
                "de": "conversion_einfluss",
                "en": "conversion impact",
                "es": "impacto de conversión",
                "it": "impatto conversione",
                "fr": "impact de conversion",
            }
        }

        self.english_headers = [
            "Product", "Entity", "Operation", "Campaign ID", "Ad group ID",
            "Portfolio ID", "Ad ID", "Keyword ID", "Product Targeting ID",
            "Campaign name", "Ad group name", "Campaign name (Informational only)",
            "Ad group name (Informational only)", "Portfolio name (Informational only)",
            "Start date", "End date", "Targeting type", "State",
            "Campaign state (Informational only)", "Ad Group State (Informational only)",
            "Daily budget", "SKU", "ASIN (Informational only)",
            "Eligibility status (Informational only)",
            "Reason for ineligibility (Informational only)",
            "Ad Group Default Bid", "Ad Group Default Bid (Informational only)",
            "Bid", "Keyword text", "Native language keyword", "Native language locale",
            "Match type", "Bidding strategy", "Placement", "Percentage",
            "Product targeting expression",
            "Resolved product targeting expression (Informational only)",
            "Impressions", "Clicks", "Click-through rate", "Spend", "Sales",
            "Orders", "Units", "Conversion rate", "ACOS", "CPC", "ROAS"
        ]

        self.mapping_en_to_de = {
            "Product": "Produkt",
            "Entity": "Entität",
            "Operation": "Operation",
            "Campaign ID": "Kampagnen-ID",
            "Ad group ID": "Anzeigengruppen-ID",
            "Portfolio ID": "Portfolio-ID",
            "Ad ID": "Anzeigen-ID",
            "Keyword ID": "Keyword-ID",
            "Product Targeting ID": "Produkt-Targeting-ID",
            "Campaign name": "Kampagnenname",
            "Ad group name": "Name der Anzeigengruppe",
            "Campaign name (Informational only)": "Kampagnenname (Nur zu Informationszwecken)",
            "Ad group name (Informational only)": "Name der Anzeigengruppe (Nur zu Informationszwecken)",
            "Portfolio name (Informational only)": "Portfolioname (Nur zu Informationszwecken)",
            "Start date": "Startdatum",
            "End date": "Enddatum",
            "Targeting type": "Targeting-Typ",
            "State": "Zustand",
            "Campaign state (Informational only)": "Kampagnenstatus (Nur zu Informationszwecken)",
            "Ad Group State (Informational only)": "Anzeigengruppen-Status (Nur zu Informationszwecken)",
            "Daily budget": "Tagesbudget",
            "SKU": "SKU",
            "ASIN (Informational only)": "ASIN (Nur zu Informationszwecken)",
            "Eligibility status (Informational only)": "Berechtigungsstatus (Nur zu Informationszwecken)",
            "Reason for ineligibility (Informational only)": "Grund der Unzulässigkeit (Nur zu Informationszwecken)",
            "Ad Group Default Bid": "Standardgebot für die Anzeigengruppe",
            "Ad Group Default Bid (Informational only)": "Standardgebot für die Anzeigengruppe (Nur zu Informationszwecken)",
            "Bid": "Gebot",
            "Keyword text": "Keyword-Text",
            "Native language keyword": "Muttersprache Keyword",
            "Native language locale": "Muttersprache Lokalisierung",
            "Match type": "Übereinstimmungstyp",
            "Bidding strategy": "Gebotsstrategie",
            "Placement": "Platzierung",
            "Percentage": "Prozentsatz",
            "Product targeting expression": "Ausdruck für Produkt-Targeting",
            "Resolved product targeting expression (Informational only)": "Problem mit dem Ausdruck für Produkt-Targeting Behoben (Nur zu Informationszwecken)",
            "Impressions": "Impressions",
            "Clicks": "Klicks",
            "Click-through rate": "Klickrate",
            "Spend": "Ausgaben",
            "Sales": "Verkäufe",
            "Orders": "Bestellungen",
            "Units": "Einheiten",
            "Conversion rate": "Conversion-Rate",
            "ACOS": "ACOS",
            "CPC": "CPC",
            "ROAS": "ROAS"
        }

        for en_key in self.english_headers:
            if en_key in self.translations:
                continue

            de_key = self.mapping_en_to_de.get(en_key)
            if de_key and de_key in self.translations:
                source_dict = self.translations[de_key]
                new_entry = {
                    "de": source_dict["de"],
                    "en": source_dict["en"],
                    "es": source_dict.get("es", source_dict["en"]),
                    "it": source_dict.get("it", source_dict["en"]),
                    "fr": source_dict.get("fr", source_dict["en"]),
                }
                self.translations[en_key] = new_entry
            else:
                self.translations[en_key] = {
                    "de": en_key,
                    "en": en_key,
                    "es": en_key,
                    "it": en_key,
                    "fr": en_key
                }

    def get_translations_for(self, key: str) -> Dict[str, str]:
        """Get all 5 language variants for a specific term (key)."""
        return self.translations.get(key, {})

    def get_translation(self, key: str, lang_code: str, default: str = "") -> str:
        """Get a single translation (e.g., 'Campaign name' in 'fr')."""
        return self.translations.get(key, {}).get(lang_code, default)

    def add_key(self, key: str, translations_5_lang: Dict[str, str]) -> None:
        """
        Add a new key->Dict(5) mapping.
        translations_5_lang must contain 5 languages (de,en,es,it,fr)
        """
        self.translations[key] = translations_5_lang

    def get_all_translations(self) -> Dict[str, Dict[str, str]]:
        """Get a complete copy of all translations."""
        return self.translations.copy()