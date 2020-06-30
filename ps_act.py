
import colormaps
import numpy as np
import struct

max_v = (2<<8 - 1)
def as_8_bit(value):
    return np.uint8(max_v * value)
  

def output_lut(filename, color_array):
  f = open(filename, "wb")
  if len(color_array) != 256:
    print("Please pad color array to 256 entries.  Did not write", filename)
    return
  print("Writing: ", filename)
  i = 0
  for c in color_array:
    for value in c:
      v = as_8_bit(value)
      if i == 255:
        print(v, end=", ")
      f.write(v)
    i += 1
  print("")
  
      
      
output_lut("magma.act", colormaps.magma.colors)
output_lut("inferno.act", colormaps.inferno.colors)
output_lut("plasma.act", colormaps.plasma.colors)
output_lut("viridis.act", colormaps.viridis.colors)

# Example of reading an ACT file and printing the values.
def read_act():
  f = open("webcolormap.ACT", "rb")
  for i in range(255):
    # Unpack "B" is format string for "unsigned byte"
    # This discussion: https://groups.google.com/forum/#!topic/adobe.photoshop.windows/YaGUbvKH_Xo
    # seems to say I should need 16 bit values instead of 8, but I could not replicate that.  /shrug
    # If you do find a 16 bit ACT file, you'd probably need to read two bytes instead of 1 and "H" format string.
    print(i, " r: ", struct.unpack("B", f.read(1)), end=", ")
    print("g: ", struct.unpack("B", f.read(1)), end=", ")
    print("b: ", struct.unpack("B", f.read(1)))
    
    
