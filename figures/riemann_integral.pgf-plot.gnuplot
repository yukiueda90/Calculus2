set table "riemann_integral.pgf-plot.table"; set format "%.5f"
set format "%.7e";; set samples 100; set dummy x; plot [x=0.2:1.2] (sin(2*pi*(x-0.2))+0.6)/6;
