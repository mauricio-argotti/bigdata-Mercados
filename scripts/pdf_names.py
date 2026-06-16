PDF_FILENAMES = {
    "es": "BigDataEnLosMercadosFinancieros.pdf",
    "en": "BigDataInFinancialMarkets.pdf",
}

DEFAULT_PDF_FILENAME = PDF_FILENAMES["es"]


def pdf_filename_for_lang(lang):
    return PDF_FILENAMES.get(lang, f"TeachBook_{lang}.pdf")
