PYTHON = python3

.PHONY: clean clobber all


all: fig6.png fig5.png fig4.png fig3.png fig2.png


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


calc1_output.dat: ../src/*.py calc1.in
	$(PYTHON) ../src/imc.py -i calc1.in > calc1.out

calc2_output.dat: ../src/*.py calc2.in
	$(PYTHON) ../src/imc.py -i calc2.in > calc2.out

calc3_output.dat: ../src/*.py calc3.in
	$(PYTHON) ../src/imc.py -i calc3.in > calc3.out

calc4_output.dat: ../src/*.py calc4.in
	$(PYTHON) ../src/imc.py -i calc4.in > calc4.out

calc5_output.dat: ../src/*.py calc5.in
	$(PYTHON) ../src/imc.py -i calc5.in > calc5.out

calc6_output.dat: ../src/*.py calc6.in
	$(PYTHON) ../src/imc.py -i calc6.in > calc6.out

calc7_output.dat: ../src/*.py calc7.in
	$(PYTHON) ../src/imc.py -i calc7.in > calc7.out


clean:
	rm -f *.pyc

clobber: clean
	rm -f *.dat *.out *.png
