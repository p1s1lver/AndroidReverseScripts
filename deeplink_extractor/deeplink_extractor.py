import uuid
import re
import xml.etree.ElementTree as ET
from gooey import Gooey, GooeyParser


def check_intent_filter(intent_filter):
    return (
        "android.intent.action.VIEW" in ET.tostring(intent_filter).decode()
        and "android.intent.category.DEFAULT" in ET.tostring(intent_filter).decode()
        and "android.intent.category.BROWSABLE" in ET.tostring(intent_filter).decode()
    )


@Gooey(program_name="APK to XML Converter", program_description="Converts APK files to XML files")
def main():
    parser = GooeyParser(description="Process some integers.")
    parser.add_argument("AndroidManifestXmlFileLocation", metavar="path", type=str, help="path to androidManifest.xml file")
    args = parser.parse_args()

    tree = ET.parse(args.AndroidManifestXmlFileLocation)
    root = tree.getroot()

    for activity in root.findall(".//activity"):

        activity_name = str(uuid.uuid4())
        for attr in activity.attrib:
            if re.search(r'.*name.*', attr):
                print(attr)
                activity_name = str(activity.attrib[attr])

        for intent_filter in activity.findall(".//intent-filter"):
            if check_intent_filter(intent_filter):
                print("Found deeplink: " + str(activity))
                filename = activity_name + ".xml"
                with open(filename, "w") as f:
                    f.write(ET.tostring(activity).decode())
                continue  # 找到了就对下一个进行判断


if __name__ == "__main__":
    main()
