### Descripción

### Solución
### Solución 1 -  consola
```
se descargo y analizo hasta encontrar una carpeta secret y dentro una imagen flag, encontre el coidgo base64 y lo coverti a imagen mediante una paginan  

giselle_maz-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/262/flag.png

--2026-03-27 13:58:40--  https://artifacts.picoctf.net/c/262/flag.png

Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.77, 3.170.131.72, ...

Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.

HTTP request sent, awaiting response... 200 OK

Length: 42945 (42K) [application/octet-stream]

Saving to: 'flag.png'

  

flag.png       100%  41.94K  --.-KB/s    in 0.02s         

  

2026-03-27 13:58:40 (2.07 MB/s) - 'flag.png' saved [42945/42945]

  

giselle_maz-picoctf@webshell:~$ gem install zsteg

Fetching zsteg-0.2.14.gem

ERROR:  While executing gem ... (Gem::FilePermissionError)

    You don't have write permissions for the /var/lib/gems/3.0.0 directory.

giselle_maz-picoctf@webshell:~$ zsteg -a flag.png

[?] 3206 bytes of extra data after image end (IEND), offset = 0x9b3b

extradata:0         .. file: Zip archive data, at least v1.0 to extract, compression method=store

    00000000: 50 4b 03 04 0a 00 00 00  00 00 3d 10 70 56 00 00  |PK........=.pV..|

    00000010: 00 00 00 00 00 00 00 00  00 00 07 00 1c 00 73 65  |..............se|

    00000020: 63 72 65 74 2f 55 54 09  00 03 95 78 12 64 95 78  |cret/UT....x.d.x|

    00000030: 12 64 75 78 0b 00 01 04  00 00 00 00 04 00 00 00  |.dux............|

    00000040: 00 50 4b 03 04 14 00 00  00 08 00 3d 10 70 56 5b  |.PK........=.pV[|

    00000050: 9b f6 a9 44 0b 00 00 de  0b 00 00 0f 00 1c 00 73  |...D...........s|

    00000060: 65 63 72 65 74 2f 66 6c  61 67 2e 70 6e 67 55 54  |ecret/flag.pngUT|

    00000070: 09 00 03 95 78 12 64 95  78 12 64 75 78 0b 00 01  |....x.d.x.dux...|

    00000080: 04 00 00 00 00 04 00 00  00 00 cd 56 67 3c db 8d  |...........Vg<..|

    00000090: 16 fe 53 ab 5a 1a 7b ef  52 d7 a8 4d 25 66 5e a3  |..S.Z.{.R..M%f^.|

    000000a0: 66 89 91 88 8a 4d 6d 45  8c d8 1a 6f 75 d0 d7 6a  |f....MmE...ou..j|

    000000b0: ec d0 9a 55 14 af 95 a0  3a d4 2a 6a 94 a6 56 07  |...U....:.*j..V.|

    000000c0: 62 f3 da 23 e2 e6 7e bc  1f ee f7 7b 3e 9c e7 ec  |b..#..~....{>...|

    000000d0: f3 e5 f9 fd ce 79 64 63  6d ca c6 2a c8 0a 00 00  |.....ydcm..*....|

    000000e0: 9b d9 6d 23 18 00 d0 23  68 b6 2a 88 a6 80 83 20  |..m#...#h.*.... |

    000000f0: 19 47 1a 30 f8 1a 5a 19  02 40 e3 b3 2b 14 77 46  |.G.0..Z..@..+.wF|

giselle_maz-picoctf@webshell:~$ strings flag.png | grep "picoCTF"

giselle_maz-picoctf@webshell:~$ 

giselle_maz-picoctf@webshell:~$ Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.77, 3.170.131.72, ...

-bash: syntax error near unexpected token `('

giselle_maz-picoctf@webshell:~$ Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.

-bash: syntax error near unexpected token `('

giselle_maz-picoctf@webshell:~$ HTTP request sent, awaiting response... 200 OK

-bash: HTTP: command not found

giselle_maz-picoctf@webshell:~$ Length: 42945 (42K) [application/octet-stream]

-bash: syntax error near unexpected token `('

giselle_maz-picoctf@webshell:~$ Saving to: 'flag.png'

-bash: Saving: command not found

giselle_maz-picoctf@webshell:~$ 

giselle_maz-picoctf@webshell:~$ flag.png       100%  41.94K  --.-KB/s    in 0.02s         

-bash: flag.png: command not found

giselle_maz-picoctf@webshell:~$ 

giselle_maz-picoctf@webshell:~$ 2026-03-27 13:58:40 (2.07 MB/s) - 'flag.png' saved [42945/42945]

-bash: syntax error near unexpected token `('

giselle_maz-picoctf@webshell:~$ 

giselle_maz-picoctf@webshell:~$ giselle_maz-picoctf@webshell:~$ gem install zsteg

-bash: giselle_maz-picoctf@webshell:~$: command not found

giselle_maz-picoctf@webshell:~$ Fetching zsteg-0.2.14.gem

-bash: Fetching: command not found

giselle_maz-picoctf@webshell:~$ ERROR:  While executing gem ... (Gem::FilePermissionError)

-bash: syntax error near unexpected token `('

giselle_maz-picoctf@webshell:~$     You don't have write permissions for the /var/lib/gems/3.0.0 directory.

> giselle_maz-picoctf@webshell:~$ zsteg -a flag.png

> [?] 3206 bytes of extra data after image end (IEND), offset = 0x9b3b

> extradata:0         .. file: Zip archive data, at least v1.0 to extract, compression method=store

>     00000000: 50 4b 03 04 0a 00 00 00  00 00 3d 10 70 56 00 00  |PK........=.pV..|

>     00000010: 00 00 00 00 00 00 00 00  00 00 07 00 1c 00 73 65  |..............se|

>     00000020: 63 72 65 74 2f 55 54 09  00 03 95 78 12 64 95 78  |cret/UT....x.d.x|

>     00000030: 12 64 75 78 0b 00 01 04  00 00 00 00 04 00 00 00  |.dux............|

>     00000040: 00 50 4b 03 04 14 00 00  00 08 00 3d 10 70 56 5b  |.PK........=.pV[|

>     00000050: 9b f6 a9 44 0b 00 00 de  0b 00 00 0f 00 1c 00 73  |...D...........s|

>     00000060: 65 63 72 65 74 2f 66 6c  61 67 2e 70 6e 67 55 54  |ecret/flag.pngUT|

>     00000070: 09 00 03 95 78 12 64 95  78 12 64 75 78 0b 00 01  |....x.d.x.dux...|

>     00000080: 04 00 00 00 00 04 00 00  00 00 cd 56 67 3c db 8d  |...........Vg<..|

>     00000090: 16 fe 53 ab 5a 1a 7b ef  52 d7 a8 4d 25 66 5e a3  |..S.Z.{.R..M%f^.|

>     000000a0: 66 89 91 88 8a 4d 6d 45  8c d8 1a 6f 75 d0 d7 6a  |f....MmE...ou..j|

>     000000b0: ec d0 9a 55 14 af 95 a0  3a d4 2a 6a 94 a6 56 07  |...U....:.*j..V.|

>     000000c0: 62 f3 da 23 e2 e6 7e bc  1f ee f7 7b 3e 9c e7 ec  |b..#..~....{>...|

>     000000d0: f3 e5 f9 fd ce 79 64 63  6d ca c6 2a c8 0a 00 00  |.....ydcm..*....|

>     000000e0: 9b d9 6d 23 18 00 d0 23  68 b6 2a 88 a6 80 83 20  |..m#...#h.*.... |

>     000000f0: 19 47 1a 30 f8 1a 5a 19  02 40 e3 b3 2b 14 77 46  |.G.0..Z..@..+.wF|

>                                                         

> 

> ^C

giselle_maz-picoctf@webshell:~$ binwalk -e flag.png

  

DECIMAL       HEXADECIMAL     DESCRIPTION

--------------------------------------------------------------------------------

0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced

41            0x29            Zlib compressed data, compressed

39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/

39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2884, uncompressed size: 3038, name: secret/flag.png

42923         0xA7AB          End of Zip archive, footer length: 22

  

giselle_maz-picoctf@webshell:~$ xiftool flag.png

-bash: xiftool: command not found

giselle_maz-picoctf@webshell:~$ binwalk -e flag.png

  

DECIMAL       HEXADECIMAL     DESCRIPTION

--------------------------------------------------------------------------------

0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced

41            0x29            Zlib compressed data, compressed

39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/

39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2884, uncompressed size: 3038, name: secret/flag.png

42923         0xA7AB          End of Zip archive, footer length: 22

  

giselle_maz-picoctf@webshell:~$ cd _flag.png.extracted

giselle_maz-picoctf@webshell:~/_flag.png.extracted$ ls -r

secret  9B3B.zip  29.zlib  29

giselle_maz-picoctf@webshell:~/_flag.png.extracted$ ^C

giselle_maz-picoctf@webshell:~/_flag.png.extracted$ cd secret

giselle_maz-picoctf@webshell:~/_flag.png.extracted/secret$ ls -l

total 4

-rw-r--r-- 1 giselle_maz-picoctf giselle_maz-picoctf 3038 Mar 16  2023 flag.png

giselle_maz-picoctf@webshell:~/_flag.png.extracted/secret$ strings flag.png | grep "picoCTF"

giselle_maz-picoctf@webshell:~/_flag.png.extracted/secret$ exiftool flag.png

ExifTool Version Number         : 12.40

File Name                       : flag.png

Directory                       : .

File Size                       : 3.0 KiB

File Modification Date/Time     : 2023:03:16 02:01:57+00:00

File Access Date/Time           : 2026:03:27 14:02:01+00:00

File Inode Change Date/Time     : 2026:03:27 14:00:09+00:00

File Permissions                : -rw-r--r--

File Type                       : PNG

File Type Extension             : png

MIME Type                       : image/png

Image Width                     : 600

Image Height                    : 50

Bit Depth                       : 16

Color Type                      : Grayscale

Compression                     : Deflate/Inflate

Filter                          : Adaptive

Interlace                       : Noninterlaced

Gamma                           : 2.2

White Point X                   : 0.3127

White Point Y                   : 0.329

Red X                           : 0.64

Red Y                           : 0.33

Green X                         : 0.3

Green Y                         : 0.6

Blue X                          : 0.15

Blue Y                          : 0.06

Background Color                : 65535

Modify Date                     : 2023:03:16 02:01:57

Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)

Datecreate                      : 2023-03-16T02:01:57+00:00

Datemodify                      : 2023-03-16T02:01:57+00:00

Image Size                      : 600x50

Megapixels                      : 0.030

giselle_maz-picoctf@webshell:~/_flag.png.extracted/secret$ strings flag.png

IHDR

gAMA

 cHRM

bKGD

tIME

IDATx

kPSG

b[(*VZ/S

:56V}U(

fM**LL

nZZK

ZZFDXYi:

tu53;|

 :Z(

 "BWW

3ED,Z

99|>

ZZ--

hiQw

WT46

FF>|

~wwz

Ayya

}utL

+7WK

"-#C$R

P:s& 

F`9;

46r8*

,mm6

+004

2;;zk

??%e4

QWjk

g74XX

z^GG\

T\llll\]}

<zdj

aCxxs3A

SWLM

4!::

?}zl

[VVV

r'O>uJ pr

-55~~

;UUryx

J||{{{{u5

F`y{

9cbr

occm

YccL

;wzy

 )id7q

>>BayyBB

ZY)U

={F^

nurZ

v-4T[;"

#,L,

G_?2r

KNNMMJ

c``!

c``!

c``!

c``!

%tEXtdate:create

2023-03-16T02:01:57+00:00@\

%tEXtdate:modify

2023-03-16T02:01:57+00:001

IEND

giselle_maz-picoctf@webshell:~/_flag.png.extracted/secret$ python3 -c "print(open('flag.png', 'rb').read()[-100:])"

b'te:create\x002023-03-16T02:01:57+00:00@\\\x01#\x00\x00\x00%tEXtdate:modify\x002023-03-16T02:01:57+00:001\x01\xb9\x9f\x00\x00\x00\x00IEND\xaeB`\x82'

giselle_maz-picoctf@webshell:~/_flag.png.extracted/secret$ download flag.png

-bash: download: command not found

giselle_maz-picoctf@webshell:~/_flag.png.extracted/secret$ base64 flag.png

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

MDEBuZ8AAAAASUVORK5CYII=

giselle_maz-picoctf@webshell:~/_flag.png.extracted/secret$
```
### Notas adicionales 
picoCTF{Hiddinng_An_imag3_within_@n_ima9e_82101824}

### Referencias
https://codebeautify.org/base64-to-image-converter