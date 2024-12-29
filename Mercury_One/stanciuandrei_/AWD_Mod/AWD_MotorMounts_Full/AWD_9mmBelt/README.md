# Full AWD Double shear Mod 9mm for Mercury1.1 -- !! In testing !!

# The mods are in testing, the parts may or may not fit right. I am not responsible for any damage this may cause.

<img src="IMAGES/AWD_Assembly_Front.png">

# BOM:
Some parts will not be mentioned because they come with the mercury kit.
| Type | Quantity | Link |
| --- | --- | --- |
| Shoulder skrews 50mm long 5mm shaft with M3 thread ([check picture](IMAGES/Shoulder_skrews.png) ) | 16 | [Aliexpress](https://www.aliexpress.com/item/1005004802215831.html) |
| M5 1mm shims (you have them) | 26 |  |
| F695-2RS bearings (4 are in the tensioners) | 12 | [Fushi](https://www.aliexpress.com/item/32850989216.html) |
| 695-2RS bearings | 18 | [Fushi](https://vi.aliexpress.com/item/1005003141257945.html) |
| M5x35 dowel pins | 6 | [Nindejin](https://vi.aliexpress.com/item/1005002308655979.html)  |
| M5x20 screws (2 from the tensioners) | 4 | [Nindejin](https://vi.aliexpress.com/item/4000142028043.html) |
| M5x60 screws | 4 | [Nindejin](https://vi.aliexpress.com/item/4000142028043.html) |
| M5x10 screws | 2 | [Nindejin](https://vi.aliexpress.com/item/4000142028043.html) |
| M5x15 screws | 4 | [Nindejin](https://vi.aliexpress.com/item/4000142028043.html) |
| M5 T-nut | 2 | [Aliexpress](https://vi.aliexpress.com/item/32706208829.html) |
| M5 Heatset insert M5 X D7.0 X L9.0 | 2 | [Aliexpress](https://vi.aliexpress.com/item/4000232990523.html)  |
| M3x35 screws | 6 | [Nindejin](https://vi.aliexpress.com/item/4000142028043.html) |
| M3 heat set inserts (from the tensioners) | 2 |  |
| 14mm tall gt2 20 tooth pulley | 4 | [Mellow](https://vi.aliexpress.com/item/33023133633.html) |
| gt2 9mm belts | 6 Meters | [TriangleLab](https://www.aliexpress.com/item/1005006507781085.html) |
| GT2 20 tooth motor pulley for 9mm (or 10mm) belt and 5mm shaft | 4 | [Mellow](https://vi.aliexpress.com/item/33023279793.html) |
| Motors with minimum 46mm shaft | 4 | [Aliexpress](https://vi.aliexpress.com/item/1005007500807396.html) [Fabreeko](https://www.fabreeko.com/products/ldo-42sth48-2504ahs55-nema-17-motor-high-temp?_pos=3&_psq=mot&_ss=e&_v=1.0)|
| stepper drivers available to drive the extra motors | 2 |  |

Aproximate BOM visualised (I have 2 wong bolts in the picture and 4 extra shims)
<img src="IMAGES/BOM.jpg">

# Belt paths
**:warning:! You must flip the xjoints bearing stacks and pulleys upside down !:warning:**

## Bottom belt path

<img src="IMAGES/BottomBeltPath.png">

## Top belt path

<img src="IMAGES/TopBeltPath.png">

# How to sync motors

[VZbot Motor sync](https://www.youtube.com/watch?v=so9oqJyirKY)

# Printer config

-The X and Y motors are now swithed and rotating backwards because of the new belt path so the pins must be swithed 

-The front motors will be defined as stepper_x1 and stepper_y1 the step and dir pins will need to have the same sign in front ( both x and x1 sould have DIR and STEP pin with ! or without, same for y and y1)

-Lower the homing speed to 10 and the motor amps to 0.4 or as low as you cand get them to move so that you have time to stop the printer if it goes the wrong direction and minimize the damage if the endstop pins are wrong.

My config as an example:
```
[stepper_x]
step_pin: PC14
dir_pin: !PC13
enable_pin: !PE6
microsteps: 16
rotation_distance: 40
endstop_pin: ^EBBCan:PB6
position_endstop: 386
position_max: 386
homing_speed: 150

[tmc5160 stepper_x]
cs_pin: PD6
spi_software_sclk_pin: PC6
spi_software_mosi_pin: PC8
spi_software_miso_pin: PC7
#diag1_pin: PC15
run_current: 1.400
sense_resistor: 0.022
#stealthchop_threshold: 999999



[stepper_x1]
step_pin: PE2
dir_pin: !PE1
enable_pin: !PE0
microsteps: 16
rotation_distance: 40

[tmc5160 stepper_x1] 
cs_pin: PD4
spi_software_sclk_pin: PC6
spi_software_mosi_pin: PC8
spi_software_miso_pin: PC7
#diag1_pin: PF1
run_current: 1.400
sense_resistor: 0.022
#stealthchop_threshold: 999999


[stepper_y]
step_pin: PE5
dir_pin: !PE4
enable_pin: !PE3
microsteps: 16
rotation_distance: 40
endstop_pin: PC0
position_endstop: 370
position_max: 370
position_min: 0
homing_speed: 150

[tmc5160 stepper_y]
cs_pin: PD5
spi_software_sclk_pin: PC6
spi_software_mosi_pin: PC8
spi_software_miso_pin: PC7
#diag1_pin: PF0
run_current: 1.400
sense_resistor: 0.022
#stealthchop_threshold: 999999


[stepper_y1]
step_pin: PB9
dir_pin: !PB8
enable_pin: !PB7
microsteps: 16
rotation_distance: 40

[tmc5160 stepper_y1] 
cs_pin: PD3
spi_software_sclk_pin: PC6
spi_software_mosi_pin: PC8
spi_software_miso_pin: PC7
#diag1_pin: PF2
run_current: 1.400
sense_resistor: 0.022
#stealthchop_threshold: 999999
```
