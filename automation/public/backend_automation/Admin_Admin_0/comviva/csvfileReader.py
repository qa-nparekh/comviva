import xml.etree.ElementTree as Xet
import time
import pandas as pd

cols = ["Event Time Stamp", "Result Value", "Sender From", "Sender SCCPAddress", "Recipient Code", "TextBody"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('data/sample.xml')
root = xmlparse.getroot()

for i in root:

    eventTimestamp = i.attrib.get("eventTimestamp")
    result = i.find("result").attrib.get("value")
    senderFrom = i.find("sender").attrib.get("from")
    sccpAddress = i.find("sender").attrib.get("sccpAddress")
    code = i.find("recipients").find("recipient").attrib.get("code")
    textBody = i.find("payload").find("message").find("textBody").text

    rows.append({"Event Time Stamp": eventTimestamp,
                 "Result Value": result,
                 "Sender From": senderFrom,
                 "Sender SCCPAddress": sccpAddress,
                 "Recipient Code": code,
                 "TextBody": textBody
                 })

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
timestamp = time.strftime("%Y%m%d-%H%M%S")

print(timestamp)

df.to_csv('Output-'+timestamp+'.csv')
