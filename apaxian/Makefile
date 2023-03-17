# out.txt : main.exe
# 	mono main.exe

# main.exe : main.cs
# 	mcs main.cs -target:exe -out:$@

# DLLS : $(addprefix -reference:,$(filter %.dll,$^))
# CODE : $(filter %.cs,$^)
# MKEXE : mcs -target:exe -out:$@ $(DLLS) $(CODE)
# MKLIB : mcs -target:library -out:$@ $(DLLS) $(CODE)

DLLS = $(addprefix -reference:,$(filter %.dll,$^))
CODE = $(filter %.cs,$^)
MKEXE = mcs -target:exe -out:$@ $(DLLS) $(CODE)
MKLIB = mcs -target:library -out:sfuns.dll apaxian.cs


all : main.exe
	mono main.exe > Out.txt

main.exe : main.cs sfuns.dll ; $(MKEXE)
sfuns.dll : apaxian.cs ; $(MKLIB)


clean : 
	rm -f *.exe
	rm -f *.txt
	rm -f *.dll