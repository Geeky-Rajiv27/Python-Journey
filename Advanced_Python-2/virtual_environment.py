'''
NOTE: Ways to download Pandas of specific versions :

1)      pip install pandas==version . for eg: pandas==1.5 .Since we can keep only one verison of one package so
        while downloading any specific version the previous one will be removed if exists.

2)      to install virtualenv named package = pip install virtualenv
            to rename it : virtualenv _Newname_

3)      we can check the version of pandas : pandas.__version__

4)      To create virtual env : python3 -m venv env

5)      To rename just created env : mv env myenv

6)      To activate just renamed env : source myenv/bin/activate

7)      we can deactivate virtual environment using command : deactivate



'''

#NOTE: whenever virtual environment is activated , in terminal it doesn't show (env)
# in the beginning

'''
NOTE:   command to List all the packages in my virtual environment :

command :   pip freeze 

NOTE : we also create a .txt file called requirements.txt where we store all the 
        information of packages versions inside that txt file and we can share them
        with other's so they can also create a same virtual environment as us.

command1 :   pip freeze > requirements.txt
command2 :   pip freeze -r requirements.txt
'''