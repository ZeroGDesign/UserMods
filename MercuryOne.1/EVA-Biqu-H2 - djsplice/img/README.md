# EVA mount for the Biqu H2 hot end / extruder

These were designed to work with the [Mercury One](https://github.com/ZeroGDesign/Mercury) conversion for an Ender 5. Rudra has made an [EVA universal faceplate](https://drive.google.com/drive/folders/1WeMnU41LHNeeJy4bnJhXC6Zqy8RPeaLE) based on the EVA v2 spec that works with the Mercury One belt paths.

This is a mount that connects the Biqu H2 hot end and extruder to the EVA Mercury faceplate, with fan duct to match.

The fan duct is loosely based on the official [EVA](https://main.eva-3d.page/) fan ducts. 'Loosely' in the fact that I'm a CAD n00b, and the official designs have much more thought/testing put into them compared to my functional yet hacky rendtion! ;)

## Images
![Face Plate](/img/EVA-Biqu-H2-Faceplate.png)
![Fan Duct](/img/EVA-Biqu-H2-Fan_Duct.png)

## Installation
* Download and print [EVA universal faceplate](https://drive.google.com/drive/folders/1WeMnU41LHNeeJy4bnJhXC6Zqy8RPeaLE), the Eva Biqu H2 mount, and the Fan duct.

![Print orientation H2 Mount](/img/EVA-H2_mount.jpg)

* Attach the H2 faceplate to the EVA carriage using 3 M3 screws
![EVA - Merc mount](/img/EVA-Merc-Mount.jpg)

* Attach the fan duct to the EVA carriage

* Attach the H2 to the faceplate via 2 screws on top of the H2, and one screw in the back.

![Merc - H2 Faceplate mounted](/img/EVA-H2_mount-installed.jpg)
![Merc - H2 rear bolt](/img/EVA-Merc-H2-install-rear-bolt.jpeg)

![Installed](/img/EVA-H2_installed.jpg)


## Known Issues
1. I optimized the design to make it fairly easy to remove the H2 from the EVA carriage while providing good rigidity using 3 point connections (3 screws between the faceplate and the carriage, and 3 screws connecting the H2 to the faceplate). In initial iterations of this design, I'd tried connecting the H2 to the faceplate using only two screws, but vibrations at higher print speeds had negative effects on quality.

2. Because of the challenges with bolt clearances between the H2 mounts and the faceplate, the extruder is ever so slightly off center from the carriage. It's about 2mm off of center from the carriage which slightly interferes with the fan duct.

3. I had to design a new fan duct because existing mods didn't quite fit correctly for me. The current nozzle design sits pretty close to the build plate, 1mm clearance. Because of the H2 / carriage offset, the right side air duct seems to be a bit impeded. While there's more optimization to be had here, the fan duct works pretty well for general purpose prints.

4. I'm a CAD n000b - I make things that work for me, and by sharing them I hope other find utility in them as well!
