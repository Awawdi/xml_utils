import logging
import json
from logging import Logger
from logger_singleton import get_logger
from xml_utils import xml_to_dict, dict_to_xml


def demo_conversion(xml_input: str) -> tuple[dict, str, str]:
    """
    Demonstrates usage of xml_to_dict, dict_to_xml, and JSON conversion.
    
    :param xml_input: XML string to convert to dictionary, JSON, and back to XML.
    :return: A tuple containing:
        - parsed dictionary,
        - JSON string,
        - re-generated XML string.
    """
    
    logger = get_logger("XMLConverter")

    # Convert XML to dict
    data_dict = xml_to_dict(xml_input, logger)

    # Convert dict to JSON
    json_output = json.dumps(data_dict, indent=4, ensure_ascii=False)

    if logger:
        logger.info("Parsed dictionary converted to JSON.")

    # Convert dict back to XML
    xml_output = dict_to_xml(data_dict, logger)

    return data_dict, json_output, xml_output


# Example usage
if __name__ == "__main__":
    example_xml = """
    <note>
        <from>Sender</from>
        <to>Receiver</to>
        <heading>Reminder</heading>
        <body>Task to accomplish</body>
    </note>
    """

    result_dict, result_json, result_xml = demo_conversion(example_xml)

    print("Parsed Dictionary:")
    print(result_dict)

    print("\nGenerated JSON:")
    print(result_json)

    print("\nGenerated XML:")
    print(result_xml)
