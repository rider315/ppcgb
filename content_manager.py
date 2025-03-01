import streamlit as st
from typing import Dict, Optional, Any
import logging
logger = logging.getLogger(__name__)

class ContentManager:
    def __init__(self):
        """
        Defines default and page-specific texts that can be displayed dynamically in navigation.
        Supports multiple languages (DE/EN).
        """
        if "feed_goat_after_upload" not in st.session_state:
            st.session_state.feed_goat_after_upload = False
        if "pulse_abenteuer_planen" not in st.session_state:
            st.session_state.pulse_abenteuer_planen = False

        # Language initialization moved to navigation.py
        # Language state is now managed centrally

        self.default_greeting = {
            'de': {
                'title': "👋 Hi, ich bin Henri – besser bekannt als PPC GOAT. 🐐",
                'message': """
                    Ich bin dein zuverlässiger Partner, wenn es darum geht, deine PPC-Kampagnen auf Amazon zu optimieren. 
                    Egal, ob du gerade erst startest oder deine Performance aufs nächste Level bringen möchtest – 
                    ich bin da, um dir zu helfen.
                """
            },
            'en': {
                'title': "👋 Hi, I'm Henri – better known as PPC GOAT. 🐐",
                'message': """
                    I'm your reliable partner when it comes to optimizing your PPC campaigns on Amazon.
                    Whether you're just starting out or want to take your performance to the next level –
                    I'm here to help you.
                """
            }
        }

        self.page_content = {
            'feed_goat': {
                'de': {
                    'page_title': "Henri füttern - PPC GOAT",
                    'main_title': "🌾 Zeit für eine kleine Stärkung!",
                    'tabs': {
                        'bulk_file': "📤 Bulk Datei",
                        'amazon_api': "🔌 Amazon API",
                        'login': "🔐 Login"
                    },
                    'upload_title': "📤 Bulk-Datei hochladen",
                    'upload_description': """
                        Damit ich dir bei deinen PPC-Kampagnen helfen kann, brauche ich erst mal was zu futtern.
                        Lade deine Bulk-Datei hoch, und ich schaue mir an, was ich daraus lernen kann!
                    """,
                    'login_section': {
                        'title': "🔐 Login",
                        'description': """
                            Melde dich an, um auf deine PPC-Kampagnen zuzugreifen und sie zu optimieren.
                            Du kannst dich entweder direkt anmelden oder die Amazon API verwenden.
                        """,
                        'email_label': "E-Mail",
                        'password_label': "Passwort",
                        'login_button': "Anmelden"
                    },
                    'api_section': {
                        'title': "🔌 Amazon API",
                        'description': "Verbinde dich direkt mit deinem Amazon-Konto für automatischen Datenzugriff",
                        'connect_button': "Mit Amazon verbinden"
                    },
                    'upload_section': {
                        'upload_instructions': """
                            ### So lädst du deine Bulk-Export-Datei hoch:
                            1. 📥 Exportiere deine Kampagnendaten aus dem Amazon Advertising-Interface  
                            2. 💾 Speichere die Datei als **XLSX**-Format  
                            3. 🖱️ Ziehe die Datei in den Upload-Bereich oder klicke zum Auswählen  
                        """,
                        'file_types': "Unterstützte Formate: XLSX • Maximal 200MB",
                        'drag_drop_text': "Ziehe deine Datei hier hin oder klicke zum Auswählen",
                        'uploader_help': "Wähle deine Datei und los geht's!",
                        'process_button': "🗺️ Jetzt Abenteuer planen"
                    }
                },
                'en': {
                    'page_title': "Feed Henri - PPC GOAT",
                    'main_title': "🌾 Time for a Little Snack!",
                    'tabs': {
                        'bulk_file': "📤 Bulk File",
                        'amazon_api': "🔌 Amazon API",
                        'login': "🔐 Login"
                    },
                    'upload_title': "📤 Upload Bulk File",
                    'upload_description': """
                        To help you with your PPC campaigns, I need something to eat first.
                        Upload your bulk file, and I'll see what I can learn from it!
                    """,
                    'login_section': {
                        'title': "🔐 Login",
                        'description': """
                            Sign in to access and optimize your PPC campaigns.
                            You can either log in directly or use the Amazon API.
                        """,
                        'email_label': "Email",
                        'password_label': "Password",
                        'login_button': "Sign In"
                    },
                    'api_section': {
                        'title': "🔌 Amazon API",
                        'description': "Connect directly with your Amazon account for automatic data access",
                        'connect_button': "Connect with Amazon"
                    },
                    'upload_section': {
                        'upload_instructions': """
                            ### How to upload your bulk export file:
                            1. 📥 Export your campaign data from the Amazon Advertising interface  
                            2. 💾 Save the file in **XLSX** format  
                            3. 🖱️ Drag the file into the upload area or click to select  
                        """,
                        'file_types': "Supported formats: XLSX • Maximum 200MB",
                        'drag_drop_text': "Drop your file here or click to select",
                        'uploader_help': "Choose your file and let's go!",
                        'process_button': "🗺️ Plan Adventure Now"
                    }
                }
            },
            'abenteuer_planen': {
                'de': {
                    'page_title': "Abenteuer planen - PPC GOAT",
                    'main_title': "📊 Wohin geht's?",
                    'optimization_question': "Auf welchen Wert möchtest du optimieren?",
                    'optimization_goal': "Optimierungsziel",
                    'target_value': "Zielwert",
                    'equipment_title': "🎒 Henris Ausrüstung",
                    'strategy_select': "Wähle deine Strategie",
                    'advanced_equipment': "⚙️ Erweitertes Equipment",
                    'advanced_description': "Hier kannst du Dämpfungsfaktor, max. Erhöhung/Senkung, Impressionen-Boost etc. anpassen",
                    'parameters': {
                        "damping_factor": "Dämpfungsfaktor",
                        "max_increase": "Maximale Erhöhung",
                        "max_decrease": "Maximale Senkung",
                        "impression_threshold": "Impressionen-Schwelle",
                        "impression_boost": "Impressionen-Boost",
                        "conversion_rate_impact": "Conversion-Rate Einfluss"
                    },
                    'strategies': {
                        'standard': "Standard",
                        'light': "Leicht",
                        'heavy': "Schwer",
                        'custom': "Individuell"
                    },
                    'sku_config_title': "🔧 SKU-spezifische Konfiguration (Coming Soon)",
                    'sku_config_info': """
                    🚧 Feature in Entwicklung

                    Die individuelle SKU-Konfiguration ist derzeit deaktiviert und wird in einer 
                    späteren Version verfügbar sein. Aktuell werden die globalen Einstellungen 
                    für alle SKUs verwendet.

                    Geplante Funktionen:
                    - Individuelle ROAS-Ziele pro SKU
                    - Spezifische Strategien für einzelne SKUs
                    - Erweiterte SKU-Gruppierung
                    """,
                    'sku_config_checkbox': "Ausrüstung individuell konfigurieren",
                    'sku_select': "SKU auswählen",
                    'strategy_select_sku': "Strategie",
                    'target_roas': "Ziel-ROAS",
                    'add_sku_button': "Weitere SKU-Regel erstellen",
                    'save_button': "🎯 Ausrüstung und Ziel speichern",
                    'success_message': "Ausrüstung & Ziele gespeichert! Besuche jetzt 'Abenteuer erleben' für den finalen Schritt.",
                    'saved_values': "Gespeicherte Werte",
                    'error_messages': {
                        'missing_columns': "Es fehlen Spalten"
                    }
                },
                'en': {
                    'page_title': "Plan Adventure - PPC GOAT",
                    'main_title': "📊 Where to?",
                    'optimization_question': "What value do you want to optimize for?",
                    'optimization_goal': "Optimization Goal",
                    'target_value': "Target Value",
                    'equipment_title': "🎒 Henri's Equipment",
                    'strategy_select': "Choose your strategy",
                    'advanced_equipment': "⚙️ Advanced Equipment",
                    'advanced_description': "Here you can adjust damping factor, max increase/decrease, impression boost, etc.",
                    'parameters': {
                        "damping_factor": "Damping Factor",
                        "max_increase": "Maximum Increase",
                        "max_decrease": "Maximum Decrease",
                        "impression_threshold": "Impression Threshold",
                        "impression_boost": "Impression Boost",
                        "conversion_rate_impact": "Conversion Rate Impact"
                    },
                    'strategies': {
                        'standard': "Standard",
                        'light': "Light",
                        'heavy': "Heavy",
                        'custom': "Custom"
                    },
                    'sku_config_title': "🔧 SKU-specific Configuration (Coming Soon)",
                    'sku_config_info': """
                    🚧 Feature in Development

                    Individual SKU configuration is currently disabled and will be available in a
                    later version. Currently, global settings are used for all SKUs.

                    Planned features:
                    - Individual ROAS targets per SKU
                    - Specific strategies for individual SKUs
                    - Advanced SKU grouping
                    """,
                    'sku_config_checkbox': "Configure equipment individually",
                    'sku_select': "Select SKU",
                    'strategy_select_sku': "Strategy",
                    'target_roas': "Target ROAS",
                    'add_sku_button': "Add another SKU rule",
                    'save_button': "🎯 Save Equipment and Target",
                    'success_message': "Equipment & goals saved! Visit 'Experience Adventure' for the final step.",
                    'saved_values': "Saved values",
                    'error_messages': {
                        'missing_columns': "Missing columns"
                    }
                }

            },
            'abenteuer_erleben': {
                'de': {
                    'page_title': "Abenteuer erleben - PPC GOAT",
                    'main_title': "🗺️ Auf zu neuen Abenteuern!",
                    'results_title': "Ergebnisse & Download",
                    'download_button': "Bulk-Datei herunterladen",
                    'error_messages': {
                        'no_file': "⚠️ Keine Datei gefunden. Bitte erst unter 'Henri füttern' eine Bulk-Datei hochladen!",
                        'invalid_format': "Ungültiges Dateiformat",
                        'missing_columns': "Es fehlen Spalten"
                    }
                },
                'en': {
                    'page_title': "Experience Adventure - PPC GOAT",
                    'main_title': "🗺️ Off to New Adventures!",
                    'results_title': "Results & Download",
                    'download_button': "Download Bulk File",
                    'error_messages': {
                        'no_file': "⚠️ No file found. Please upload a bulk file under 'Feed Henri' first!",
                        'invalid_format': "Invalid file format",
                        'missing_columns': "Missing columns"
                    }
                }
            }
        }

    def get_page_content(self, page: str) -> Dict[str, Any]:
        """
        Returns the content for a specific page in the current language.
        """
        try:
            # Get language from session state, managed by navigation
            lang = st.session_state.get('language', 'de')
            return self.page_content.get(page, {}).get(lang, {})
        except Exception as e:
            st.error(f"Error in ContentManager.get_page_content: {str(e)}")
            return {}

    def get_content(self, page: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, str]:
        """
        Returns the appropriate text (title + message) based on page and context.
        Uses the language setting from session state.
        """
        try:
            # Get language from session state, managed by navigation
            lang = st.session_state.get('language', 'de')

            # If no context provided, use empty dict
            context = context or {}

            # Get default greeting based on language
            default_content = {
                'title': self.default_greeting[lang]['title'],
                'message': self.default_greeting[lang]['message']
            }

            # Special cases based on context
            if context.get("equipment_saved"):
                saved_content = {
                    'de': {
                        'title': "🎯 Super, alles gespeichert und bereit!",
                        'message': """
                            Ich habe deine Ausrüstung und Ziele gespeichert. Jetzt sind wir bereit für das nächste
                            Abenteuer! Klicke auf 'Abenteuer erleben' in der Navigation, um loszulegen.
                        """
                    },
                    'en': {
                        'title': "🎯 Great, everything saved and ready!",
                        'message': """
                            I've saved your equipment and goals. Now we're ready for the next
                            adventure! Click on 'Experience Adventure' in the navigation to get started.
                        """
                    }
                }
                return saved_content[lang]

            # Default to page content if available
            page_content = self.page_content.get(page, {}).get(lang, {})
            if page_content:
                return {
                    'title': page_content.get('main_title', default_content['title']),
                    'message': page_content.get('upload_description', default_content['message'])
                }

            # Fallback to default greeting
            return default_content

        except Exception as e:
            logger.error(f"Error in ContentManager.get_content: {str(e)}")
            return self.default_greeting[st.session_state.get('language', 'de')]