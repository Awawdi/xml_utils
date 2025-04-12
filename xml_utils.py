from logging import Logger

import xmltodict


def xml_to_dict(xml_input: str, logger: Logger = None) -> dict[str, any]:
    """
    Converts an XML string into a Python dictionary.

    :param xml_input: The XML string to be parsed.
    :param logger: (Optional) A Logger instance to log the parsing process.
                   If provided, logs an informational message before parsing.
    :return: A dictionary representation of the XML data.
    """
    if logger:
        logger.info("Parsing data from XML to dictionary.")
    return xmltodict.parse(xml_input, encoding="utf-8")


def dict_to_xml(data: dict, logger: Logger = None) -> str:
    """
    Converts a Python dictionary into an XML string.

    :param data: The dictionary to be converted into XML format.
    :param logger: (Optional) A Logger instance to log the conversion process.
                   If provided, logs an informational message before conversion.
    :return: An XML string representation of the dictionary.
    """
    if logger:
        logger.info("Parsing data from dictionary to XML.")
    return xmltodict.unparse(data, pretty=True, full_document=True)