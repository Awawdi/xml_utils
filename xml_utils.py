from logging import Logger

import xmltodict


def xml_to_dict(xml_input: str, logger: Logger = None) -> dict[str, any]:
    """
    The method parse XML string to dictionary.
    :param logger: The logger to write to.
    :param xml_input: The xml input that will be parsed to dictionary.
    :return: A dictionary that contain xml tags as keys, and their value as dictionary values.
    """

    if logger:
        logger.info("Parsing data from XML to dictionary.")
    return xmltodict.parse(xml_input, encoding="utf-8")


def dict_to_xml(data: dict, logger: Logger = None) -> str:
    """
    The method parse dictionary to XML str.
    :param logger: The logger to write to.
    :param data: The dictionary we want to parse into XML string.
    :return: XML string.
    """

    if logger:
        logger.info("Parsing data from dictionary to XML.")
    return xmltodict.unparse(data, pretty=True, full_document=True)