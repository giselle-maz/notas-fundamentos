### Descripción
You will find the flag after analysing this apkDownload [here](https://artifacts.picoctf.net/c/449/timer.apk).
### Solución
```

giselle_maz-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/449/timer.apk
--2026-05-04 19:59:56--  https://artifacts.picoctf.net/c/449/timer.apk
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.72, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4678467 (4.5M) [application/octet-stream]
Saving to: 'timer.apk'

timer.apk              100%[============================>]   4.46M  1.83MB/s    in 2.4s    

2026-05-04 19:59:58 (1.83 MB/s) - 'timer.apk' saved [4678467/4678467]

giselle_maz-picoctf@webshell:~$ ls -lh timer.apk
-rw-rw-r-- 1 giselle_maz-picoctf giselle_maz-picoctf 4.5M Mar 16  2023 timer.apk
giselle_maz-picoctf@webshell:~$ grep -rnE "picoCTF{.*}" .
./.bash_history:66:curl http://verbal-sleep.picoctf.net:52219/heapdump | grep -o "picoCTF{[^}]*}"
./solucion.py:14:print("picoCTF{" + "".join(flag) + "}")
giselle_maz-picoctf@webshell:~$ strings classes.dex | grep "picoCTF"
strings: 'classes.dex': No such file
giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ unzip timer.apk -d timer_extraido
Archive:  timer.apk
  inflating: timer_extraido/META-INF/com/android/build/gradle/app-metadata.properties  
  inflating: timer_extraido/classes3.dex  

do/META-INF/MANIFEST.MF  
giselle_maz-picoctf@webshell:~$ grep -as "picoCTF{" timer_extraido/classes*.dex
timer_extraido/classes3.dex:getSecondsgetText
                                             getTextViewhourshours_remaining
                                                                            hoursentereditkmillisUntilFinishedminutesminutes_remainingminutesenteredmvnameonCliconCreateonCreate$lambda-onFinishonTick
              parseBooleaparseInt*picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}playbtnsavedInstsec_remainingsecondsseconds remaining: seconds_remainingsecondsenteredsetContentViesetHours
giselle_maz-picoctf@webshell:~$ ^C
giselle_maz-picoctf@webshell:~$ ^C
```
### Notas adicionales 
picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
### Referencias