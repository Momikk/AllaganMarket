import json
import re
import struct
import hashlib
from pathlib import Path

config = json.loads((Path.home() / 'AppData/Roaming/XIVLauncherCN/launcherConfigV3.json').read_text(encoding='utf-8-sig'))
exe = Path(config['GamePath']) / 'game/ffxiv_dx11.exe'
data = exe.read_bytes()
print('executable SHA256', hashlib.sha256(data).hexdigest())
print('game version', (exe.parent / 'ffxivgame.ver').read_text().strip())
pe = struct.unpack_from('<I', data, 0x3c)[0]
sections = struct.unpack_from('<H', data, pe + 6)[0]
optional_size = struct.unpack_from('<H', data, pe + 20)[0]
section_start = pe + 24 + optional_size
for i in range(sections):
    offset = section_start + i * 40
    if data[offset:offset+8].rstrip(b'\0') == b'.text':
        size, rva, rawsize, raw = struct.unpack_from('<IIII', data, offset + 8)
        text = data[raw:raw+rawsize]
        break

patterns = {
    'pre_7_55': '48 89 74 24 ?? 57 48 81 EC ?? ?? ?? ?? 44 0F B7 42 ??',
    'upstream_7_55': 'E8 ?? ?? ?? ?? E9 ?? ?? ?? ?? 48 8B D7 41 8B CE E8 ?? ?? ?? ?? E9 ?? ?? ?? ?? 48 8B D7 41 8B CE E8 ?? ?? ?? ?? E9 ?? ?? ?? ?? 48 8B D7 41 8B CE E8 ?? ?? ?? ?? E9 ?? ?? ?? ?? 48 8D 57 10',
}
for name, sig in patterns.items():
    regex = b''.join(b'.' if part == '??' else re.escape(bytes.fromhex(part)) for part in sig.split())
    matches = list(re.finditer(regex, text, re.DOTALL))
    print(name, len(matches))
    for match in matches[:5]:
        position = match.start()
        print(hex(rva + position), text[position:position+96].hex(' '))
        if text[position] == 0xe8:
            target = position + 5 + struct.unpack_from('<i', text, position+1)[0]
            print('call target', hex(rva + target), text[target:target+96].hex(' '))

source = (Path(__file__).resolve().parents[1] / 'AllaganMarket/Services/InventoryService.cs').read_text(encoding='utf-8-sig')
active_sig = re.search(r'\[Signature\(\s*"([0-9A-F? ]+)"', source).group(1)
active_regex = b''.join(b'.' if part == '??' else re.escape(bytes.fromhex(part)) for part in active_sig.split())
active_matches = list(re.finditer(active_regex, text, re.DOTALL))
assert len(active_matches) == 1, f'Published inventory signature must be unique: {len(active_matches)}'
print('published signature uniquely matches', hex(rva + active_matches[0].start()))

try:
    import capstone
    print('capstone available')
except ImportError:
    print('capstone unavailable')
