"""Provide RGB color constants and a colors dictionary with
elements formatted: colors[colorname] = CONSTANT"""

from collections import namedtuple, OrderedDict

Color = namedtuple('RGB','red, green, blue')
colors = {} #dict of colors

class RGB(Color):
    @property
    def hexstr(self):
        '''Returns color in hex format'''
        return '#{:02X}{:02X}{:02X}'.format(self.red*255,self.green*255,self.blue*255)

#Color contants
ALICEBLUE = RGB(0.941, 0.973, 1.000)
ANTIQUEWHITE = RGB(0.980, 0.922, 0.843)
ANTIQUEWHITE1 = RGB(1.000, 0.937, 0.859)
ANTIQUEWHITE2 = RGB(0.933, 0.875, 0.800)
ANTIQUEWHITE3 = RGB(0.804, 0.753, 0.690)
ANTIQUEWHITE4 = RGB(0.545, 0.514, 0.471)
AQUA = RGB(0.000, 1.000, 1.000)
AQUAMARINE1 = RGB(0.498, 1.000, 0.831)
AQUAMARINE2 = RGB(0.463, 0.933, 0.776)
AQUAMARINE3 = RGB(0.400, 0.804, 0.667)
AQUAMARINE4 = RGB(0.271, 0.545, 0.455)
AZURE1 = RGB(0.941, 1.000, 1.000)
AZURE2 = RGB(0.878, 0.933, 0.933)
AZURE3 = RGB(0.757, 0.804, 0.804)
AZURE4 = RGB(0.514, 0.545, 0.545)
BANANA = RGB(0.890, 0.812, 0.341)
BEIGE = RGB(0.961, 0.961, 0.863)
BISQUE1 = RGB(1.000, 0.894, 0.769)
BISQUE2 = RGB(0.933, 0.835, 0.718)
BISQUE3 = RGB(0.804, 0.718, 0.620)
BISQUE4 = RGB(0.545, 0.490, 0.420)
BLACK = RGB(0.000, 0.000, 0.000)
BLANCHEDALMOND = RGB(1.000, 0.922, 0.804)
BLUE = RGB(0.000, 0.000, 1.000)
BLUE2 = RGB(0.000, 0.000, 0.933)
BLUE3 = RGB(0.000, 0.000, 0.804)
BLUE4 = RGB(0.000, 0.000, 0.545)
BLUEVIOLET = RGB(0.541, 0.169, 0.886)
BRICK = RGB(0.612, 0.400, 0.122)
BROWN = RGB(0.647, 0.165, 0.165)
BROWN1 = RGB(1.000, 0.251, 0.251)
BROWN2 = RGB(0.933, 0.231, 0.231)
BROWN3 = RGB(0.804, 0.200, 0.200)
BROWN4 = RGB(0.545, 0.137, 0.137)
BURLYWOOD = RGB(0.871, 0.722, 0.529)
BURLYWOOD1 = RGB(1.000, 0.827, 0.608)
BURLYWOOD2 = RGB(0.933, 0.773, 0.569)
BURLYWOOD3 = RGB(0.804, 0.667, 0.490)
BURLYWOOD4 = RGB(0.545, 0.451, 0.333)
BURNTSIENNA = RGB(0.541, 0.212, 0.059)
BURNTUMBER = RGB(0.541, 0.200, 0.141)
CADETBLUE = RGB(0.373, 0.620, 0.627)
CADETBLUE1 = RGB(0.596, 0.961, 1.000)
CADETBLUE2 = RGB(0.557, 0.898, 0.933)
CADETBLUE3 = RGB(0.478, 0.773, 0.804)
CADETBLUE4 = RGB(0.325, 0.525, 0.545)
CADMIUMORANGE = RGB(1.000, 0.380, 0.012)
CADMIUMYELLOW = RGB(1.000, 0.600, 0.071)
CARROT = RGB(0.929, 0.569, 0.129)
CHARTREUSE1 = RGB(0.498, 1.000, 0.000)
CHARTREUSE2 = RGB(0.463, 0.933, 0.000)
CHARTREUSE3 = RGB(0.400, 0.804, 0.000)
CHARTREUSE4 = RGB(0.271, 0.545, 0.000)
CHOCOLATE = RGB(0.824, 0.412, 0.118)
CHOCOLATE1 = RGB(1.000, 0.498, 0.141)
CHOCOLATE2 = RGB(0.933, 0.463, 0.129)
CHOCOLATE3 = RGB(0.804, 0.400, 0.114)
CHOCOLATE4 = RGB(0.545, 0.271, 0.075)
COBALT = RGB(0.239, 0.349, 0.671)
COBALTGREEN = RGB(0.239, 0.569, 0.251)
COLDGREY = RGB(0.502, 0.541, 0.529)
CORAL = RGB(1.000, 0.498, 0.314)
CORAL1 = RGB(1.000, 0.447, 0.337)
CORAL2 = RGB(0.933, 0.416, 0.314)
CORAL3 = RGB(0.804, 0.357, 0.271)
CORAL4 = RGB(0.545, 0.243, 0.184)
CORNFLOWERBLUE = RGB(0.392, 0.584, 0.929)
CORNSILK1 = RGB(1.000, 0.973, 0.863)
CORNSILK2 = RGB(0.933, 0.910, 0.804)
CORNSILK3 = RGB(0.804, 0.784, 0.694)
CORNSILK4 = RGB(0.545, 0.533, 0.471)
CRIMSON = RGB(0.863, 0.078, 0.235)
CYAN2 = RGB(0.000, 0.933, 0.933)
CYAN3 = RGB(0.000, 0.804, 0.804)
CYAN4 = RGB(0.000, 0.545, 0.545)
DARKGOLDENROD = RGB(0.722, 0.525, 0.043)
DARKGOLDENROD1 = RGB(1.000, 0.725, 0.059)
DARKGOLDENROD2 = RGB(0.933, 0.678, 0.055)
DARKGOLDENROD3 = RGB(0.804, 0.584, 0.047)
DARKGOLDENROD4 = RGB(0.545, 0.396, 0.031)
DARKGRAY = RGB(0.663, 0.663, 0.663)
DARKGREEN = RGB(0.000, 0.392, 0.000)
DARKKHAKI = RGB(0.741, 0.718, 0.420)
DARKOLIVEGREEN = RGB(0.333, 0.420, 0.184)
DARKOLIVEGREEN1 = RGB(0.792, 1.000, 0.439)
DARKOLIVEGREEN2 = RGB(0.737, 0.933, 0.408)
DARKOLIVEGREEN3 = RGB(0.635, 0.804, 0.353)
DARKOLIVEGREEN4 = RGB(0.431, 0.545, 0.239)
DARKORANGE = RGB(1.000, 0.549, 0.000)
DARKORANGE1 = RGB(1.000, 0.498, 0.000)
DARKORANGE2 = RGB(0.933, 0.463, 0.000)
DARKORANGE3 = RGB(0.804, 0.400, 0.000)
DARKORANGE4 = RGB(0.545, 0.271, 0.000)
DARKORCHID = RGB(0.600, 0.196, 0.800)
DARKORCHID1 = RGB(0.749, 0.243, 1.000)
DARKORCHID2 = RGB(0.698, 0.227, 0.933)
DARKORCHID3 = RGB(0.604, 0.196, 0.804)
DARKORCHID4 = RGB(0.408, 0.133, 0.545)
DARKSALMON = RGB(0.914, 0.588, 0.478)
DARKSEAGREEN = RGB(0.561, 0.737, 0.561)
DARKSEAGREEN1 = RGB(0.757, 1.000, 0.757)
DARKSEAGREEN2 = RGB(0.706, 0.933, 0.706)
DARKSEAGREEN3 = RGB(0.608, 0.804, 0.608)
DARKSEAGREEN4 = RGB(0.412, 0.545, 0.412)
DARKSLATEBLUE = RGB(0.282, 0.239, 0.545)
DARKSLATEGRAY = RGB(0.184, 0.310, 0.310)
DARKSLATEGRAY1 = RGB(0.592, 1.000, 1.000)
DARKSLATEGRAY2 = RGB(0.553, 0.933, 0.933)
DARKSLATEGRAY3 = RGB(0.475, 0.804, 0.804)
DARKSLATEGRAY4 = RGB(0.322, 0.545, 0.545)
DARKTURQUOISE = RGB(0.000, 0.808, 0.820)
DARKVIOLET = RGB(0.580, 0.000, 0.827)
DEEPPINK1 = RGB(1.000, 0.078, 0.576)
DEEPPINK2 = RGB(0.933, 0.071, 0.537)
DEEPPINK3 = RGB(0.804, 0.063, 0.463)
DEEPPINK4 = RGB(0.545, 0.039, 0.314)
DEEPSKYBLUE1 = RGB(0.000, 0.749, 1.000)
DEEPSKYBLUE2 = RGB(0.000, 0.698, 0.933)
DEEPSKYBLUE3 = RGB(0.000, 0.604, 0.804)
DEEPSKYBLUE4 = RGB(0.000, 0.408, 0.545)
DIMGRAY = RGB(0.412, 0.412, 0.412)
DIMGRAY = RGB(0.412, 0.412, 0.412)
DODGERBLUE1 = RGB(0.118, 0.565, 1.000)
DODGERBLUE2 = RGB(0.110, 0.525, 0.933)
DODGERBLUE3 = RGB(0.094, 0.455, 0.804)
DODGERBLUE4 = RGB(0.063, 0.306, 0.545)
EGGSHELL = RGB(0.988, 0.902, 0.788)
EMERALDGREEN = RGB(0.000, 0.788, 0.341)
FIREBRICK = RGB(0.698, 0.133, 0.133)
FIREBRICK1 = RGB(1.000, 0.188, 0.188)
FIREBRICK2 = RGB(0.933, 0.173, 0.173)
FIREBRICK3 = RGB(0.804, 0.149, 0.149)
FIREBRICK4 = RGB(0.545, 0.102, 0.102)
FLESH = RGB(1.000, 0.490, 0.251)
FLORALWHITE = RGB(1.000, 0.980, 0.941)
FORESTGREEN = RGB(0.133, 0.545, 0.133)
GAINSBORO = RGB(0.863, 0.863, 0.863)
GHOSTWHITE = RGB(0.973, 0.973, 1.000)
GOLD1 = RGB(1.000, 0.843, 0.000)
GOLD2 = RGB(0.933, 0.788, 0.000)
GOLD3 = RGB(0.804, 0.678, 0.000)
GOLD4 = RGB(0.545, 0.459, 0.000)
GOLDENROD = RGB(0.855, 0.647, 0.125)
GOLDENROD1 = RGB(1.000, 0.757, 0.145)
GOLDENROD2 = RGB(0.933, 0.706, 0.133)
GOLDENROD3 = RGB(0.804, 0.608, 0.114)
GOLDENROD4 = RGB(0.545, 0.412, 0.078)
GRAY = RGB(0.502, 0.502, 0.502)
GRAY1 = RGB(0.012, 0.012, 0.012)
GRAY10 = RGB(0.102, 0.102, 0.102)
GRAY11 = RGB(0.110, 0.110, 0.110)
GRAY12 = RGB(0.122, 0.122, 0.122)
GRAY13 = RGB(0.129, 0.129, 0.129)
GRAY14 = RGB(0.141, 0.141, 0.141)
GRAY15 = RGB(0.149, 0.149, 0.149)
GRAY16 = RGB(0.161, 0.161, 0.161)
GRAY17 = RGB(0.169, 0.169, 0.169)
GRAY18 = RGB(0.180, 0.180, 0.180)
GRAY19 = RGB(0.188, 0.188, 0.188)
GRAY2 = RGB(0.020, 0.020, 0.020)
GRAY20 = RGB(0.200, 0.200, 0.200)
GRAY21 = RGB(0.212, 0.212, 0.212)
GRAY22 = RGB(0.220, 0.220, 0.220)
GRAY23 = RGB(0.231, 0.231, 0.231)
GRAY24 = RGB(0.239, 0.239, 0.239)
GRAY25 = RGB(0.251, 0.251, 0.251)
GRAY26 = RGB(0.259, 0.259, 0.259)
GRAY27 = RGB(0.271, 0.271, 0.271)
GRAY28 = RGB(0.278, 0.278, 0.278)
GRAY29 = RGB(0.290, 0.290, 0.290)
GRAY3 = RGB(0.031, 0.031, 0.031)
GRAY30 = RGB(0.302, 0.302, 0.302)
GRAY31 = RGB(0.310, 0.310, 0.310)
GRAY32 = RGB(0.322, 0.322, 0.322)
GRAY33 = RGB(0.329, 0.329, 0.329)
GRAY34 = RGB(0.341, 0.341, 0.341)
GRAY35 = RGB(0.349, 0.349, 0.349)
GRAY36 = RGB(0.361, 0.361, 0.361)
GRAY37 = RGB(0.369, 0.369, 0.369)
GRAY38 = RGB(0.380, 0.380, 0.380)
GRAY39 = RGB(0.388, 0.388, 0.388)
GRAY4 = RGB(0.039, 0.039, 0.039)
GRAY40 = RGB(0.400, 0.400, 0.400)
GRAY42 = RGB(0.420, 0.420, 0.420)
GRAY43 = RGB(0.431, 0.431, 0.431)
GRAY44 = RGB(0.439, 0.439, 0.439)
GRAY45 = RGB(0.451, 0.451, 0.451)
GRAY46 = RGB(0.459, 0.459, 0.459)
GRAY47 = RGB(0.471, 0.471, 0.471)
GRAY48 = RGB(0.478, 0.478, 0.478)
GRAY49 = RGB(0.490, 0.490, 0.490)
GRAY5 = RGB(0.051, 0.051, 0.051)
GRAY50 = RGB(0.498, 0.498, 0.498)
GRAY51 = RGB(0.510, 0.510, 0.510)
GRAY52 = RGB(0.522, 0.522, 0.522)
GRAY53 = RGB(0.529, 0.529, 0.529)
GRAY54 = RGB(0.541, 0.541, 0.541)
GRAY55 = RGB(0.549, 0.549, 0.549)
GRAY56 = RGB(0.561, 0.561, 0.561)
GRAY57 = RGB(0.569, 0.569, 0.569)
GRAY58 = RGB(0.580, 0.580, 0.580)
GRAY59 = RGB(0.588, 0.588, 0.588)
GRAY6 = RGB(0.059, 0.059, 0.059)
GRAY60 = RGB(0.600, 0.600, 0.600)
GRAY61 = RGB(0.612, 0.612, 0.612)
GRAY62 = RGB(0.620, 0.620, 0.620)
GRAY63 = RGB(0.631, 0.631, 0.631)
GRAY64 = RGB(0.639, 0.639, 0.639)
GRAY65 = RGB(0.651, 0.651, 0.651)
GRAY66 = RGB(0.659, 0.659, 0.659)
GRAY67 = RGB(0.671, 0.671, 0.671)
GRAY68 = RGB(0.678, 0.678, 0.678)
GRAY69 = RGB(0.690, 0.690, 0.690)
GRAY7 = RGB(0.071, 0.071, 0.071)
GRAY70 = RGB(0.702, 0.702, 0.702)
GRAY71 = RGB(0.710, 0.710, 0.710)
GRAY72 = RGB(0.722, 0.722, 0.722)
GRAY73 = RGB(0.729, 0.729, 0.729)
GRAY74 = RGB(0.741, 0.741, 0.741)
GRAY75 = RGB(0.749, 0.749, 0.749)
GRAY76 = RGB(0.761, 0.761, 0.761)
GRAY77 = RGB(0.769, 0.769, 0.769)
GRAY78 = RGB(0.780, 0.780, 0.780)
GRAY79 = RGB(0.788, 0.788, 0.788)
GRAY8 = RGB(0.078, 0.078, 0.078)
GRAY80 = RGB(0.800, 0.800, 0.800)
GRAY81 = RGB(0.812, 0.812, 0.812)
GRAY82 = RGB(0.820, 0.820, 0.820)
GRAY83 = RGB(0.831, 0.831, 0.831)
GRAY84 = RGB(0.839, 0.839, 0.839)
GRAY85 = RGB(0.851, 0.851, 0.851)
GRAY86 = RGB(0.859, 0.859, 0.859)
GRAY87 = RGB(0.871, 0.871, 0.871)
GRAY88 = RGB(0.878, 0.878, 0.878)
GRAY89 = RGB(0.890, 0.890, 0.890)
GRAY9 = RGB(0.090, 0.090, 0.090)
GRAY90 = RGB(0.898, 0.898, 0.898)
GRAY91 = RGB(0.910, 0.910, 0.910)
GRAY92 = RGB(0.922, 0.922, 0.922)
GRAY93 = RGB(0.929, 0.929, 0.929)
GRAY94 = RGB(0.941, 0.941, 0.941)
GRAY95 = RGB(0.949, 0.949, 0.949)
GRAY97 = RGB(0.969, 0.969, 0.969)
GRAY98 = RGB(0.980, 0.980, 0.980)
GRAY99 = RGB(0.988, 0.988, 0.988)
GREEN = RGB(0.000, 0.502, 0.000)
GREEN1 = RGB(0.000, 1.000, 0.000)
GREEN2 = RGB(0.000, 0.933, 0.000)
GREEN3 = RGB(0.000, 0.804, 0.000)
GREEN4 = RGB(0.000, 0.545, 0.000)
GREENYELLOW = RGB(0.678, 1.000, 0.184)
HONEYDEW1 = RGB(0.941, 1.000, 0.941)
HONEYDEW2 = RGB(0.878, 0.933, 0.878)
HONEYDEW3 = RGB(0.757, 0.804, 0.757)
HONEYDEW4 = RGB(0.514, 0.545, 0.514)
HOTPINK = RGB(1.000, 0.412, 0.706)
HOTPINK1 = RGB(1.000, 0.431, 0.706)
HOTPINK2 = RGB(0.933, 0.416, 0.655)
HOTPINK3 = RGB(0.804, 0.376, 0.565)
HOTPINK4 = RGB(0.545, 0.227, 0.384)
INDIANRED = RGB(0.690, 0.090, 0.122)
INDIANRED = RGB(0.804, 0.361, 0.361)
INDIANRED1 = RGB(1.000, 0.416, 0.416)
INDIANRED2 = RGB(0.933, 0.388, 0.388)
INDIANRED3 = RGB(0.804, 0.333, 0.333)
INDIANRED4 = RGB(0.545, 0.227, 0.227)
INDIGO = RGB(0.294, 0.000, 0.510)
IVORY1 = RGB(1.000, 1.000, 0.941)
IVORY2 = RGB(0.933, 0.933, 0.878)
IVORY3 = RGB(0.804, 0.804, 0.757)
IVORY4 = RGB(0.545, 0.545, 0.514)
IVORYBLACK = RGB(0.161, 0.141, 0.129)
KHAKI = RGB(0.941, 0.902, 0.549)
KHAKI1 = RGB(1.000, 0.965, 0.561)
KHAKI2 = RGB(0.933, 0.902, 0.522)
KHAKI3 = RGB(0.804, 0.776, 0.451)
KHAKI4 = RGB(0.545, 0.525, 0.306)
LAVENDER = RGB(0.902, 0.902, 0.980)
LAVENDERBLUSH1 = RGB(1.000, 0.941, 0.961)
LAVENDERBLUSH2 = RGB(0.933, 0.878, 0.898)
LAVENDERBLUSH3 = RGB(0.804, 0.757, 0.773)
LAVENDERBLUSH4 = RGB(0.545, 0.514, 0.525)
LAWNGREEN = RGB(0.486, 0.988, 0.000)
LEMONCHIFFON1 = RGB(1.000, 0.980, 0.804)
LEMONCHIFFON2 = RGB(0.933, 0.914, 0.749)
LEMONCHIFFON3 = RGB(0.804, 0.788, 0.647)
LEMONCHIFFON4 = RGB(0.545, 0.537, 0.439)
LIGHTBLUE = RGB(0.678, 0.847, 0.902)
LIGHTBLUE1 = RGB(0.749, 0.937, 1.000)
LIGHTBLUE2 = RGB(0.698, 0.875, 0.933)
LIGHTBLUE3 = RGB(0.604, 0.753, 0.804)
LIGHTBLUE4 = RGB(0.408, 0.514, 0.545)
LIGHTCORAL = RGB(0.941, 0.502, 0.502)
LIGHTCYAN1 = RGB(0.878, 1.000, 1.000)
LIGHTCYAN2 = RGB(0.820, 0.933, 0.933)
LIGHTCYAN3 = RGB(0.706, 0.804, 0.804)
LIGHTCYAN4 = RGB(0.478, 0.545, 0.545)
LIGHTGOLDENROD1 = RGB(1.000, 0.925, 0.545)
LIGHTGOLDENROD2 = RGB(0.933, 0.863, 0.510)
LIGHTGOLDENROD3 = RGB(0.804, 0.745, 0.439)
LIGHTGOLDENROD4 = RGB(0.545, 0.506, 0.298)
LIGHTGOLDENRODYELLOW = RGB(0.980, 0.980, 0.824)
LIGHTGREY = RGB(0.827, 0.827, 0.827)
LIGHTPINK = RGB(1.000, 0.714, 0.757)
LIGHTPINK1 = RGB(1.000, 0.682, 0.725)
LIGHTPINK2 = RGB(0.933, 0.635, 0.678)
LIGHTPINK3 = RGB(0.804, 0.549, 0.584)
LIGHTPINK4 = RGB(0.545, 0.373, 0.396)
LIGHTSALMON1 = RGB(1.000, 0.627, 0.478)
LIGHTSALMON2 = RGB(0.933, 0.584, 0.447)
LIGHTSALMON3 = RGB(0.804, 0.506, 0.384)
LIGHTSALMON4 = RGB(0.545, 0.341, 0.259)
LIGHTSEAGREEN = RGB(0.125, 0.698, 0.667)
LIGHTSKYBLUE = RGB(0.529, 0.808, 0.980)
LIGHTSKYBLUE1 = RGB(0.690, 0.886, 1.000)
LIGHTSKYBLUE2 = RGB(0.643, 0.827, 0.933)
LIGHTSKYBLUE3 = RGB(0.553, 0.714, 0.804)
LIGHTSKYBLUE4 = RGB(0.376, 0.482, 0.545)
LIGHTSLATEBLUE = RGB(0.518, 0.439, 1.000)
LIGHTSLATEGRAY = RGB(0.467, 0.533, 0.600)
LIGHTSTEELBLUE = RGB(0.690, 0.769, 0.871)
LIGHTSTEELBLUE1 = RGB(0.792, 0.882, 1.000)
LIGHTSTEELBLUE2 = RGB(0.737, 0.824, 0.933)
LIGHTSTEELBLUE3 = RGB(0.635, 0.710, 0.804)
LIGHTSTEELBLUE4 = RGB(0.431, 0.482, 0.545)
LIGHTYELLOW1 = RGB(1.000, 1.000, 0.878)
LIGHTYELLOW2 = RGB(0.933, 0.933, 0.820)
LIGHTYELLOW3 = RGB(0.804, 0.804, 0.706)
LIGHTYELLOW4 = RGB(0.545, 0.545, 0.478)
LIMEGREEN = RGB(0.196, 0.804, 0.196)
LINEN = RGB(0.980, 0.941, 0.902)
MAGENTA = RGB(1.000, 0.000, 1.000)
MAGENTA2 = RGB(0.933, 0.000, 0.933)
MAGENTA3 = RGB(0.804, 0.000, 0.804)
MAGENTA4 = RGB(0.545, 0.000, 0.545)
MANGANESEBLUE = RGB(0.012, 0.659, 0.620)
MAROON = RGB(0.502, 0.000, 0.000)
MAROON1 = RGB(1.000, 0.204, 0.702)
MAROON2 = RGB(0.933, 0.188, 0.655)
MAROON3 = RGB(0.804, 0.161, 0.565)
MAROON4 = RGB(0.545, 0.110, 0.384)
MEDIUMORCHID = RGB(0.729, 0.333, 0.827)
MEDIUMORCHID1 = RGB(0.878, 0.400, 1.000)
MEDIUMORCHID2 = RGB(0.820, 0.373, 0.933)
MEDIUMORCHID3 = RGB(0.706, 0.322, 0.804)
MEDIUMORCHID4 = RGB(0.478, 0.216, 0.545)
MEDIUMPURPLE = RGB(0.576, 0.439, 0.859)
MEDIUMPURPLE1 = RGB(0.671, 0.510, 1.000)
MEDIUMPURPLE2 = RGB(0.624, 0.475, 0.933)
MEDIUMPURPLE3 = RGB(0.537, 0.408, 0.804)
MEDIUMPURPLE4 = RGB(0.365, 0.278, 0.545)
MEDIUMSEAGREEN = RGB(0.235, 0.702, 0.443)
MEDIUMSLATEBLUE = RGB(0.482, 0.408, 0.933)
MEDIUMSPRINGGREEN = RGB(0.000, 0.980, 0.604)
MEDIUMTURQUOISE = RGB(0.282, 0.820, 0.800)
MEDIUMVIOLETRED = RGB(0.780, 0.082, 0.522)
MELON = RGB(0.890, 0.659, 0.412)
MIDNIGHTBLUE = RGB(0.098, 0.098, 0.439)
MINT = RGB(0.741, 0.988, 0.788)
MINTCREAM = RGB(0.961, 1.000, 0.980)
MISTYROSE1 = RGB(1.000, 0.894, 0.882)
MISTYROSE2 = RGB(0.933, 0.835, 0.824)
MISTYROSE3 = RGB(0.804, 0.718, 0.710)
MISTYROSE4 = RGB(0.545, 0.490, 0.482)
MOCCASIN = RGB(1.000, 0.894, 0.710)
NAVAJOWHITE1 = RGB(1.000, 0.871, 0.678)
NAVAJOWHITE2 = RGB(0.933, 0.812, 0.631)
NAVAJOWHITE3 = RGB(0.804, 0.702, 0.545)
NAVAJOWHITE4 = RGB(0.545, 0.475, 0.369)
NAVY = RGB(0.000, 0.000, 0.502)
OLDLACE = RGB(0.992, 0.961, 0.902)
OLIVE = RGB(0.502, 0.502, 0.000)
OLIVEDRAB = RGB(0.420, 0.557, 0.137)
OLIVEDRAB1 = RGB(0.753, 1.000, 0.243)
OLIVEDRAB2 = RGB(0.702, 0.933, 0.227)
OLIVEDRAB3 = RGB(0.604, 0.804, 0.196)
OLIVEDRAB4 = RGB(0.412, 0.545, 0.133)
ORANGE = RGB(1.000, 0.502, 0.000)
ORANGE1 = RGB(1.000, 0.647, 0.000)
ORANGE2 = RGB(0.933, 0.604, 0.000)
ORANGE3 = RGB(0.804, 0.522, 0.000)
ORANGE4 = RGB(0.545, 0.353, 0.000)
ORANGERED1 = RGB(1.000, 0.271, 0.000)
ORANGERED2 = RGB(0.933, 0.251, 0.000)
ORANGERED3 = RGB(0.804, 0.216, 0.000)
ORANGERED4 = RGB(0.545, 0.145, 0.000)
ORCHID = RGB(0.855, 0.439, 0.839)
ORCHID1 = RGB(1.000, 0.514, 0.980)
ORCHID2 = RGB(0.933, 0.478, 0.914)
ORCHID3 = RGB(0.804, 0.412, 0.788)
ORCHID4 = RGB(0.545, 0.278, 0.537)
PALEGOLDENROD = RGB(0.933, 0.910, 0.667)
PALEGREEN = RGB(0.596, 0.984, 0.596)
PALEGREEN1 = RGB(0.604, 1.000, 0.604)
PALEGREEN2 = RGB(0.565, 0.933, 0.565)
PALEGREEN3 = RGB(0.486, 0.804, 0.486)
PALEGREEN4 = RGB(0.329, 0.545, 0.329)
PALETURQUOISE1 = RGB(0.733, 1.000, 1.000)
PALETURQUOISE2 = RGB(0.682, 0.933, 0.933)
PALETURQUOISE3 = RGB(0.588, 0.804, 0.804)
PALETURQUOISE4 = RGB(0.400, 0.545, 0.545)
PALEVIOLETRED = RGB(0.859, 0.439, 0.576)
PALEVIOLETRED1 = RGB(1.000, 0.510, 0.671)
PALEVIOLETRED2 = RGB(0.933, 0.475, 0.624)
PALEVIOLETRED3 = RGB(0.804, 0.408, 0.537)
PALEVIOLETRED4 = RGB(0.545, 0.278, 0.365)
PAPAYAWHIP = RGB(1.000, 0.937, 0.835)
PEACHPUFF1 = RGB(1.000, 0.855, 0.725)
PEACHPUFF2 = RGB(0.933, 0.796, 0.678)
PEACHPUFF3 = RGB(0.804, 0.686, 0.584)
PEACHPUFF4 = RGB(0.545, 0.467, 0.396)
PEACOCK = RGB(0.200, 0.631, 0.788)
PINK = RGB(1.000, 0.753, 0.796)
PINK1 = RGB(1.000, 0.710, 0.773)
PINK2 = RGB(0.933, 0.663, 0.722)
PINK3 = RGB(0.804, 0.569, 0.620)
PINK4 = RGB(0.545, 0.388, 0.424)
PLUM = RGB(0.867, 0.627, 0.867)
PLUM1 = RGB(1.000, 0.733, 1.000)
PLUM2 = RGB(0.933, 0.682, 0.933)
PLUM3 = RGB(0.804, 0.588, 0.804)
PLUM4 = RGB(0.545, 0.400, 0.545)
POWDERBLUE = RGB(0.690, 0.878, 0.902)
PURPLE = RGB(0.502, 0.000, 0.502)
PURPLE1 = RGB(0.608, 0.188, 1.000)
PURPLE2 = RGB(0.569, 0.173, 0.933)
PURPLE3 = RGB(0.490, 0.149, 0.804)
PURPLE4 = RGB(0.333, 0.102, 0.545)
RASPBERRY = RGB(0.529, 0.149, 0.341)
RAWSIENNA = RGB(0.780, 0.380, 0.078)
RED1 = RGB(1.000, 0.000, 0.000)
RED2 = RGB(0.933, 0.000, 0.000)
RED3 = RGB(0.804, 0.000, 0.000)
RED4 = RGB(0.545, 0.000, 0.000)
ROSYBROWN = RGB(0.737, 0.561, 0.561)
ROSYBROWN1 = RGB(1.000, 0.757, 0.757)
ROSYBROWN2 = RGB(0.933, 0.706, 0.706)
ROSYBROWN3 = RGB(0.804, 0.608, 0.608)
ROSYBROWN4 = RGB(0.545, 0.412, 0.412)
ROYALBLUE = RGB(0.255, 0.412, 0.882)
ROYALBLUE1 = RGB(0.282, 0.463, 1.000)
ROYALBLUE2 = RGB(0.263, 0.431, 0.933)
ROYALBLUE3 = RGB(0.227, 0.373, 0.804)
ROYALBLUE4 = RGB(0.153, 0.251, 0.545)
SALMON = RGB(0.980, 0.502, 0.447)
SALMON1 = RGB(1.000, 0.549, 0.412)
SALMON2 = RGB(0.933, 0.510, 0.384)
SALMON3 = RGB(0.804, 0.439, 0.329)
SALMON4 = RGB(0.545, 0.298, 0.224)
SANDYBROWN = RGB(0.957, 0.643, 0.376)
SAPGREEN = RGB(0.188, 0.502, 0.078)
SEAGREEN1 = RGB(0.329, 1.000, 0.624)
SEAGREEN2 = RGB(0.306, 0.933, 0.580)
SEAGREEN3 = RGB(0.263, 0.804, 0.502)
SEAGREEN4 = RGB(0.180, 0.545, 0.341)
SEASHELL1 = RGB(1.000, 0.961, 0.933)
SEASHELL2 = RGB(0.933, 0.898, 0.871)
SEASHELL3 = RGB(0.804, 0.773, 0.749)
SEASHELL4 = RGB(0.545, 0.525, 0.510)
SEPIA = RGB(0.369, 0.149, 0.071)
SGIBEET = RGB(0.557, 0.220, 0.557)
SGIBRIGHTGRAY = RGB(0.773, 0.757, 0.667)
SGICHARTREUSE = RGB(0.443, 0.776, 0.443)
SGIDARKGRAY = RGB(0.333, 0.333, 0.333)
SGIGRAY12 = RGB(0.118, 0.118, 0.118)
SGIGRAY16 = RGB(0.157, 0.157, 0.157)
SGIGRAY32 = RGB(0.318, 0.318, 0.318)
SGIGRAY36 = RGB(0.357, 0.357, 0.357)
SGIGRAY52 = RGB(0.518, 0.518, 0.518)
SGIGRAY56 = RGB(0.557, 0.557, 0.557)
SGIGRAY72 = RGB(0.718, 0.718, 0.718)
SGIGRAY76 = RGB(0.757, 0.757, 0.757)
SGIGRAY92 = RGB(0.918, 0.918, 0.918)
SGIGRAY96 = RGB(0.957, 0.957, 0.957)
SGILIGHTBLUE = RGB(0.490, 0.620, 0.753)
SGILIGHTGRAY = RGB(0.667, 0.667, 0.667)
SGIOLIVEDRAB = RGB(0.557, 0.557, 0.220)
SGISALMON = RGB(0.776, 0.443, 0.443)
SGISLATEBLUE = RGB(0.443, 0.443, 0.776)
SGITEAL = RGB(0.220, 0.557, 0.557)
SIENNA = RGB(0.627, 0.322, 0.176)
SIENNA1 = RGB(1.000, 0.510, 0.278)
SIENNA2 = RGB(0.933, 0.475, 0.259)
SIENNA3 = RGB(0.804, 0.408, 0.224)
SIENNA4 = RGB(0.545, 0.278, 0.149)
SILVER = RGB(0.753, 0.753, 0.753)
SKYBLUE = RGB(0.529, 0.808, 0.922)
SKYBLUE1 = RGB(0.529, 0.808, 1.000)
SKYBLUE2 = RGB(0.494, 0.753, 0.933)
SKYBLUE3 = RGB(0.424, 0.651, 0.804)
SKYBLUE4 = RGB(0.290, 0.439, 0.545)
SLATEBLUE = RGB(0.416, 0.353, 0.804)
SLATEBLUE1 = RGB(0.514, 0.435, 1.000)
SLATEBLUE2 = RGB(0.478, 0.404, 0.933)
SLATEBLUE3 = RGB(0.412, 0.349, 0.804)
SLATEBLUE4 = RGB(0.278, 0.235, 0.545)
SLATEGRAY = RGB(0.439, 0.502, 0.565)
SLATEGRAY1 = RGB(0.776, 0.886, 1.000)
SLATEGRAY2 = RGB(0.725, 0.827, 0.933)
SLATEGRAY3 = RGB(0.624, 0.714, 0.804)
SLATEGRAY4 = RGB(0.424, 0.482, 0.545)
SNOW1 = RGB(1.000, 0.980, 0.980)
SNOW2 = RGB(0.933, 0.914, 0.914)
SNOW3 = RGB(0.804, 0.788, 0.788)
SNOW4 = RGB(0.545, 0.537, 0.537)
SPRINGGREEN = RGB(0.000, 1.000, 0.498)
SPRINGGREEN1 = RGB(0.000, 0.933, 0.463)
SPRINGGREEN2 = RGB(0.000, 0.804, 0.400)
SPRINGGREEN3 = RGB(0.000, 0.545, 0.271)
STEELBLUE = RGB(0.275, 0.510, 0.706)
STEELBLUE1 = RGB(0.388, 0.722, 1.000)
STEELBLUE2 = RGB(0.361, 0.675, 0.933)
STEELBLUE3 = RGB(0.310, 0.580, 0.804)
STEELBLUE4 = RGB(0.212, 0.392, 0.545)
TAN = RGB(0.824, 0.706, 0.549)
TAN1 = RGB(1.000, 0.647, 0.310)
TAN2 = RGB(0.933, 0.604, 0.286)
TAN3 = RGB(0.804, 0.522, 0.247)
TAN4 = RGB(0.545, 0.353, 0.169)
TEAL = RGB(0.000, 0.502, 0.502)
THISTLE = RGB(0.847, 0.749, 0.847)
THISTLE1 = RGB(1.000, 0.882, 1.000)
THISTLE2 = RGB(0.933, 0.824, 0.933)
THISTLE3 = RGB(0.804, 0.710, 0.804)
THISTLE4 = RGB(0.545, 0.482, 0.545)
TOMATO1 = RGB(1.000, 0.388, 0.278)
TOMATO2 = RGB(0.933, 0.361, 0.259)
TOMATO3 = RGB(0.804, 0.310, 0.224)
TOMATO4 = RGB(0.545, 0.212, 0.149)
TURQUOISE = RGB(0.251, 0.878, 0.816)
TURQUOISE1 = RGB(0.000, 0.961, 1.000)
TURQUOISE2 = RGB(0.000, 0.898, 0.933)
TURQUOISE3 = RGB(0.000, 0.773, 0.804)
TURQUOISE4 = RGB(0.000, 0.525, 0.545)
TURQUOISEBLUE = RGB(0.000, 0.780, 0.549)
VIOLET = RGB(0.933, 0.510, 0.933)
VIOLETRED = RGB(0.816, 0.125, 0.565)
VIOLETRED1 = RGB(1.000, 0.243, 0.588)
VIOLETRED2 = RGB(0.933, 0.227, 0.549)
VIOLETRED3 = RGB(0.804, 0.196, 0.471)
VIOLETRED4 = RGB(0.545, 0.133, 0.322)
WARMGREY = RGB(0.502, 0.502, 0.412)
WHEAT = RGB(0.961, 0.871, 0.702)
WHEAT1 = RGB(1.000, 0.906, 0.729)
WHEAT2 = RGB(0.933, 0.847, 0.682)
WHEAT3 = RGB(0.804, 0.729, 0.588)
WHEAT4 = RGB(0.545, 0.494, 0.400)
WHITE = RGB(1.000, 1.000, 1.000)
WHITESMOKE = RGB(0.961, 0.961, 0.961)
WHITESMOKE = RGB(0.961, 0.961, 0.961)
YELLOW1 = RGB(1.000, 1.000, 0.000)
YELLOW2 = RGB(0.933, 0.933, 0.000)
YELLOW3 = RGB(0.804, 0.804, 0.000)
YELLOW4 = RGB(0.545, 0.545, 0.000)

#Add colors to colors dictionary
colors['aliceblue'] = ALICEBLUE
colors['antiquewhite'] = ANTIQUEWHITE
colors['antiquewhite1'] = ANTIQUEWHITE1
colors['antiquewhite2'] = ANTIQUEWHITE2
colors['antiquewhite3'] = ANTIQUEWHITE3
colors['antiquewhite4'] = ANTIQUEWHITE4
colors['aqua'] = AQUA
colors['aquamarine1'] = AQUAMARINE1
colors['aquamarine2'] = AQUAMARINE2
colors['aquamarine3'] = AQUAMARINE3
colors['aquamarine4'] = AQUAMARINE4
colors['azure1'] = AZURE1
colors['azure2'] = AZURE2
colors['azure3'] = AZURE3
colors['azure4'] = AZURE4
colors['banana'] = BANANA
colors['beige'] = BEIGE
colors['bisque1'] = BISQUE1
colors['bisque2'] = BISQUE2
colors['bisque3'] = BISQUE3
colors['bisque4'] = BISQUE4
colors['black'] = BLACK
colors['blanchedalmond'] = BLANCHEDALMOND
colors['blue'] = BLUE
colors['blue2'] = BLUE2
colors['blue3'] = BLUE3
colors['blue4'] = BLUE4
colors['blueviolet'] = BLUEVIOLET
colors['brick'] = BRICK
colors['brown'] = BROWN
colors['brown1'] = BROWN1
colors['brown2'] = BROWN2
colors['brown3'] = BROWN3
colors['brown4'] = BROWN4
colors['burlywood'] = BURLYWOOD
colors['burlywood1'] = BURLYWOOD1
colors['burlywood2'] = BURLYWOOD2
colors['burlywood3'] = BURLYWOOD3
colors['burlywood4'] = BURLYWOOD4
colors['burntsienna'] = BURNTSIENNA
colors['burntumber'] = BURNTUMBER
colors['cadetblue'] = CADETBLUE
colors['cadetblue1'] = CADETBLUE1
colors['cadetblue2'] = CADETBLUE2
colors['cadetblue3'] = CADETBLUE3
colors['cadetblue4'] = CADETBLUE4
colors['cadmiumorange'] = CADMIUMORANGE
colors['cadmiumyellow'] = CADMIUMYELLOW
colors['carrot'] = CARROT
colors['chartreuse1'] = CHARTREUSE1
colors['chartreuse2'] = CHARTREUSE2
colors['chartreuse3'] = CHARTREUSE3
colors['chartreuse4'] = CHARTREUSE4
colors['chocolate'] = CHOCOLATE
colors['chocolate1'] = CHOCOLATE1
colors['chocolate2'] = CHOCOLATE2
colors['chocolate3'] = CHOCOLATE3
colors['chocolate4'] = CHOCOLATE4
colors['cobalt'] = COBALT
colors['cobaltgreen'] = COBALTGREEN
colors['coldgrey'] = COLDGREY
colors['coral'] = CORAL
colors['coral1'] = CORAL1
colors['coral2'] = CORAL2
colors['coral3'] = CORAL3
colors['coral4'] = CORAL4
colors['cornflowerblue'] = CORNFLOWERBLUE
colors['cornsilk1'] = CORNSILK1
colors['cornsilk2'] = CORNSILK2
colors['cornsilk3'] = CORNSILK3
colors['cornsilk4'] = CORNSILK4
colors['crimson'] = CRIMSON
colors['cyan2'] = CYAN2
colors['cyan3'] = CYAN3
colors['cyan4'] = CYAN4
colors['darkgoldenrod'] = DARKGOLDENROD
colors['darkgoldenrod1'] = DARKGOLDENROD1
colors['darkgoldenrod2'] = DARKGOLDENROD2
colors['darkgoldenrod3'] = DARKGOLDENROD3
colors['darkgoldenrod4'] = DARKGOLDENROD4
colors['darkgray'] = DARKGRAY
colors['darkgreen'] = DARKGREEN
colors['darkkhaki'] = DARKKHAKI
colors['darkolivegreen'] = DARKOLIVEGREEN
colors['darkolivegreen1'] = DARKOLIVEGREEN1
colors['darkolivegreen2'] = DARKOLIVEGREEN2
colors['darkolivegreen3'] = DARKOLIVEGREEN3
colors['darkolivegreen4'] = DARKOLIVEGREEN4
colors['darkorange'] = DARKORANGE
colors['darkorange1'] = DARKORANGE1
colors['darkorange2'] = DARKORANGE2
colors['darkorange3'] = DARKORANGE3
colors['darkorange4'] = DARKORANGE4
colors['darkorchid'] = DARKORCHID
colors['darkorchid1'] = DARKORCHID1
colors['darkorchid2'] = DARKORCHID2
colors['darkorchid3'] = DARKORCHID3
colors['darkorchid4'] = DARKORCHID4
colors['darksalmon'] = DARKSALMON
colors['darkseagreen'] = DARKSEAGREEN
colors['darkseagreen1'] = DARKSEAGREEN1
colors['darkseagreen2'] = DARKSEAGREEN2
colors['darkseagreen3'] = DARKSEAGREEN3
colors['darkseagreen4'] = DARKSEAGREEN4
colors['darkslateblue'] = DARKSLATEBLUE
colors['darkslategray'] = DARKSLATEGRAY
colors['darkslategray1'] = DARKSLATEGRAY1
colors['darkslategray2'] = DARKSLATEGRAY2
colors['darkslategray3'] = DARKSLATEGRAY3
colors['darkslategray4'] = DARKSLATEGRAY4
colors['darkturquoise'] = DARKTURQUOISE
colors['darkviolet'] = DARKVIOLET
colors['deeppink1'] = DEEPPINK1
colors['deeppink2'] = DEEPPINK2
colors['deeppink3'] = DEEPPINK3
colors['deeppink4'] = DEEPPINK4
colors['deepskyblue1'] = DEEPSKYBLUE1
colors['deepskyblue2'] = DEEPSKYBLUE2
colors['deepskyblue3'] = DEEPSKYBLUE3
colors['deepskyblue4'] = DEEPSKYBLUE4
colors['dimgray'] = DIMGRAY
colors['dimgray'] = DIMGRAY
colors['dodgerblue1'] = DODGERBLUE1
colors['dodgerblue2'] = DODGERBLUE2
colors['dodgerblue3'] = DODGERBLUE3
colors['dodgerblue4'] = DODGERBLUE4
colors['eggshell'] = EGGSHELL
colors['emeraldgreen'] = EMERALDGREEN
colors['firebrick'] = FIREBRICK
colors['firebrick1'] = FIREBRICK1
colors['firebrick2'] = FIREBRICK2
colors['firebrick3'] = FIREBRICK3
colors['firebrick4'] = FIREBRICK4
colors['flesh'] = FLESH
colors['floralwhite'] = FLORALWHITE
colors['forestgreen'] = FORESTGREEN
colors['gainsboro'] = GAINSBORO
colors['ghostwhite'] = GHOSTWHITE
colors['gold1'] = GOLD1
colors['gold2'] = GOLD2
colors['gold3'] = GOLD3
colors['gold4'] = GOLD4
colors['goldenrod'] = GOLDENROD
colors['goldenrod1'] = GOLDENROD1
colors['goldenrod2'] = GOLDENROD2
colors['goldenrod3'] = GOLDENROD3
colors['goldenrod4'] = GOLDENROD4
colors['gray'] = GRAY
colors['gray1'] = GRAY1
colors['gray10'] = GRAY10
colors['gray11'] = GRAY11
colors['gray12'] = GRAY12
colors['gray13'] = GRAY13
colors['gray14'] = GRAY14
colors['gray15'] = GRAY15
colors['gray16'] = GRAY16
colors['gray17'] = GRAY17
colors['gray18'] = GRAY18
colors['gray19'] = GRAY19
colors['gray2'] = GRAY2
colors['gray20'] = GRAY20
colors['gray21'] = GRAY21
colors['gray22'] = GRAY22
colors['gray23'] = GRAY23
colors['gray24'] = GRAY24
colors['gray25'] = GRAY25
colors['gray26'] = GRAY26
colors['gray27'] = GRAY27
colors['gray28'] = GRAY28
colors['gray29'] = GRAY29
colors['gray3'] = GRAY3
colors['gray30'] = GRAY30
colors['gray31'] = GRAY31
colors['gray32'] = GRAY32
colors['gray33'] = GRAY33
colors['gray34'] = GRAY34
colors['gray35'] = GRAY35
colors['gray36'] = GRAY36
colors['gray37'] = GRAY37
colors['gray38'] = GRAY38
colors['gray39'] = GRAY39
colors['gray4'] = GRAY4
colors['gray40'] = GRAY40
colors['gray42'] = GRAY42
colors['gray43'] = GRAY43
colors['gray44'] = GRAY44
colors['gray45'] = GRAY45
colors['gray46'] = GRAY46
colors['gray47'] = GRAY47
colors['gray48'] = GRAY48
colors['gray49'] = GRAY49
colors['gray5'] = GRAY5
colors['gray50'] = GRAY50
colors['gray51'] = GRAY51
colors['gray52'] = GRAY52
colors['gray53'] = GRAY53
colors['gray54'] = GRAY54
colors['gray55'] = GRAY55
colors['gray56'] = GRAY56
colors['gray57'] = GRAY57
colors['gray58'] = GRAY58
colors['gray59'] = GRAY59
colors['gray6'] = GRAY6
colors['gray60'] = GRAY60
colors['gray61'] = GRAY61
colors['gray62'] = GRAY62
colors['gray63'] = GRAY63
colors['gray64'] = GRAY64
colors['gray65'] = GRAY65
colors['gray66'] = GRAY66
colors['gray67'] = GRAY67
colors['gray68'] = GRAY68
colors['gray69'] = GRAY69
colors['gray7'] = GRAY7
colors['gray70'] = GRAY70
colors['gray71'] = GRAY71
colors['gray72'] = GRAY72
colors['gray73'] = GRAY73
colors['gray74'] = GRAY74
colors['gray75'] = GRAY75
colors['gray76'] = GRAY76
colors['gray77'] = GRAY77
colors['gray78'] = GRAY78
colors['gray79'] = GRAY79
colors['gray8'] = GRAY8
colors['gray80'] = GRAY80
colors['gray81'] = GRAY81
colors['gray82'] = GRAY82
colors['gray83'] = GRAY83
colors['gray84'] = GRAY84
colors['gray85'] = GRAY85
colors['gray86'] = GRAY86
colors['gray87'] = GRAY87
colors['gray88'] = GRAY88
colors['gray89'] = GRAY89
colors['gray9'] = GRAY9
colors['gray90'] = GRAY90
colors['gray91'] = GRAY91
colors['gray92'] = GRAY92
colors['gray93'] = GRAY93
colors['gray94'] = GRAY94
colors['gray95'] = GRAY95
colors['gray97'] = GRAY97
colors['gray98'] = GRAY98
colors['gray99'] = GRAY99
colors['green'] = GREEN
colors['green1'] = GREEN1
colors['green2'] = GREEN2
colors['green3'] = GREEN3
colors['green4'] = GREEN4
colors['greenyellow'] = GREENYELLOW
colors['honeydew1'] = HONEYDEW1
colors['honeydew2'] = HONEYDEW2
colors['honeydew3'] = HONEYDEW3
colors['honeydew4'] = HONEYDEW4
colors['hotpink'] = HOTPINK
colors['hotpink1'] = HOTPINK1
colors['hotpink2'] = HOTPINK2
colors['hotpink3'] = HOTPINK3
colors['hotpink4'] = HOTPINK4
colors['indianred'] = INDIANRED
colors['indianred'] = INDIANRED
colors['indianred1'] = INDIANRED1
colors['indianred2'] = INDIANRED2
colors['indianred3'] = INDIANRED3
colors['indianred4'] = INDIANRED4
colors['indigo'] = INDIGO
colors['ivory1'] = IVORY1
colors['ivory2'] = IVORY2
colors['ivory3'] = IVORY3
colors['ivory4'] = IVORY4
colors['ivoryblack'] = IVORYBLACK
colors['khaki'] = KHAKI
colors['khaki1'] = KHAKI1
colors['khaki2'] = KHAKI2
colors['khaki3'] = KHAKI3
colors['khaki4'] = KHAKI4
colors['lavender'] = LAVENDER
colors['lavenderblush1'] = LAVENDERBLUSH1
colors['lavenderblush2'] = LAVENDERBLUSH2
colors['lavenderblush3'] = LAVENDERBLUSH3
colors['lavenderblush4'] = LAVENDERBLUSH4
colors['lawngreen'] = LAWNGREEN
colors['lemonchiffon1'] = LEMONCHIFFON1
colors['lemonchiffon2'] = LEMONCHIFFON2
colors['lemonchiffon3'] = LEMONCHIFFON3
colors['lemonchiffon4'] = LEMONCHIFFON4
colors['lightblue'] = LIGHTBLUE
colors['lightblue1'] = LIGHTBLUE1
colors['lightblue2'] = LIGHTBLUE2
colors['lightblue3'] = LIGHTBLUE3
colors['lightblue4'] = LIGHTBLUE4
colors['lightcoral'] = LIGHTCORAL
colors['lightcyan1'] = LIGHTCYAN1
colors['lightcyan2'] = LIGHTCYAN2
colors['lightcyan3'] = LIGHTCYAN3
colors['lightcyan4'] = LIGHTCYAN4
colors['lightgoldenrod1'] = LIGHTGOLDENROD1
colors['lightgoldenrod2'] = LIGHTGOLDENROD2
colors['lightgoldenrod3'] = LIGHTGOLDENROD3
colors['lightgoldenrod4'] = LIGHTGOLDENROD4
colors['lightgoldenrodyellow'] = LIGHTGOLDENRODYELLOW
colors['lightgrey'] = LIGHTGREY
colors['lightpink'] = LIGHTPINK
colors['lightpink1'] = LIGHTPINK1
colors['lightpink2'] = LIGHTPINK2
colors['lightpink3'] = LIGHTPINK3
colors['lightpink4'] = LIGHTPINK4
colors['lightsalmon1'] = LIGHTSALMON1
colors['lightsalmon2'] = LIGHTSALMON2
colors['lightsalmon3'] = LIGHTSALMON3
colors['lightsalmon4'] = LIGHTSALMON4
colors['lightseagreen'] = LIGHTSEAGREEN
colors['lightskyblue'] = LIGHTSKYBLUE
colors['lightskyblue1'] = LIGHTSKYBLUE1
colors['lightskyblue2'] = LIGHTSKYBLUE2
colors['lightskyblue3'] = LIGHTSKYBLUE3
colors['lightskyblue4'] = LIGHTSKYBLUE4
colors['lightslateblue'] = LIGHTSLATEBLUE
colors['lightslategray'] = LIGHTSLATEGRAY
colors['lightsteelblue'] = LIGHTSTEELBLUE
colors['lightsteelblue1'] = LIGHTSTEELBLUE1
colors['lightsteelblue2'] = LIGHTSTEELBLUE2
colors['lightsteelblue3'] = LIGHTSTEELBLUE3
colors['lightsteelblue4'] = LIGHTSTEELBLUE4
colors['lightyellow1'] = LIGHTYELLOW1
colors['lightyellow2'] = LIGHTYELLOW2
colors['lightyellow3'] = LIGHTYELLOW3
colors['lightyellow4'] = LIGHTYELLOW4
colors['limegreen'] = LIMEGREEN
colors['linen'] = LINEN
colors['magenta'] = MAGENTA
colors['magenta2'] = MAGENTA2
colors['magenta3'] = MAGENTA3
colors['magenta4'] = MAGENTA4
colors['manganeseblue'] = MANGANESEBLUE
colors['maroon'] = MAROON
colors['maroon1'] = MAROON1
colors['maroon2'] = MAROON2
colors['maroon3'] = MAROON3
colors['maroon4'] = MAROON4
colors['mediumorchid'] = MEDIUMORCHID
colors['mediumorchid1'] = MEDIUMORCHID1
colors['mediumorchid2'] = MEDIUMORCHID2
colors['mediumorchid3'] = MEDIUMORCHID3
colors['mediumorchid4'] = MEDIUMORCHID4
colors['mediumpurple'] = MEDIUMPURPLE
colors['mediumpurple1'] = MEDIUMPURPLE1
colors['mediumpurple2'] = MEDIUMPURPLE2
colors['mediumpurple3'] = MEDIUMPURPLE3
colors['mediumpurple4'] = MEDIUMPURPLE4
colors['mediumseagreen'] = MEDIUMSEAGREEN
colors['mediumslateblue'] = MEDIUMSLATEBLUE
colors['mediumspringgreen'] = MEDIUMSPRINGGREEN
colors['mediumturquoise'] = MEDIUMTURQUOISE
colors['mediumvioletred'] = MEDIUMVIOLETRED
colors['melon'] = MELON
colors['midnightblue'] = MIDNIGHTBLUE
colors['mint'] = MINT
colors['mintcream'] = MINTCREAM
colors['mistyrose1'] = MISTYROSE1
colors['mistyrose2'] = MISTYROSE2
colors['mistyrose3'] = MISTYROSE3
colors['mistyrose4'] = MISTYROSE4
colors['moccasin'] = MOCCASIN
colors['navajowhite1'] = NAVAJOWHITE1
colors['navajowhite2'] = NAVAJOWHITE2
colors['navajowhite3'] = NAVAJOWHITE3
colors['navajowhite4'] = NAVAJOWHITE4
colors['navy'] = NAVY
colors['oldlace'] = OLDLACE
colors['olive'] = OLIVE
colors['olivedrab'] = OLIVEDRAB
colors['olivedrab1'] = OLIVEDRAB1
colors['olivedrab2'] = OLIVEDRAB2
colors['olivedrab3'] = OLIVEDRAB3
colors['olivedrab4'] = OLIVEDRAB4
colors['orange'] = ORANGE
colors['orange1'] = ORANGE1
colors['orange2'] = ORANGE2
colors['orange3'] = ORANGE3
colors['orange4'] = ORANGE4
colors['orangered1'] = ORANGERED1
colors['orangered2'] = ORANGERED2
colors['orangered3'] = ORANGERED3
colors['orangered4'] = ORANGERED4
colors['orchid'] = ORCHID
colors['orchid1'] = ORCHID1
colors['orchid2'] = ORCHID2
colors['orchid3'] = ORCHID3
colors['orchid4'] = ORCHID4
colors['palegoldenrod'] = PALEGOLDENROD
colors['palegreen'] = PALEGREEN
colors['palegreen1'] = PALEGREEN1
colors['palegreen2'] = PALEGREEN2
colors['palegreen3'] = PALEGREEN3
colors['palegreen4'] = PALEGREEN4
colors['paleturquoise1'] = PALETURQUOISE1
colors['paleturquoise2'] = PALETURQUOISE2
colors['paleturquoise3'] = PALETURQUOISE3
colors['paleturquoise4'] = PALETURQUOISE4
colors['palevioletred'] = PALEVIOLETRED
colors['palevioletred1'] = PALEVIOLETRED1
colors['palevioletred2'] = PALEVIOLETRED2
colors['palevioletred3'] = PALEVIOLETRED3
colors['palevioletred4'] = PALEVIOLETRED4
colors['papayawhip'] = PAPAYAWHIP
colors['peachpuff1'] = PEACHPUFF1
colors['peachpuff2'] = PEACHPUFF2
colors['peachpuff3'] = PEACHPUFF3
colors['peachpuff4'] = PEACHPUFF4
colors['peacock'] = PEACOCK
colors['pink'] = PINK
colors['pink1'] = PINK1
colors['pink2'] = PINK2
colors['pink3'] = PINK3
colors['pink4'] = PINK4
colors['plum'] = PLUM
colors['plum1'] = PLUM1
colors['plum2'] = PLUM2
colors['plum3'] = PLUM3
colors['plum4'] = PLUM4
colors['powderblue'] = POWDERBLUE
colors['purple'] = PURPLE
colors['purple1'] = PURPLE1
colors['purple2'] = PURPLE2
colors['purple3'] = PURPLE3
colors['purple4'] = PURPLE4
colors['raspberry'] = RASPBERRY
colors['rawsienna'] = RAWSIENNA
colors['red1'] = RED1
colors['red2'] = RED2
colors['red3'] = RED3
colors['red4'] = RED4
colors['rosybrown'] = ROSYBROWN
colors['rosybrown1'] = ROSYBROWN1
colors['rosybrown2'] = ROSYBROWN2
colors['rosybrown3'] = ROSYBROWN3
colors['rosybrown4'] = ROSYBROWN4
colors['royalblue'] = ROYALBLUE
colors['royalblue1'] = ROYALBLUE1
colors['royalblue2'] = ROYALBLUE2
colors['royalblue3'] = ROYALBLUE3
colors['royalblue4'] = ROYALBLUE4
colors['salmon'] = SALMON
colors['salmon1'] = SALMON1
colors['salmon2'] = SALMON2
colors['salmon3'] = SALMON3
colors['salmon4'] = SALMON4
colors['sandybrown'] = SANDYBROWN
colors['sapgreen'] = SAPGREEN
colors['seagreen1'] = SEAGREEN1
colors['seagreen2'] = SEAGREEN2
colors['seagreen3'] = SEAGREEN3
colors['seagreen4'] = SEAGREEN4
colors['seashell1'] = SEASHELL1
colors['seashell2'] = SEASHELL2
colors['seashell3'] = SEASHELL3
colors['seashell4'] = SEASHELL4
colors['sepia'] = SEPIA
colors['sgibeet'] = SGIBEET
colors['sgibrightgray'] = SGIBRIGHTGRAY
colors['sgichartreuse'] = SGICHARTREUSE
colors['sgidarkgray'] = SGIDARKGRAY
colors['sgigray12'] = SGIGRAY12
colors['sgigray16'] = SGIGRAY16
colors['sgigray32'] = SGIGRAY32
colors['sgigray36'] = SGIGRAY36
colors['sgigray52'] = SGIGRAY52
colors['sgigray56'] = SGIGRAY56
colors['sgigray72'] = SGIGRAY72
colors['sgigray76'] = SGIGRAY76
colors['sgigray92'] = SGIGRAY92
colors['sgigray96'] = SGIGRAY96
colors['sgilightblue'] = SGILIGHTBLUE
colors['sgilightgray'] = SGILIGHTGRAY
colors['sgiolivedrab'] = SGIOLIVEDRAB
colors['sgisalmon'] = SGISALMON
colors['sgislateblue'] = SGISLATEBLUE
colors['sgiteal'] = SGITEAL
colors['sienna'] = SIENNA
colors['sienna1'] = SIENNA1
colors['sienna2'] = SIENNA2
colors['sienna3'] = SIENNA3
colors['sienna4'] = SIENNA4
colors['silver'] = SILVER
colors['skyblue'] = SKYBLUE
colors['skyblue1'] = SKYBLUE1
colors['skyblue2'] = SKYBLUE2
colors['skyblue3'] = SKYBLUE3
colors['skyblue4'] = SKYBLUE4
colors['slateblue'] = SLATEBLUE
colors['slateblue1'] = SLATEBLUE1
colors['slateblue2'] = SLATEBLUE2
colors['slateblue3'] = SLATEBLUE3
colors['slateblue4'] = SLATEBLUE4
colors['slategray'] = SLATEGRAY
colors['slategray1'] = SLATEGRAY1
colors['slategray2'] = SLATEGRAY2
colors['slategray3'] = SLATEGRAY3
colors['slategray4'] = SLATEGRAY4
colors['snow1'] = SNOW1
colors['snow2'] = SNOW2
colors['snow3'] = SNOW3
colors['snow4'] = SNOW4
colors['springgreen'] = SPRINGGREEN
colors['springgreen1'] = SPRINGGREEN1
colors['springgreen2'] = SPRINGGREEN2
colors['springgreen3'] = SPRINGGREEN3
colors['steelblue'] = STEELBLUE
colors['steelblue1'] = STEELBLUE1
colors['steelblue2'] = STEELBLUE2
colors['steelblue3'] = STEELBLUE3
colors['steelblue4'] = STEELBLUE4
colors['tan'] = TAN
colors['tan1'] = TAN1
colors['tan2'] = TAN2
colors['tan3'] = TAN3
colors['tan4'] = TAN4
colors['teal'] = TEAL
colors['thistle'] = THISTLE
colors['thistle1'] = THISTLE1
colors['thistle2'] = THISTLE2
colors['thistle3'] = THISTLE3
colors['thistle4'] = THISTLE4
colors['tomato1'] = TOMATO1
colors['tomato2'] = TOMATO2
colors['tomato3'] = TOMATO3
colors['tomato4'] = TOMATO4
colors['turquoise'] = TURQUOISE
colors['turquoise1'] = TURQUOISE1
colors['turquoise2'] = TURQUOISE2
colors['turquoise3'] = TURQUOISE3
colors['turquoise4'] = TURQUOISE4
colors['turquoiseblue'] = TURQUOISEBLUE
colors['violet'] = VIOLET
colors['violetred'] = VIOLETRED
colors['violetred1'] = VIOLETRED1
colors['violetred2'] = VIOLETRED2
colors['violetred3'] = VIOLETRED3
colors['violetred4'] = VIOLETRED4
colors['warmgrey'] = WARMGREY
colors['wheat'] = WHEAT
colors['wheat1'] = WHEAT1
colors['wheat2'] = WHEAT2
colors['wheat3'] = WHEAT3
colors['wheat4'] = WHEAT4
colors['white'] = WHITE
colors['whitesmoke'] = WHITESMOKE
colors['whitesmoke'] = WHITESMOKE
colors['yellow1'] = YELLOW1
colors['yellow2'] = YELLOW2
colors['yellow3'] = YELLOW3
colors['yellow4'] = YELLOW4

colors = OrderedDict(sorted(colors.items(), key=lambda t: t[0]))
