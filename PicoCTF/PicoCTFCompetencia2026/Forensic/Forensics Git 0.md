
## Descripcion

Can you find the flag in this disk image?
Download the disk image https://challenge-files.picoctf.net/c_plain_mesa/96db2eea3d6d3e215d3dc2289457a1bc10b17b1de69c46996a171f4f689db74b/disk.img.gz

## Solucion

descargamos el archivo:

giselle_maz-picoctf@webshell:~$ wget -q https://challenge-files.picoctf.net/c_plain_mesa/96db2eea3d6d3e215d3dc2289457a1bc10b17b1de69c46996a171f4f689db74b/disk.img.gz

realizamos un filtrado sin descomprimir y dentro de todo lo que arroja esta la flag en dos partes:

```
giselle_maz-picoctf@webshell:~$ zcat disk.img.gz | strings | grep "picoCTF{"
The picoCTF flag format is 'picoCTF{}' where there is some leetspeak phrase in between the curly braces
giselle_maz-picoctf@webshell:~$ zcat disk.img.gz | mmls /dev/stdin
Sector offset supplied is larger than disk image (maximum: 0)
giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ zcat disk.img.gz | strings -n 8 | grep -C 5 "pico"
ffffffff81b81ec0 t pirq_esc_set
ffffffff81b81f30 t __pfx_pirq_serverworks_get
ffffffff81b81f40 t pirq_serverworks_get
ffffffff81b81f70 t __pfx_pirq_serverworks_set
ffffffff81b81f80 t pirq_serverworks_set
ffffffff81b81fb0 t __pfx_pirq_pico_get
ffffffff81b81fc0 t pirq_pico_get
ffffffff81b82000 t __pfx_pirq_pico_set
ffffffff81b82010 t pirq_pico_set
ffffffff81b82050 t __pfx_pirq_get_dev_info
ffffffff81b82060 t pirq_get_dev_info
ffffffff81b82120 t __pfx_pirq_amd756_get
ffffffff81b82130 t pirq_amd756_get
ffffffff81b821f0 t __pfx_pirq_sis503_get

ffffffff82b13a00 t ite_router_probe
ffffffff82b13a90 t __pfx_ali_router_probe
ffffffff82b13aa0 t ali_router_probe
ffffffff82b13ba0 t __pfx_amd_router_probe
ffffffff82b13bb0 t amd_router_probe
ffffffff82b13ca0 t __pfx_pico_router_probe
ffffffff82b13cb0 t pico_router_probe
ffffffff82b13d80 t __pfx_fix_acer_tm360_irqrouting
ffffffff82b13d90 t fix_acer_tm360_irqrouting
ffffffff82b13e20 t __pfx_fix_broken_hp_bios_irq9
ffffffff82b13e30 t fix_broken_hp_bios_irq9
ffffffff82b13ec0 t __pfx_pirq_peer_trick

.apk.e9902f19aeb9f60b13e5982eb8729ffedbfe65ea0a2302e4
.apk.b8b3d375d18afec4b491137576e507a7a06e7afc44c63e6da8b
hid-elan.ko.gz
hid-logitech-dj.ko.gz
hid-megaworld.ko.gz
hid-picolcd.ko.gz
hid-prodikeys.ko.gz
hid-roccat-isku.ko.gz
hid-roccat-ryos.ko.gz
hid-roccat-arvo.ko.gz
hid-roccat-common.ko.gz

Z:Q1VDRnqk+eobjPN+sr4SHSsf4ToEI=
R:hid-ortek.ko.gz
Z:Q1EDox0pu2f1D5/239g2APSWn5lNY=
R:hid-penmount.ko.gz
Z:Q1sIJd3FlguBWzFYDNkV9xfqygSNg=
R:hid-picolcd.ko.gz
Z:Q1AQ3AnWixcJZKTXPe0T/gOChuWCo=
R:hid-plantronics.ko.gz
Z:Q1bLgw+eMIlZPoITf1MAHZeWfaezk=
R:hid-playstation.ko.gz
Z:Q1Z3hp4heaMdbza5ifBcqdrzneIpA=

Z:Q1VDRnqk+eobjPN+sr4SHSsf4ToEI=
R:hid-ortek.ko.gz
Z:Q1EDox0pu2f1D5/239g2APSWn5lNY=
R:hid-penmount.ko.gz
Z:Q1sIJd3FlguBWzFYDNkV9xfqygSNg=
R:hid-picolcd.ko.gz
Z:Q1AQ3AnWixcJZKTXPe0T/gOChuWCo=
R:hid-plantronics.ko.gz
Z:Q1bLgw+eMIlZPoITf1MAHZeWfaezk=
R:hid-playstation.ko.gz
Z:Q1Z3hp4heaMdbza5ifBcqdrzneIpA=

kernel/drivers/hid/hid-multitouch.ko
kernel/drivers/hid/hid-nintendo.ko
kernel/drivers/hid/hid-ortek.ko
kernel/drivers/hid/hid-prodikeys.ko
kernel/drivers/hid/hid-penmount.ko
kernel/drivers/hid/hid-picolcd.ko
kernel/drivers/hid/hid-plantronics.ko
kernel/drivers/hid/hid-playstation.ko
kernel/drivers/hid/hid-primax.ko
kernel/drivers/hid/hid-pxrc.ko
kernel/drivers/hid/hid-razer.ko

hid-logitech.ko.gz
hid-microsoft.ko.gz
hid-elan.ko.gz
hid-logitech-dj.ko.gz
hid-megaworld.ko.gz
hid-picolcd.ko.gz
hid-prodikeys.ko.gz
hid-roccat-isku.ko.gz
hid-roccat-ryos.ko.gz
hid-roccat-lua.ko.gz
hid-cougar.ko.gz

kernel/drivers/hid/hid-multitouch.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-nintendo.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-ortek.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-prodikeys.ko.gz: kernel/sound/core/snd-rawmidi.ko.gz kernel/sound/core/snd-seq-device.ko.gz kernel/drivers/hid/usbhid/usbhid.ko.gz kernel/drivers/hid/hid.ko.gz kernel/sound/core/snd.ko.gz kernel/sound/soundcore.ko.gz kernel/drivers/usb/core/usbcore.ko.gz kernel/drivers/usb/common/usb-common.ko.gz
kernel/drivers/hid/hid-penmount.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-picolcd.ko.gz: kernel/drivers/hid/hid.ko.gz kernel/drivers/media/rc/rc-core.ko.gz kernel/drivers/video/backlight/lcd.ko.gz
kernel/drivers/hid/hid-plantronics.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-playstation.ko.gz: kernel/drivers/leds/led-class-multicolor.ko.gz kernel/drivers/hid/hid.ko.gz kernel/drivers/input/ff-memless.ko.gz
kernel/drivers/hid/hid-primax.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-pxrc.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-razer.ko.gz: kernel/drivers/hid/hid.ko.gz

kernel/drivers/hid/hid-multitouch.ko.gz: kernel/drivers/hid/hid.ko.gz
dintendo
kernel/drivers/hid/hid-nintendo.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-ortek.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-penmount.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-picolcd.ko.gz: kernel/drivers/hid/hid.ko.gz kernel/drivers/media/rc/rc-core.ko.gz kernel/drivers/video/backlight/lcd.ko.gz
kernel/drivers/hid/hid-plantronics.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-playstation.ko.gz: kernel/drivers/leds/led-class-multicolor.ko.gz kernel/drivers/hid/hid.ko.gz kernel/drivers/input/ff-memless.ko.gz
kernel/drivers/hid/hid-primax.ko.gz: kernel/drivers/hid/hid.ko.gz
kernel/drivers/hid/hid-prodikeys.ko.gz: kernel/sound/core/snd-rawmidi.ko.gz kernel/sound/core/snd-seq-device.ko.gz kernel/drivers/hid/usbhid/usbhid.ko.gz kernel/drivers/hid/hid.ko.gz kernel/sound/core/snd.ko.gz kernel/sound/soundcore.ko.gz kernel/drivers/usb/core/usbcore.ko.gz kernel/drivers/usb/common/usb-common.ko.gz
kernel/drivers/hid/hid-pxrc.ko.gz: kernel/drivers/hid/hid.ko.gz

Lines that start with '#' are comments.

For a project mostly in C, the following would be a good set of

exclude patterns (uncomment them if you want to use them):

.[oa]

ref: refs/heads/master
The picoCTF flag format is 'picoCTF{}' where there is some leetspeak phrase in between the curly braces
+)JMU06c040031Q
Wrap this phrase in the flag format: g17_1n_7h3_d15k_041217d8
327681bb38cf467cec328eec9707b240e3e74ced
0000000000000000000000000000000000000000 327681bb38cf467cec328eec9707b240e3e74ced ctf-player [ctf-player@example.com](mailto:ctf-player@example.com) 1763542167 +0000 commit (initial): Wrap this phrase in the flag format: g17_1n_7h3_d15k_041217d8
0000000000000000000000000000000000000000 327681bb38cf467cec328eec9707b240e3e74ced ctf-player [ctf-player@example.com](mailto:ctf-player@example.com) 1763542167 +0000 commit (initial): Wrap this phrase in the flag format: g17_1n_7h3_d15k_041217d8

hid_lenovo
hid_lenovo
hid_lenovo
hid_lenovo
3p0000310
hid_picolcd
hid_picolcd
^Q8p0000
^dp00001125
hid_asus
hid_elan
hid_elan

alias hid:b0003g*v000005A4p00008003 hid_ortek
alias hid:b0003g*v000005A4p00002000 hid_ortek
alias hid:b0003g*v000005A4p00001700 hid_ortek
alias hid:b0003g*v0000041Ep00002801 hid_prodikeys
alias hid:b0003g*v000014E1p00006000 hid_penmount
alias hid:b0003g*v000004D8p0000F002 hid_picolcd
alias hid:b0003g*v000004D8p0000C002 hid_picolcd
alias hid:b0003g*v0000047Fp* hid_plantronics
alias hid:b0003g*v0000054Cp00000DF2 hid_playstation
alias hid:b0005g*v0000054Cp00000DF2 hid_playstation
alias hid:b0003g*v0000054Cp00000CE6 hid_playstation
alias hid:b0005g*v0000054Cp00000CE6 hid_playstation
giselle_maz-picoctf@webshell:~$

flag aqui: 

The picoCTF flag format is 'picoCTF{}' where there is some leetspeak phrase in between the curly braces
+)JMU06c040031Q
Wrap this phrase in the flag format: g17_1n_7h3_d15k_041217d8

```
## Nots adicionales

picoCTF{g17_1n_7h3_d15k_041217d8}

## Referencias