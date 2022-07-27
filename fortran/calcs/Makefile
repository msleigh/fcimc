PYTHON = python3
EXE = ../src/imc.exe

.PHONY: clean clobber all


all: fig2.png fig3.png fig4.png fig5.png fig6.png


fig2.png: make_fig2.py calc1_output.dat
	$(PYTHON) make_fig2.py

fig3.png: make_fig3.py calc1_output.dat calc2_output.dat
	$(PYTHON) make_fig3.py

fig4.png: make_fig4.py calc1_output.dat calc3_output.dat calc4_output.dat
	$(PYTHON) make_fig4.py

fig5.png: make_fig5.py calc1_output.dat calc5_output.dat calc6_output.dat
	$(PYTHON) make_fig5.py

fig6.png: make_fig6.py calc6_output.dat calc7_output.dat
	$(PYTHON) make_fig6.py


calc1_output.dat: $(EXE) calc1.in
	$(EXE) -i calc1.in -o calc1_output.dat > calc1.out

calc2_output.dat: $(EXE) calc2.in
	$(EXE) -i calc2.in -o calc2_output.dat > calc2.out

calc3_output.dat: $(EXE) calc3.in
	$(EXE) -i calc3.in -o calc3_output.dat > calc3.out

calc4_output.dat: $(EXE) calc4.in
	$(EXE) -i calc4.in -o calc4_output.dat > calc4.out

calc5_output.dat: $(EXE) calc5.in
	$(EXE) -i calc5.in -o calc5_output.dat > calc5.out

calc6_output.dat: $(EXE) calc6.in
	$(EXE) -i calc6.in -o calc6_output.dat > calc6.out

calc7_output.dat: $(EXE) calc7.in
	$(EXE) -i calc7.in -o calc7_output.dat > calc7.out

calc1.in: ../../python/calcs/calc1.in
	cp ../../python/calcs/calc1.in ./

calc2.in: ../../python/calcs/calc2.in
	cp ../../python/calcs/calc2.in ./

calc3.in: ../../python/calcs/calc3.in
	cp ../../python/calcs/calc3.in ./

calc4.in: ../../python/calcs/calc4.in
	cp ../../python/calcs/calc4.in ./

calc5.in: ../../python/calcs/calc5.in
	cp ../../python/calcs/calc5.in ./

calc6.in: ../../python/calcs/calc6.in
	cp ../../python/calcs/calc6.in ./

calc7.in: ../../python/calcs/calc7.in
	cp ../../python/calcs/calc7.in ./

clean:
	rm -f *.pyc

clobber: clean
	rm -f *.dat *.out *.png
