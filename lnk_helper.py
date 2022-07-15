# https://stackoverflow.com/questions/397125/reading-the-target-of-a-lnk-file-in-python/28952464#28952464
# https://gist.github.com/Winand/997ed38269e899eb561991a0c663fa49
from struct import unpack
from locale import getdefaultlocale

# TODO:
#   Add support for targets with HasArguments flag, e.g. GOG Galaxy Games
#   example: "C:\Program Files (x86)\GOG Galaxy\GalaxyClient.exe" /command=runGame /gameId=1207659583 /path="G:\Modern Games\GOG Games\Megabyte Punch"
#   Ref: https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-SHLLINK/%5bMS-SHLLINK%5d-210407.pdf


def get_target(path):
    with open(path, 'rb') as stream:
        content = stream.read()
        # skip first 20 bytes (HeaderSize and LinkCLSID)
        # read the LinkFlags structure (4 bytes)
        lflags = unpack('I', content[0x14:0x18])[0]
        position = 0x18
        # if the HasLinkTargetIDList bit is set then skip the stored IDList
        # structure and header
        if (lflags & 0x01) == 1:
            position = unpack('H', content[0x4C:0x4E])[0] + 0x4E
        last_pos = position
        position += 0x04
        # get how long the file information is (LinkInfoSize)
        length = unpack('I', content[last_pos:position])[0]
        # skip 12 bytes (LinkInfoHeaderSize, LinkInfoFlags and VolumeIDOffset)
        position += 0x0C
        # go to the LocalBasePath position
        lbpos = unpack('I', content[position:position+0x04])[0]
        position = last_pos + lbpos
        # read the string at the given position of the determined length
        size = (length + last_pos) - position - 0x02
        content = content[position:position+size].split(b'\x00', 1)
        return content[-1].decode('utf-16' if len(content) > 1
                                  else getdefaultlocale()[1])
