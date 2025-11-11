from lxml import etree
import os
from tqdm import tqdm

def alto_to_tei(alto_path):
    # ALTO namespace
    NS = {'alto': 'http://www.loc.gov/standards/alto/ns-v3#'}

    # Parse ALTO
    tree = etree.parse(alto_path)
    root = tree.getroot()

    # TEI setup
    NS_TEI = "http://www.tei-c.org/ns/1.0"
    tei = etree.Element("{%s}TEI" % NS_TEI, nsmap={None: NS_TEI})
    text = etree.SubElement(tei, "text")
    body = etree.SubElement(text, "body")

    # Iterate over pages
    for page in root.findall(".//alto:Page", namespaces=NS):
        etree.SubElement(body, "pb", n=page.get("PHYSICAL_IMG_NR", ""), facs=page.get("ID", ""))

        # Each text block becomes a <div>
        for block in page.findall(".//alto:TextBlock", namespaces=NS):
            div = etree.SubElement(body, "div")

            # Each line creates a <lb/> and adds text in .tail
            for line in block.findall(".//alto:TextLine", namespaces=NS):
                lb = etree.SubElement(div, "lb")
                words = [s.get("CONTENT", "") for s in line.findall("alto:String", namespaces=NS)]
                lb.tail = " " + " ".join(words) if words else ""
    return tei

def display_tei(tei):
    print(etree.tostring(tei, pretty_print=True, encoding="UTF-8", xml_declaration=True).decode("utf-8"))

def save_tei(tei, tei_path):
    with open(tei_path, "wb") as f:
        f.write(etree.tostring(tei, pretty_print=True, encoding="UTF-8", xml_declaration=True))


if __name__ == "__main__":

    for dir in ["outputs", "outputs/DUFLT_1752_1", "outputs/DUFLT_1752_1/tei"]:
        if not os.path.exists(dir):
            os.mkdir(dir)

    for f in tqdm(os.listdir("data/DUFLT_1752_1/alto")):
        if f.endswith(".xml"):
            alto_path = os.path.join("data", "DUFLT_1752_1", "alto", f)
            tei_path = os.path.join("outputs", "DUFLT_1752_1", "tei", f)

            tei = alto_to_tei(alto_path)
            save_tei(tei, tei_path)