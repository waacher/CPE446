set width 200
b "fibonacci.cpp":21
cont
b exit
monitor stacktrace on
monitor stackbreak newmax
cont
monitor stackbreak off
cont
monitor stats
quit
