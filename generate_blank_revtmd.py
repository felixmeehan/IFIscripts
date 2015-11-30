import sys
import subprocess
import os



from easygui import multenterbox, choicebox
filenoext = filenoext = os.path.basename(sys.argv[1])

msg ="Which Workflow?"
title = "Workflows"
choices = ["Telecine One Light", "bestlight", "Telecine Grade", "Tape Ingest 1", "Tape Ingest 2", "Tape Edit Suite 1", "Tape Edit Suite 2"]
choice = choicebox(msg, title, choices)
print choice
if choice not in ("Telecine One Light", "bestlight", "Telecine Grade"):
    msg ="Tape Deck?"
    title = "Pick a name yo!"
    choices = ["DVW-500", "MiniDV-Something", "Beta-1800p-something", "J-30", "HDCAM-thing", "Another Beta gizmo", "Unknown"]
    deck = choicebox(msg, title, choices)
else:
    msg ="Telecine Machine"
    title = "Pick a name yo!"
    choices = ["Flashtransfer", "Flashscan",]
    scanner = choicebox(msg, title, choices)
    

msg ="User?"
title = "Pick a name yo!"
choices = ["Kieran O'Leary", "Gavin Martin", "Dean Kavanagh", "Raelene Casey", "Anja Mahler", "Eoin O'Donohoe", "Unknown"]
user = choicebox(msg, title, choices)


    
msg = "Enter your personal information"
title = "blablablabl"
fieldNames = ["Source Accession Number","Notes","Filmographic Reference Number"]
fieldValues = []  # we start with blanks for the values
fieldValues = multenterbox(msg,title, fieldNames)
 
    # make sure that none of the fields was left blank
while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.' % fieldNames[i])
        if errmsg == "": break # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
 
print "Reply was:", fieldValues
    
inmagicxml = sys.argv[1] + '.xml'
updated = inmagicxml + 'updated.xml'
def revtmd_coding_process_history():
    fo.write('<revtmd:codingProcessHistory>\n')
    fo.write('<revtmd:role/>\n')
    fo.write('<revtmd:description/>\n')
    fo.write('<revtmd:manufacturer/>\n')
    fo.write('<revtmd:modelName/>\n')
    fo.write('<revtmd:version/>\n')
    fo.write('<revtmd:serialNumber/>\n')
    fo.write('<revtmd:signal/>\n')
    fo.write('<revtmd:settings/>\n')
    fo.write('<revtmd:videoEncoding/>\n')
    fo.write('</revtmd:codingProcessHistory>\n')

with open(inmagicxml, "w+") as fo:

    fo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fo.write('<revtmd xmlns:revtmd="http://nwtssite.nwts.nara/schema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://nwtssite.nwts.nara/schema/  http://www.archives.gov/preservation/products/reVTMD.xsd">\n')
    fo.write('<revtmd:reVTMD>\n')
    fo.write('<revtmd:object>\n')
    fo.write('<revtmd:filename/>\n')
    fo.write('<revtmd:organization>\n')
    fo.write('<revtmd:organization_main>\n')
    fo.write('<revtmd:name/>\n')
    fo.write('<revtmd:role/>\n')
    fo.write('</revtmd:organization_main>\n')
    fo.write('<revtmd:organization_division>\n')
    fo.write('<revtmd:name/>\n')
    fo.write('</revtmd:organization_division>\n')
    fo.write('</revtmd:organization>\n')
    fo.write('<!-- Use for custodian of the content item -->\n')
    fo.write('<revtmd:organization>\n')
    fo.write('<revtmd:organization_main>\n')
    fo.write('<revtmd:name/>\n')
    fo.write('<revtmd:role/>\n')
    fo.write('<revtmd:role_note/>\n')
    fo.write('</revtmd:organization_main>\n')
    fo.write('</revtmd:organization>\n')
    fo.write('<revtmd:identifier/>\n')
    fo.write('<revtmd:mimetype/>\n')
    fo.write('<revtmd:checksum algorithm="" dateTime=""/>\n')
    fo.write('<!-- Checksum as generated immediately after the digitization process. -->\n')
    fo.write('<revtmd:use/>\n')
    fo.write('<revtmd:captureHistory>\n')
    fo.write('<revtmd:digitizationDate/>\n')
    fo.write('<revtmd:digitizationEngineer/>\n')
    fo.write('<revtmd:preparationActions/>\n')
    fo.write('<revtmd:preparationActions/>\n')
    fo.write('<!-- Here you list the tools used to create the object being described in this record.\n')
    fo.write('For example, if you are creating a record for a low-quality viewing copy, you would describe\n')
    fo.write('all of the tools used to get from the higher quality preservation copy to the viewing copy. -->\n')
    revtmd_coding_process_history()
    revtmd_coding_process_history()
    revtmd_coding_process_history()
    revtmd_coding_process_history()
    revtmd_coding_process_history()
    fo.write('</revtmd:captureHistory>\n')
    fo.write('</revtmd:object>\n')
    fo.write('</revtmd:reVTMD>\n')
    fo.write('</revtmd>\n')
    
    
def add_to_revtmd(element, value, xmlfile):
    subprocess.call(['xml', 'ed', '--inplace', '-N', 'x=http://nwtssite.nwts.nara/schema/', '-u', element, '-v', value, xmlfile])
def ffmpeg_revtmd():
    add_to_revtmd('//revtmd:codingProcessHistory[5]/revtmd:role', 'Transcode', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[5]/revtmd:description', 'Transcode to FFv1 in Matroska wrapper', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[5]/revtmd:manufacturer', 'ffmpeg', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[5]/revtmd:modelName', '2.8.2', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[5]/revtmd:videoEncoding', "FFv1", inmagicxml)
def avid_capture_revtmd():
    add_to_revtmd('//revtmd:codingProcessHistory[2]/revtmd:role', 'Capture', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[2]/revtmd:description', 'SDI bitstream capture', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[2]/revtmd:manufacturer', 'Avid', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[2]/revtmd:modelName', 'Media Composer', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[2]/revtmd:version', '8.3.0', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[2]/revtmd:serialNumber', 'ABC123', inmagicxml)
def avid_export_revtmd():
    add_to_revtmd('//revtmd:codingProcessHistory[4]/revtmd:role', 'Transcode', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[4]/revtmd:description', 'Transcode to v210 in quicktime warpper', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[4]/revtmd:manufacturer', 'Avid', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[4]/revtmd:modelName', 'Media Composer', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[4]/revtmd:version', '8.3.0', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[4]/revtmd:videoEncoding', "v210", inmagicxml)
def avid_consolidate_revtmd():
    add_to_revtmd('//revtmd:codingProcessHistory[3]/revtmd:role', 'Transcode', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[3]/revtmd:description', 'Add plate, consolidate multiple clips', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[3]/revtmd:manufacturer', 'Avid', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[3]/revtmd:modelName', 'Media Composer', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[3]/revtmd:version', '8.3.0', inmagicxml)
  
def bestlight():
        
    add_to_revtmd('//revtmd:filename', filenoext, inmagicxml)
    add_to_revtmd('//revtmd:identifier', fieldValues[0], inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:role', 'Playback', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:description', '16mm Film Digitisation', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:manufacturer', 'MWA', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:modelName', 'Flashtransfer', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:signal', 'SDI', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:serialNumber', 'ABC123', inmagicxml)
    
    avid_capture_revtmd()
    add_to_revtmd('//revtmd:digitizationEngineer[1]', user, inmagicxml)
    avid_consolidate_revtmd()
    avid_export_revtmd()
    ffmpeg_revtmd()
def ingest1():
        
    add_to_revtmd('//revtmd:filename', filenoext, inmagicxml)
    add_to_revtmd('//revtmd:identifier', fieldValues[0], inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:role', 'Playback', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:description', '16mm Film Digitisation', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:manufacturer', 'MWA', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:modelName', 'Flashtransfer', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:signal', 'SDI', inmagicxml)
    add_to_revtmd('//revtmd:codingProcessHistory[1]/revtmd:serialNumber', 'ABC123', inmagicxml)
    add_to_revtmd('//revtmd:digitizationEngineer[1]', user, inmagicxml)

    avid_export_revtmd()
    ffmpeg_revtmd()
  
if choice == "bestlight":
    bestlight()
elif choice =="Tape Ingest 1":
    ingest1()
