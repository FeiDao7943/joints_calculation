# joints_calculation
> Not avaliable until 8th Dec, 2022. The main script will be unseen.

> Changes that need to be made in the file `run_calculate.py` is in row 50~90 and arguement `--link_num`

There are 5 parameters need to define in common line. If the user wants to do all part of calculation with a 3-link manipulator, just need type:
`python run_calculate.py –link_num 3 --position --jacobian --velocity --torque ` in the command line. 
  
And if just want to calculate, and generate a figure, type:
`python run_calculate.py –link_num 3`
in the command line. All the result will be printed in the command line.
