# joints_calculation

### Example Figure
<div align=center>
<img src="https://github.com/FeiDao7943/joints_calculation/blob/main/example_figure/example.png" width="400px">
<img src="https://github.com/FeiDao7943/joints_calculation/blob/main/example_figure/example2.png" width="400px">
</div>


### Recent Update

**2022/12/8**
>* Welcome to joint-manipulator calculation. All these files are programming for the coursework.
>* Maybe this script still has some 'bug', but it can complete the drawing jobs of the coursework.
>* Changes that need to be made in the file `run_calculate.py` is in row 50~90 and arguement `--link_num`
There are 5 parameters need to define in common line. If the user wants to do all part of calculation with a 3-link manipulator, just need type:
`python run_calculate.py –-link_num 3 --position --jacobian --velocity --torque ` in the command line. 
>* And if just want to calculate, and generate a figure, type: `python run_calculate.py -–link_num 3` in the command line. All the result will be printed in the command line.

**2023/1/4** 
>* The code has been cluttered during the programming process in order to temporarily implement the functionality, so a new collated code may be uploaded to another repository in the near future, or perhaps a branch.

**2023/1/7** 
>* There is now a public project in my another repository called `manipulator`, which is an improved version of this project (not yet fully completed).
> Web address: https://github.com/FeiDao7943/manipulator.git

**2023/1/8** 
>* The main features and code have been added to the repository `manipulator`, including the visual GUI parameter adjustment interface and the drawing tool interface. The convergence of the calculation results between the two two books also shows the reliability. Web address: https://github.com/FeiDao7943/manipulator.git
>* There wiil ne not further changes to this repository. The subsequent updates and improvements about the calculation scripts for the robot manipulator will be transferred to the new repository.

### Attention
**Not avaliable until 16:00 at 8th Dec, 2022 in U.K. time. The main script and files will be unseen before the coursework submited.**
