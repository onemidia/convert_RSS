
import xml.etree.ElementTree as ET

def convert_to_rss(file_path):
    root = ET.Element("rss", version="2.0")
    channel = ET.SubElement(root, "channel")
    ET.SubElement(channel, "title").text = "Arquivo Convertido"
    ET.SubElement(channel, "description").text = "Feed gerado automaticamente."
    ET.SubElement(channel, "link").text = "http://localhost"
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            item = ET.SubElement(channel, "item")
            ET.SubElement(item, "title").text = line.strip()
    
    return ET.tostring(root, encoding='utf-8').decode('utf-8')