# AWD Mercury1.1 mod
<img src="AWD_render.PNG">


# BOM:
| Type | Quantity | Link |
| --- | --- | --- |
| Shoulder skrews 40mm long 5mm shaft with M3 thread | 8 | [Aliexpress](https://www.aliexpress.com/item/1005004802215831.html) |
| M5 1mm shims (6 you can extract from the tensioners) | 18 | [Nindejin](https://www.aliexpress.com/item/4000174460068.html?aff_fcid=e7d51ebaaac74b4dafd074d5c6d607a1-1728682878095-03455-_A9rXO4&tt=CPS_NORMAL&aff_fsk=_A9rXO4&aff_platform=shareComponent-detail&sk=_A9rXO4&aff_trace_key=e7d51ebaaac74b4dafd074d5c6d607a1-1728682878095-03455-_A9rXO4&terminal_id=3db8dc71742443ffb34ffa7b2e123b97&afSmartRedirect=y) |
| F695-2RS bearings(4 are in the tensioners) | 12 | [Kit of 10 Aliexpress](https://www.aliexpress.com/item/32850989216.html) |
| 5x30 shafts (the ones from the tensioners) | 2 |  |
| M5x20 screws(from the tensioners) | 2 |  |
| M3 heat set inserts (from the tensioners) | 2 |  |
| 8.5mm gt2 20 tooth pulley | 2 | [Mellow](https://www.aliexpress.com/item/1005004374407134.html?spm=a2g0o.order_list.order_list_main.24.21ef1802NFrx61) |
| gt2 6mm belts(I use gates gates 6mm 2gt-rf belt) | 6 Meters | [TriangleLab](https://www.aliexpress.com/item/1005006507781085.html?spm=a2g0o.detail.pcDetailTopMoreOtherSeller.1.1ebaId4bId4bJ2&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=8cab5cd5-2cb5-4df6-88f0-f8fb543ab826&_t=gps-id:pcDetailTopMoreOtherSeller,scm-url:1007.40050.354490.0,pvid:8cab5cd5-2cb5-4df6-88f0-f8fb543ab826,tpp_buckets:668%232846%238111%231996&pdp_npi=4%40dis%21RON%2139.32%2139.32%21%21%218.45%218.45%21%40211b698e17286817196807058e861e%2112000037754698142%21rec%21RO%21921752181%21X&utparam-url=scene%3ApcDetailTopMoreOtherSeller%7Cquery_from%3A) |
| GT2 20 tooth motor pulley for 6mm belt 5mm shaft | 2 | [Mellow](https://www.aliexpress.com/item/33002989677.html?spm=a2g0o.store_pc_home.0.0.4c6c3378bdigwy&pdp_npi=4%40dis%21RON%21RON%2029.03%21RON%204.61%21%21%216.24%210.99%21%40%2167022731524%21sh%21%21%21) |
| motors like the one you use in the back to match | 2 | [Biqu](https://biqu.equipment/products/ldo-42sth48-2504ac-reva-motor-driver?variant=39991585636450) |
| stepper drivers available to drive the extra motors | 2 |  |

Aproximate BOM visualised (I have 2 wong bolts in the picture and 4 extra shims)
<img src="BOM.jpg">

# Belt paths
**:warning:! You must flip the xjoints bearing stacks and pulleys upside down !:warning:**

## Bottom belt path

<img src="Pictures/BottomBeltPath.png">

## Top belt path

<img src="Pictures/TopBeltPath.png">

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
